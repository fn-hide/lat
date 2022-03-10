import pandas as pd

from glob import glob



class Preprocessing:
    def __init__(self, path):
        self.filepaths = glob(path)
        self.target = 'rain'
        self.colnames = ['date', 'temp', 'hum', self.target, 'sun', 'wind']
        self.df_all = pd.DataFrame()
        
    def concate_all(self):
        list_df = []
        for filepath in self.filepaths:
            df = pd.read_excel(filepath, names=self.colnames, skipfooter=8)
            df.dropna(axis=0, subset=['date'], inplace=True)
            df.drop(index=df.index[0], inplace=True)
            
            list_df.append(df)
            
        self.df_all = pd.concat(list_df, ignore_index=True)
        self.df_all.set_index('date', inplace=True)
        
    def change8888(self):
        self.df_all.replace({8888:0}, inplace=True)
        
    def fillmissing(self):
        self.df_all = self.df_all.interpolate()
        self.df_all = self.df_all.fillna(0)
    
    def datetiming(self):
        self.df_all.index = pd.to_datetime(self.df_all.index, format='%d-%m-%Y')
        
    def resampling(self):
        self.df_all = self.df_all.resample('W').sum()
    
    def scaling(self):
        for col in self.df_all.columns:
            if col != self.target:
                self.df_all[col] = self.df_all[col].transform(lambda x: (x-x.min())/(x.max()-x.min()))
    
    def get_inou(self):
        return self.df_all.drop(columns=[self.target]), self.df_all[self.target]
        
    
    
    # TODO: Do and check correct file sorting from glob
    # TODO: Make your fillmissing own methods
