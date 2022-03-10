from turtle import down
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/titanic.csv')
print(df.head())
print(df.columns)

catplt = sns.catplot(x='Survived', col='Embarked', row='Sex', hue='Pclass', kind='count', data=df)
catplt = sns.catplot(x='Embarked', y='Fare', kind='violin', hue='Survived', data=df)

violin = sns.violinplot(data=df, x='Embarked', y='Fare', hue='Survived', split=True)
plt.show()

for i in catplt.axes:
    for j in i:
        for k in j.patches:
            h, w, x = k.get_height(), k.get_width(), k.get_x()
            j.annotate(
                format(h, '.0f'), (x+w / 2, h), 
                ha='center', va='center', xytext=(0, 9), textcoords='offset points'
            )

catplt.set(ylim=(-10, 275))

plt.show()


print(df.columns)
df.SibSp.unique()
df.Parch.unique()

catplt1 = sns.catplot(x='SibSp', hue='Survived', kind='count', data=df)
catplt2 = sns.catplot(x='Parch', hue='Survived', kind='count', data=df)

fig = plt.figure()
gs  = fig.add_gridspec(1, 2)

with sns.axes_style('whitegrid'):
    ax = fig.add_subplot(gs[0, 0])
    sns.catplot(x='SibSp', hue='Survived', kind='count', data=df)
with sns.axes_style('whitegrid'):
    ax = fig.add_subplot(gs[0, 1])
    sns.catplot(x='Parch', hue='Survived', kind='count', data=df)

fig.tight_layout()
plt.show()













