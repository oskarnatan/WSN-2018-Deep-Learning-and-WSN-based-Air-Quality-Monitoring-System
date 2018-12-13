"""
Created on Wed Nov 21 12:34:38 2018

@author: Oskar
"""

#IMPORT PACKAGES
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.optimizers import Adam
from keras.utils import plot_model

#AMBIL MODEL DNN, METRIC FUNCTION
from oskarlib.deeplearning import DNN
from oskarlib.metricfunction import RegMetric


#TUNING PARAMETER DEEP LEARNING
np.random.seed(10000)
epoch = 10000
lrate = 0.0005


#LOAD DATASET dan SCALING minmax
dataset = pd.read_excel("dataset\AirQualityUCI.xlsx")
array = dataset.values
X = array[:,0:2]
mmxs = MinMaxScaler()
X = mmxs.fit_transform(X)
Y = array[:,2:3]


time_start = time.clock()
#CALL NN FROM OSKARLIB
model = DNN.Regressor(input=len(X[0]), output=len(Y[0]))

#SET OPTIMIZER, LOSS FUNCTION, METRICS, LRATE
optim = Adam(lr=lrate, decay=0.0)
model.compile(optimizer=optim, loss='logcosh', metrics=['mean_absolute_error'])
#model.compile(optimizer=optim, loss='mean_absolute_error', metrics=[RegMetric.R2])

#TRAIN NN
H = model.fit(X, Y, epochs=epoch, batch_size=10)
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

com_time = (time.clock() - time_start)
print(com_time)

#SAVE MODEL dan VISUALISASINYA
model.save("AQreg.h5")
plot_model(model, to_file='AQreg.jpg')

#PLOT GRAPH REGRESI
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, epoch), H.history["loss"], label="Loss")
plt.plot(np.arange(0, epoch), H.history["mean_absolute_error"], label="MAE") #regresi
plt.title("Loss and MAE")
plt.xlabel("Epoch #")
plt.ylabel("Loss/MAE")
plt.legend(loc="upper left")
plt.savefig("AQreg.png")

"""
### HASIL TRAIN
DNN.Regressor
epoch = 10000
lrate = 0.0005
LOSS LOGCOSH : 0.1533
MAE : 0.3898
Comp Time: 4062.1350362794105
"""