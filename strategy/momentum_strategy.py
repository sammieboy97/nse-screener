
from .base_strategy import Strategy
import pandas as pd


class MomentumStrategy(Strategy):

    def __init__(self, periods = [100, 75, 50, 25]):
        self.periods = periods

    def execute_strategy(self, df: pd.DataFrame, instrument_count = 10) -> pd.DataFrame:
        top_symbols_dict = {}

        for period in self.periods:
            df = df.iloc[::-1]
            top_symbols = df.groupby('CH_SYMBOL').apply(lambda x: x['CH_CLOSING_PRICE'].pct_change(periods=period) * 100)
            top_symbols = top_symbols.groupby('CH_SYMBOL').last()
            top_symbols = top_symbols.sort_values(ascending=False)
            top_symbols = top_symbols.head(instrument_count)
            top_symbols_dict[period] = top_symbols

            print(f"\nTop Symbols for period {period}\n")
            print(top_symbols)
        
        top_symbols_df = pd.concat(top_symbols_dict, axis=1)
        return top_symbols_df