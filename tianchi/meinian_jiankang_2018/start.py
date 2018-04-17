import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import os

print("./data directory:", os.listdir("./data"))

data_part_1 = pd.read_csv("./data/meinian_round1_data_part1_20180408.txt", '$')
data_part_2 = pd.read_csv("./data/meinian_round1_data_part2_20180408.txt", '$')
data_test_a = pd.read_csv("./data/[new] meinian_round1_test_a_20180409.csv", ',')
data_train = pd.read_csv("./data/meinian_round1_train_20180408.csv", ',')
