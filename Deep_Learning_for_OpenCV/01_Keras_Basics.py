from keras.datasets import boston_housing
from keras.layers import Dense
from keras.models import Sequential

(X_train, Y_train), (X_test, Y_test) = boston_housing.load_data()

nFeatures = X_train.shape[1]

model = Sequential()

model.add(Dense(20, input_shape=(nFeatures,), activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(optimizer='rmsprop', loss='mse', metrics=['mse', 'mae'])

model.fit(X_train, Y_train, batch_size=4, epochs=1000)

model.summary()

model.evaluate(X_test, Y_test, verbose=True)

Y_pred = model.predict(X_test)

print(Y_test[:5])
print(Y_pred[:5, 0])
