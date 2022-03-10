from cmath import sqrt
from preprocessing import Preprocessing
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np
from random import random, randint
from sklearn.metrics import r2_score, mean_absolute_percentage_error, mean_absolute_error, mean_squared_error
from forecasting_metrics import maape



def split_sequences(sequences, n_steps):
	X, y = list(), list()
	for i in range(len(sequences)):
		end_ix = i + n_steps
		if end_ix > len(sequences):
			break
		seq_x, seq_y = sequences[i:end_ix, :-1], sequences[end_ix-1, -1]
		X.append(seq_x)
		y.append(seq_y)
	return np.array(X), np.array(y)



pre_obj = Preprocessing('data/*.xlsx')
pre_obj.concate_all()
pre_obj.change8888()
pre_obj.fillmissing()
pre_obj.datetiming()
pre_obj.resampling()
pre_obj.scaling()

print(pre_obj.df_all.head())

hujan = pre_obj.df_all['rain']
pred = [randint(1, 30)+i for i in hujan]

r2_score(hujan, pred), mean_absolute_percentage_error(hujan, pred), mean_squared_error(hujan, pred), mean_absolute_error(hujan, pred), np.sqrt(mean_squared_error(hujan, pred))

maape(hujan, pred)

plt.plot(hujan, label='hujan')
plt.plot(hujan.index, pred, label='predicted')
plt.legend()
plt.show()

# print(pre_obj.df_all.head())

# X, y = pre_obj.get_inou()

# dataset = np.hstack((X.values, y.values.reshape(-1, 1)))

# Xtrain, ytrain = split_sequences(dataset, 3)

# _, n_steps, n_features = Xtrain.shape
# print(n_steps, n_features)

# model = Sequential()
# model.add(LSTM(50, activation='relu'))
# model.add(Dense(1))
# model.compile(optimizer='Adam', loss='mse')
# model.fit(Xtrain, ytrain, epochs=100, verbose=0)
# yhat = model.predict(Xtrain, verbose=0)
# print(yhat)

# plot_cols = list(pre_obj.df_all.columns)
# plot_features = pre_obj.df_all[plot_cols]
# plot_features.index = pre_obj.df_all.index
# _ = plot_features.plot(subplots=True, figsize=(15,10))

# plt.plot(yhat)
# plt.plot(ytrain)
# plt.show()



