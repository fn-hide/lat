from contextlib import nullcontext
from enum import auto
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/auto.csv')
df.columns = [column.replace('-', '_') for column in df.columns]
df.columns
print(df.isnull().sum())
print(df.info())
df.isnull().sum()

for col in df.columns:
    # uniqval = df[col].unique()
    # print(f'{col} >>> {uniqval}')
    # df[col].replace({'?': np.nan}, inplace=True)
    
    val, cnt = np.unique(df[col], return_counts=True)
    

sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.tight_layout()
plt.show()

df.isnull().sum()

check = df.isnull().sum()
null_col = [check.index[i] for i, null_count in enumerate(check) if null_count != 0]
print(null_col)
    
for col in null_col:
    print(df[col].head())
    try:
        df[col] = pd.to_numeric(df[col])
        df[col].fillna(df[col].mean(), inplace=True)
    except:
        df[col].fillna(method='bfill', inplace=True)

# sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
# plt.tight_layout()
# plt.show()

sns.heatmap(df.corr(), annot=True, cmap='bwr', fmt='.2f')
plt.tight_layout()
plt.show()

sns.pairplot(df, vars=['price', 'horsepower'])
sns.jointplot('price', 'horsepower', data=df)
plt.tight_layout()
plt.show()

# TODO: engine_size toward price
# TODO: highway_mpg toward price
# TODO: num_of_doors toward price

sns.catplot(x='symboling', y='price', data=df, kind='violin')
sns.scatterplot(x='normalized_losses', y='price', data=df)
# sns.boxplot(x='num_of_doors', y='price', data=df)
plt.tight_layout()
plt.show()

df.columns
df.info()

# plot using pandas: df[list_selected_columns].hist(bins=15, figsize=(15, 6), layout=(2, 4));
# sns.countplot(df['columns']);

