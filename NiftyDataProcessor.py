from nsepython import *

class NiftyDataProcessor:
    def __init__(self, loader):
        self.loader = loader

    def create_filtered_data(self, series="EQ", start_date="25-01-2024", end_date="26-01-2025"):
        symbols = self.loader.get_nifty50_symbols()
        filtered_dfs = []

        for symbol in symbols:
            df = equity_history(symbol, series, start_date, end_date)

            if 'CH_CLOSING_PRICE' in df.columns and 'CH_SYMBOL' in df.columns:
                df = df[['CH_CLOSING_PRICE', 'CH_SYMBOL', 'CH_TIMESTAMP']]
                df['Percentage_Diff'] = df['CH_CLOSING_PRICE'].pct_change() * 100
                df['Greater_Than_30'] = df['Percentage_Diff'].abs() > 30

                if not df['Greater_Than_30'].any():
                    print(f"Symbol {symbol} has no percentage difference greater than 30%. So adding into the clean data")
                    filtered_dfs.append(df)
            else:
                print(f"Required columns not found for symbol {symbol}")

        filtered_df = pd.concat(filtered_dfs)
        print(filtered_df)
        # filtered_df.to_csv("filtered_nifty50.csv", index=False)

    def read_filtered_data(self, filepath="filtered_nifty50.csv"):
        return pd.read_csv(filepath)

    def get_top_symbols_for_period(self, period, filepath="data/filtered_nifty50.csv"):
        df = self.read_filtered_data(filepath)
        df = df.iloc[::-1]
        df = df.groupby('CH_SYMBOL').apply(lambda x: x['CH_CLOSING_PRICE'].pct_change(periods=period) * 100)
        df = df.groupby('CH_SYMBOL').last()
        df = df.sort_values(ascending=False)
        print(df.head(10))