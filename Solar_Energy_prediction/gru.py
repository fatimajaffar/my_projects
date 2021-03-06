# -*- coding: utf-8 -*-
"""GRU.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Y-eo97pVsRxX4oc5qTsJjrJ8e2vspjQ
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
import sklearn
# %matplotlib inline
# %config InlineBackend.figure_format='retina'
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
tf.random.set_seed(RANDOM_SEED)

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/Research/weather_five_minutes.csv')

df.drop(['--Timestamp---',' UV '],axis=1,inplace=True)

train_size = int(len(df) * 0.8)
test_size = len(df) - train_size
train, test = df.iloc[0:train_size], df.iloc[train_size:len(df)]
print(len(train), len(test))

from sklearn.preprocessing import MinMaxScaler
f_columns = ['Temp', 'Chill', 'Humid', 'Dewpt',' Wind ','HiWind','Rain ','Barom',' ET  ']
f_transformer = MinMaxScaler()
f_transformer = f_transformer.fit(train[f_columns].to_numpy())
train.loc[:, f_columns] = f_transformer.transform(
  train[f_columns].to_numpy()
)
test.loc[:, f_columns] = f_transformer.transform(
  test[f_columns].to_numpy()
)

solar_transformer = MinMaxScaler()
solar = solar_transformer.fit(train[['Solar']])
train['Solar'] = solar.transform(train[['Solar']])
test['Solar'] = solar.transform(test[['Solar']])

def create_dataset(X, y, time_steps=1):
    Xs, ys = [], []
    for i in range(len(X) - time_steps):
        v = X.iloc[i:(i + time_steps)].values
        Xs.append(v)
        ys.append(y.iloc[i + time_steps])
    return np.array(Xs), np.array(ys)

time_steps = 1
# reshape to [samples, time_steps, n_features]
X_train, y_train = create_dataset(train, train.Solar, time_steps)
X_test, y_test = create_dataset(test, test.Solar, time_steps)
print(X_train.shape, y_train.shape)

from keras.layers import LSTM
from keras.layers import GRU

model2 = keras.models.Sequential()
model2.add(GRU(128, input_shape=(X_train.shape[1], X_train.shape[2]),return_sequences=True))
model2.add(tf.keras.layers.LeakyReLU(alpha=0.5))
model2.add(GRU(64, return_sequences=True))
model2.add(tf.keras.layers.LeakyReLU(alpha=0.5))
model2.add(tf.keras.layers.Dropout(0.5))
model2.add(GRU(32, return_sequences=True))
model2.add(tf.keras.layers.LeakyReLU(alpha=0.5))
model2.add(tf.keras.layers.Dropout(0.5))
model2.add((GRU(16,return_sequences=False)))
model2.add(tf.keras.layers.Dropout(0.5))
model2.add(tf.keras.layers.Dense(1))

optimizer = keras.optimizers.Adam()
model2.compile(loss='mean_squared_error', optimizer=optimizer)

history2= model2.fit(
    X_train, y_train,
    epochs=30,
    batch_size=256,
    validation_split=0.1,
    shuffle=False
)

plt.rcParams["figure.figsize"] = (6,4)
plt.plot(history2.history['loss'],marker='o',label='train')
plt.plot(history2.history['val_loss'],marker='o',label='validation')
plt.title('GRU',fontsize=20)
plt.ylabel('loss ',fontsize=15)
plt.xlabel('epochs',fontsize=15)
plt.legend(fontsize=15)

y_pred2=model2.predict(X_test)
y_train_inv = solar_transformer.inverse_transform(y_train.reshape(1, -1))
y_test_inv = solar_transformer.inverse_transform(y_test.reshape(1,-1))
y_pred2_inv = solar_transformer.inverse_transform(y_pred2)

from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test,y_pred2))
print(np.sqrt(mean_squared_error(y_test,y_pred2)))
from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(y_test,y_pred2))

def percentage_error(actual, predicted):
    res = np.empty(actual.shape)
    for j in range(actual.shape[0]):
        if actual[j] != 0:
            res[j] = (actual[j] - predicted[j]) / actual[j]
        else:
            res[j] = predicted[j] / np.mean(actual)
    return res

def mean_absolute_percentage_error(y_test, y_pred): 
    return np.mean(np.abs(percentage_error(np.asarray(y_test), np.asarray(y_pred)))) * 100

mean_absolute_percentage_error(y_test, y_pred2)

plt.rcParams["figure.figsize"] = (8,3)
plt.plot(y_test[0:1000],color='orange',label="Orignial ")
plt.plot(y_pred2[0:1000],color="green",label="Forecast ")

plt.xlabel('Number of Observation',fontsize=25)
plt.ylabel('Solar Energy(W/m??)',fontsize=20)
plt.title('Solar energy prediction using GRU',fontsize=20)
plt.legend(fontsize=15)
plt.show()