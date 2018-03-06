import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import os

print("./data directory:", os.listdir("./data"))

train_raw = pd.read_csv("./data/new yancheng_train_20171226.csv")
test_sample_A = pd.read_csv("./data/yancheng_testA_20171225.csv")
test_sample_B = pd.read_csv("./data/yancheng_testB_20180224.csv")

def prepare_data():
  # get car sales per month per class_id
  # e.g. {class_id_1: { 201201: 104}}
  sales = {}
  for index, row in train_raw.iterrows():
    class_id = row.class_id
    sale_date = row.sale_date
    sale_quantity = row.sale_quantity
    if class_id not in sales:
      sales[class_id] = {}
    if sale_date not in sales:
      sales[class_id][sale_date] = 0
    sales[class_id][sale_date] += sale_quantity
  # sale dates
  month_list = list(set(train_raw.sale_date.values))
  month_list.sort()
  # class_ids
  class_id_list = list(set(train_raw.class_id.values))
  class_id_list.sort()
  return sales, month_list, class_id_list

def make_train_data(sales_dict, month_list, class_id_list, lastN=3, predict=False):
  # df = DataFrame(table, columns=headers) 
  # - table = [['Heading1', 'Heading2'], [1 , 2], [3, 4]]
  # - headers = table.pop(0) # gives the headers as list and leaves data
  headers = ["class_id"]
  for i in range(lastN):
    headers.append("last_"+ str(i+1))
  headers.append("Y")
  table = []
  for class_id in class_id_list:
    for start in range(len(month_list)-lastN+1):
      if not predict and start == (len(month_list)-lastN):
        continue
      row = [class_id]
      for i in range(start, start+lastN):
        sale_record = sales_dict.get(class_id, {}).get(month_list[i], 0)
        row.append(sale_record)
      sale_Y = None if predict else sales_dict.get(class_id, {}).get(month_list[start+lastN])
      if not sale_Y and not predict:
        continue
      row.append(sale_Y)
      table.append(row)

  df = pd.DataFrame(table, columns=headers)      
  return df

# Solution_0: make linear regression working.
def solution_0():
  data_X = pd.DataFrame({
             'compartment': train_raw.compartment,
             'quality': train_raw.total_quality,
             'sale_quantity': train_raw.sale_quantity,
             'sale_date': train_raw.sale_date % 100})
  data_Y = train_raw["sale_quantity"]
  train_X = data_X[0:10000]
  train_Y = data_Y[0:10000]
  test_Y = data_Y[10000:10100]
  test_X = data_X[10000:10100]
  
  model = LinearRegression()
  model.fit(train_X, train_Y)
  print("model.coef_ = ", model.coef_)
  print("model.score = ", model.score(test_X, test_Y))

# Now we have 201201 to 201710, we need to predict 201711.
# Solution 1: predict car sales based on previous 8 days data.
# for day 1,2,3: predict day 4.
def solution_1(N=3):
  sales_dict, month_list, class_id_list = prepare_data()
  df = make_train_data(sales_dict, month_list, class_id_list, lastN=N)
  df = df.sample(frac=1).reset_index(drop=True)

  data_X = pd.DataFrame()
  for i in range(N):
    data_X["last_"+str(i+1)] = df["last_"+str(i+1)]
  # print(data_X)
  # data_X = pd.DataFrame({
  #            'last_1': df.last_1,
  #            'last_2': df.last_2,
  #            'last_3': df.last_3,
  #            })
  data_Y = df.Y
  test_size = int(len(df)/5)
  train_X = data_X[:-test_size]
  train_Y = data_Y[:-test_size]
  test_Y = data_Y[-test_size:]
  test_X = data_X[-test_size:]

  model = LinearRegression()
  model.fit(train_X, train_Y)
  print("train_size:", len(train_X), ", test_size", len(test_X))
  print("model.coef_ = ", model.coef_)
  print("model.score = ", model.score(test_X, test_Y))
  return model.score(test_X, test_Y), model.coef_,model

# summary = []
# for i in range(12):
#   score, coef, model = solution_1(i+1)
#   summary.append([i+1, score, coef, model])
# 
# for entry in summary:
#   print(entry)

def submit_1():
  sales_dict, month_list, class_id_list = prepare_data()
  # Use last 9 days history.
  N = 9
  _, _, model = solution_1(N=N)
  df = make_train_data(sales_dict, month_list[-N:], class_id_list, lastN=N, predict=True)
  predict_X = pd.DataFrame()
  for i in range(N):
    predict_X["last_"+str(i+1)] = df["last_"+str(i+1)]
  # print(predict_X)
  predict_Y = model.predict(predict_X)
  # print(predict_Y)
  out_df = pd.DataFrame({
    "predict_date": 201711,
    "class_id": class_id_list,
    "predict_quantity": predict_Y,
  })
  return out_df

out_df = submit_1()
out_df.to_csv('linear_regression_last_9_records.csv', columns=['predict_date', 'class_id', 'predict_quantity'], index=False)
