from NiftyDataLoader import NiftyDataLoader
from data_processor import DataProcessor
from strategy.momentum_strategy import MomentumStrategy
import pandas as pd

def main():
    loader = NiftyDataLoader(csv_path="data/ind_nifty500list.csv")
    clean_data_path = "data/filtered_nifty500.csv"
    # The below line is commented as the clean data for nifty500list.csv is created. If need a new one, uncomment and get the data
    # loader.create_clean_data(clean_data_path)

    df = loader.read_clean_data(filepath=clean_data_path)
    periods = [100, 75, 50, 25]
    top_symbols_dict = {}

    for period in periods:
        strategy = MomentumStrategy(period=period)
        top_symbols = strategy.screen_top(df)
        top_symbols_dict[period] = top_symbols

        print(f"\nTop Symbols for period {period}\n")
        print(top_symbols)

    # Convert the dictionary to a DataFrame with symbols and percentage values
    top_symbols_df = pd.concat(top_symbols_dict, axis=1)
    print("\nTop Symbols DataFrame\n")
    print(top_symbols_df)

if __name__ == "__main__":
    main()