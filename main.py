from tensorflow import keras 
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt 
import seaborn as sns 
import os 
from datetime import datetime


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 



data = pd.read_csv('MicrosoftStock.csv')
print(data.head())
print(data.info())
print(data.describe())