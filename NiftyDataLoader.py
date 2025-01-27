import pandas as pd
from nsepython import *

class NiftyDataLoader:
    def __init__(self, csv_path="data/ind_nifty500list.csv", symbols_column="Symbol"):
        self.csv_path = csv_path
        self.symbols_column = symbols_column

    def load_data(self):
        return pd.read_csv(self.csv_path) 
    
    def get_symbols(self):
        data = self.load_data()
        return data[self.symbols_column]
    
    def read_clean_data(self, filepath="data/filtered_nifty500.csv"):
        return pd.read_csv(filepath)
    
    
    def create_clean_data(self, clean_data_path, series="EQ", start_date="25-01-2024", end_date="26-01-2025"):
        symbols = self.get_symbols()
        filtered_dfs = []

        for symbol in symbols:
            df = equity_history(symbol, series, start_date, end_date)

            if 'CH_CLOSING_PRICE' in df.columns and 'CH_SYMBOL' in df.columns:
                df = df[['CH_CLOSING_PRICE', 'CH_SYMBOL', 'mTIMESTAMP']]
                df['Percentage_Diff'] = df['CH_CLOSING_PRICE'].pct_change() * 100
                df['Greater_Than_30'] = df['Percentage_Diff'].abs() > 30

                if not df['Greater_Than_30'].any():
                    print(f"Symbol {symbol} has no percentage difference greater than 30%. So adding into the clean data")
                    filtered_dfs.append(df)
            else:
                print(f"Required columns not found for symbol {symbol}")

        filtered_df = pd.concat(filtered_dfs)
        filtered_df.to_csv(clean_data_path, index=False)