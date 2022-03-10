import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



class Manage:
    def __init__(self, df, target) -> None:
        self.df_all = df
        self.df_cat = df.select_dtypes(include='object')
        self.df_num = df.select_dtypes(exclude='object')
        self.params = df.drop(columns=[target])
        self.target = df[target]
    
    def view_uniqval(self, dataset, thresh=np.inf):
        for col in dataset.columns:
            uniqval = dataset[col].unique()
            if len(uniqval) < thresh:
                print(col, '>>>', uniqval)
                
    def view_plot(self):
        for col in self.df_cat.columns:
            sns.catplot(x=col, y=self.target.columns, kind='count', data=self.df_cat)
        else:
            plt.show()
    
