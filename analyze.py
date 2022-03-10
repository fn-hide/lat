import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('data/auto.csv')

for col in df.columns:
    uniqval = df[col].unique()
    df[col].replace({'?': np.nan}, inplace=True)

# print(df.isnull().sum())

# sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
# plt.tight_layout()
# plt.show()


# mengisi data hilang: fillmissing

check = df.isnull().sum()
null_col = [check.index[i] for i,null_count in enumerate(check) if null_count != 0]


for col in null_col:
    # print(df[col].head())
    try:
        df[col] = pd.to_numeric(df[col])
        df[col].fillna(df[col].mean(), inplace=True)
    except:
        df[col].fillna(method='bfill', inplace=True)

# sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
# plt.tight_layout()
# plt.show()

# sns.heatmap(df.corr(), cmap='bwr', annot=True)
# plt.tight_layout()
# plt.show()

# sns.boxplot(x='price', y='num-of-doors', data=df)
# plt.tight_layout()
# plt.show()


sns.pairplot(df, vars=['price', 'engine-size'])
plt.tight_layout()
plt.show()



