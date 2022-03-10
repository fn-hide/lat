import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import re

from bs4 import BeautifulSoup



def cleaner(x):
    return re.sub('[()]*', '', x.split()[-1].upper())


ori = 'https://docs.google.com/spreadsheets/u/0/d/1-DUOjkKBh9Uf5x5umvqognJQJqAEoCZKbap8AZ0fhXo/htmlview#gid=1914265423'
edt = 'https://bit.ly/Respon-Oprec'
html = requests.get(ori)
soup = BeautifulSoup(html.text, 'lxml')
tables = soup.find_all('table')
table = tables[0]

dataset = {
    'date': [],
    'name': [],
    'nimu': [],
    'year': [],
    'drv1': [],
    'drv2': [],
    'pros': [],
    'cons': [],
    'dep1': [],
    'rea1': [],
    'dep2': [],
    'rea2': [],
    'numb': [],
}

for row in table.find_all('tr'):
    for key,col in zip(dataset.keys(), row.find_all('td')):
        dataset[key].append(col.text)

df = pd.DataFrame(dataset).drop(index=[0, 1]).reset_index(drop=True)
df.dep1 = df.dep1.apply(lambda x: cleaner(x))
df.dep2 = df.dep2.apply(lambda x: cleaner(x))
df.head()
df.dep1.unique()
df.columns


df_long = pd.melt(df, id_vars=['name', 'year'], value_vars=['dep1', 'dep2'])
df_long.head()

myplt = sns.catplot(data=df_long, x='value', hue='variable', kind='count', order=df.dep1.unique(), palette='hls')
myplt.set_xticklabels(rotation=45)
myplt.tight_layout()
myplt.set_xlabels('Departments')
myplt.set_ylabels('Candidates')

new_legends = ['1st', '2nd']
myplt._legend.set_title('Choices')
for new_legend, legend in zip(new_legends, myplt._legend.texts):
    legend.set_text(new_legend)
    
plt.show()

myplt = sns.catplot(data=df_long, x='value', col='year', hue='variable', kind='count', palette='hls')
myplt.set_xlabels('Departments')
myplt.set_ylabels('Candidates')
myplt.set_xticklabels(rotation=45)
myplt.tight_layout()

new_legends = ['1st', '2nd']
myplt._legend.set_title('Choices')
for new_legend, legend in zip(new_legends, myplt._legend.texts):
    legend.set_text(new_legend)

n = 2021
for i in myplt.axes:
    for j in i:
        j.set_title('Angkatan ' + str(n))
        n -= 1
        
plt.show()


