import math
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import pandas as pd
import pandas as pd
import tensorflow as tf
import tensorflow as tf
import os

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LinearRegression

# print("./data directory:", os.listdir("./data"))

# ./data directory: ['tianchi_fresh_comp_train_user.csv', 'tianchi_fresh_comp_train_item.csv']

train_user = pd.read_csv("./data/tianchi_fresh_comp_train_user.csv")
train_item = pd.read_csv("./data/tianchi_fresh_comp_train_item.csv")

