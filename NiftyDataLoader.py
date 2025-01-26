import pandas as pd

class NiftyDataLoader:
    def __init__(self, csv_path="data/ind_nifty500list.csv", symbols_column="Symbol"):
        self.csv_path = csv_path
        self.symbols_column = symbols_column

    def load_data(self):
        return pd.read_csv(self.csv_path) 
    
    def get_symbols(self):
        data = self.load_data()
        return data[self.symbols_column]