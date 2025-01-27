
from .base_strategy import Strategy
import pandas as pd


class MomentumStrategy(Strategy):

    def __init__(self, periods = [100, 75, 50, 25]):
        self.periods = periods
    
    def screen_stocks(self, isTop, df: pd.DataFrame, instrument_count = 10, snapshot__back_in_days = 1) -> pd.DataFrame:
        top_symbols_dict = {}

        # Filter out symbols with less than 200 rows
        symbol_counts = df['CH_SYMBOL'].value_counts()
        valid_symbols = symbol_counts[symbol_counts >= 200].index
        df = df[df['CH_SYMBOL'].isin(valid_symbols)]

        for period in self.periods:
            df_period = df.copy()
            df_period = df_period.iloc[::-1]
            df_period['PCT_CHANGE'] = df_period.groupby('CH_SYMBOL')['CH_CLOSING_PRICE'].pct_change(periods=period) * 100
            df_period = df_period.groupby('CH_SYMBOL').apply(lambda x: x.iloc[-snapshot__back_in_days] if len(x) > snapshot__back_in_days else x.iloc[-1])
            df_period = df_period.sort_values(by='PCT_CHANGE', ascending=not isTop)
            top_symbols = df_period[['CH_SYMBOL', 'PCT_CHANGE']].head(instrument_count)
            
            top_symbols_dict[period] = top_symbols

            print(f"\nTop Symbols for period {period}\n")
            print(top_symbols)

        top_symbols_df = pd.concat(top_symbols_dict, axis=1)

        # Keep only rows with more than one non-NaN value
        top_symbols_df = top_symbols_df.dropna(thresh=2)


        return top_symbols_df

    def execute_trade(self, df, top_symbols_df, buy_day, sell_day):
        weightedDifferencePercentageSum = 0
        differenceSum = 0
        capitalNeeded = 0
        df = df.iloc[::-1]
        for symbol in top_symbols_df.index:
            signal_buy_day_df = df.groupby('CH_SYMBOL').apply(lambda x: x.iloc[-buy_day] if len(x) > buy_day else x.iloc[0])
            signal_sell_day_df = df.groupby('CH_SYMBOL').apply(lambda x: x.iloc[-sell_day] if len(x) > sell_day else x.iloc[0])
            buy_day_price = signal_buy_day_df.loc[symbol, 'CH_CLOSING_PRICE'] if symbol in signal_buy_day_df.index else None
            sell_day_price = signal_sell_day_df.loc[symbol, 'CH_CLOSING_PRICE'] if symbol in signal_sell_day_df.index else None
            difference = sell_day_price - buy_day_price
            differencePercentage = (difference / buy_day_price) * 100
            print(f"Symbol: {symbol}, Buy Price: {buy_day_price}, Sell Price: {sell_day_price}, Difference: {difference}, Difference Percentage: {differencePercentage}")
            differenceSum += difference
            capitalNeeded += buy_day_price
            weightedDifferencePercentageSum += (differencePercentage * buy_day_price)

        totalDifferencePercentage = (weightedDifferencePercentageSum / capitalNeeded) if capitalNeeded != 0 else 0
        print(f"Total Difference: {differenceSum}, Total Capital Needed: {capitalNeeded}, Total Difference Percentage: {totalDifferencePercentage}")
        return totalDifferencePercentage, capitalNeeded
    