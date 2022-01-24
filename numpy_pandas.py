from matplotlib.pyplot import axis
import numpy as np
import pandas as pd
from glob import glob
import os

# arr = np.array([1, 2, 3, 4], dtype=np.float32)

# zero = np.zeros(10)
# one = np.ones((3, 3))
# ful = np.full((3, 3), 3)

# arr2 = np.arange(1, 10, 2)
# rand = np.random.randint((3, 3))

# eyes = np.eye(3)

# empti = np.empty(3)

# print('arr')
# print(arr)
# print('zero')
# print(zero)
# print('one')
# print(one)
# print('ful')
# print(ful)
# print('arr2')
# print(arr2)
# print('rand')
# print(rand)
# print('eyes')
# print(eyes)
# print('empti')
# print(empti)

# arr = np.array([range(i, i+3) for i in [6, 7, 8]])
# print(arr)
# print('ndim', arr.ndim)
# print('ndim', arr.shape)
# print('ndim', arr.size)
# print('ndim', arr.dtype)

# arr = np.arange(10)
# print(arr)
# print(arr[::2])
# print(arr[::-1])

# x = np.array([[3, 5, 7, 6], [7, 6, 8, 8], [1, 6, 7, 7]])
# x_sub = x[:2, :2].copy()
# x_sub[0, 0] = 1000
# print(x)
# print(x_sub)

# arr = np.arange(1, 4)
# arr2 = np.arange(4, 7)
# # arr3 = np.concatenate([arr, arr2], axis=1)
# arr3 = np.vstack([arr, arr2])
# print(arr)
# print(arr2)
# print(arr3)

# grid = np.arange(16).reshape((4, 4))
# upper, lower = np.vsplit(grid, [2])
# left, right = np.hsplit(grid, [2])

# print(grid)
# print(upper, lower)
# print(left, right)

df = pd.read_excel('data/laporan harian 400.xlsx', skiprows=8, skipfooter=11)

# print(df.loc[:5, ['Tanggal', 'Tavg']])  # eksklusif
# print(df.iloc[:5, [1, 3, 5]])           # inklusif

# print(df.RR)
# print(df['RR'])
# print(df.RR is df['RR'])

# print('belum')
# print(df.set_index('Tanggal'))
# print(df)

# print('sudah')
# df.set_index('Tanggal', inplace=True)
# print('df')
# print(df)

# print(df.head())
# print(df.fillna(method='bfill').head())
# print(df.fillna(method='ffill').head())

# print(pd.to_datetime("20150704"))
# print(pd.to_datetime("20150704") + pd.to_timedelta(np.arange(12), 'D'))

# print(pd.date_range('01-01-2015', periods=10, freq='d'))
# df = df.fillna(0)
# print(df.RR)
# print(df.RR.apply(lambda x: x-x//2))
# print(df.RR.transform(lambda x: x-x.mean()))

'''
- membaca file
- concatenation
- buat dataset
- interpolasi linier "pandas interpolasi"
- mengubah tanggal ('str') to datetime64

[optional]
- resample('W')
- x-x.min() / abs(x.max() - x.min()) --> min max scaler
- ubah nama columns
'''

filepaths = glob('data/*.xlsx')
filepaths = os.listdir('data')
