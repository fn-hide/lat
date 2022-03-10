# import pandas as pd
# from manage import Manage



# df_raw = pd.read_csv('data/houses.csv')
# df_obj = Manage(df_raw, 'SalePrice')

# df_obj.view_plot()

# dir(df_obj)

# print(df_raw.info())
# print([i for i in df_raw.isnull().sum() if i > 0])
# print(df_raw.head())


pertanian = {
    'pd': (0, 1, 2*60),
    'jg': (1, 3, 5*60),
    'wt': (2, 5, 10*60),
    'tb': (3, 7, 20*60),
    'kp': (4, 9, 30*60),
    'st': (5, 11, 1*60*60),
    'tm': (6, 13, 2*60*60),
    'pn': (7, 15, 3*60*60),
    'kt': (8, 17, 4*60*60)
}

for key, val in pertanian.items():
    profit = (val[1]-val[0])*2*28
    print(key, profit, val[-1], '\t>', val[-1]/profit)
