import numpy as np
import tensorflow as tf
import pickle
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense, SimpleRNN
from tensorflow.keras.optimizers import Adam



model = load_model('IMFmachinelearning_dscovr')


def prediction_dscovr(x_prediction):
    h = model.predict(x_prediction).tolist() 
    for i in range(len(h)):
         h[i] = (h[i][0]*2 -1)*20
    return(h)


f_dscovr = open(r"C:\Users\alexa\Desktop\hackaton\pickle files\dscovr.pkl", 'rb')


dscovr = pickle.load(f_dscovr)

dscovr = dscovr[15000:16001]

x_f, y_f = [element[0] for element in dscovr], [element[1] for element in dscovr]


for i in range(len(x_f)):
    for j in range(len(x_f[0])):
        x_f[i][j] = x_f[i][j] / 20
        x_f[i][j] = (x_f[i][j] + 1) / 2

X = np.array([np.array(element) for element in x_f])
y = np.array(y_f)


predicted_values = [prediction_dscovr(X)]
real_values = y_f

plt.plot(predicted_values[0])
plt.plot(real_values)
plt.ylabel("IMF Z component")
plt.xlabel("blue = predicted values, orange = real_values")
plt.show()