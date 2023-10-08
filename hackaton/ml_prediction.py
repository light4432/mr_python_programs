import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense, SimpleRNN
from tensorflow.keras.optimizers import Adam
import pickle

global model 
model = load_model('IMFmachinelearning_dscovr')


#-------------
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

#-------------



def prediction_ace(x_prediction):
    h = model.predict(x_prediction).tolist() 
    return(h)


def multiple_prediction(n , x_prediction):
    if n >= 10:
        return(x_prediction)
    else : 
          h = prediction_ace(np.array([x_prediction]))[0][0]
          x_prediction = x_prediction.tolist()
          n+=1
          x_prediction = [x_prediction[i] for i in range(1,10)]
          x_prediction.append(h)          
          return(multiple_prediction(n, np.array(x_prediction)))

     


print(multiple_prediction(0,X[0]))
