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

print("./data directory:", os.listdir("./data"))
# ./data directory: ['train.csv', 'gender_submission.csv', 'test.csv']

train = pd.read_csv("./data/train.csv")
test = pd.read_csv("./data/test.csv")

