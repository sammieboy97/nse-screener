from nsepython import *

class NiftyDataProcessor:
    def __init__(self):
        return

    def get_top_symbols_for_period(self, period, df):
        df = df.iloc[::-1]
        df = df.groupby('CH_SYMBOL').apply(lambda x: x['CH_CLOSING_PRICE'].pct_change(periods=period) * 100)
        df = df.groupby('CH_SYMBOL').last()
        df = df.sort_values(ascending=False)
        print(df.head(10))