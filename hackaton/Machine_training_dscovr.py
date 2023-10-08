import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN
from tensorflow.keras.optimizers import Adam
import pickle

# Open the DSCOVR pickle file
f_dscovr = open(r"C:\Users\alexa\Desktop\hackaton\pickle files\dscovr.pkl", 'rb')

# Load DSCOVR data from the pickle file
dscovr = pickle.load(f_dscovr)

# Limit DSCOVR data to the first 15000 elements
dscovr = dscovr[:15000]

# Extract input (x_f) and target (y_f) data from DSCOVR
x_f, y_f = [element[0] for element in dscovr], [element[1] for element in dscovr]

# Preprocess the data
for i in range(len(x_f)):
    for j in range(len(x_f[0])):
        x_f[i][j] = x_f[i][j] / 20
        x_f[i][j] = (x_f[i][j] + 1) / 2

for k in range(len(y_f)):
    y_f[k] = y_f[k] / 20
    y_f[k] = (y_f[k] + 1) / 2

X = np.array([np.array(element) for element in x_f])
y = np.array(y_f)

# Generate example data (you should replace this with your actual data)
# X contains measurements from the previous 10 seconds
# y contains the magnetic field at time t

# Split the data into training and test sets
train_size = int(0.8 * len(X))
X_train, X_test = X[train_size:], X[:train_size]
y_train, y_test = y[train_size:], y[:train_size]

# Create the RNN model
model = Sequential()
model.add(SimpleRNN(units=64, activation='relu', input_shape=(10, 1)))
model.add(Dense(1))

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=400, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model on the test set
loss = model.evaluate(X_test, y_test)

# Use the model to make predictions
predictions = model.predict(X_test)

# You can now use "predictions" to get predictions of the magnetic field at a given time

# Save the model
model.save('IMFmachinelearning_dscovr')