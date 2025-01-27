from NiftyDataLoader import NiftyDataLoader
from data_processor import DataProcessor
from strategy.momentum_strategy import MomentumStrategy
import pandas as pd

def main():
    loader = NiftyDataLoader(csv_path="data/ind_nifty500list.csv")
    clean_data_path = "data/filtered_nifty500.csv"
    # The below line is commented as the clean data for nifty500list.csv is created. If need a new one, uncomment and get the data
    # loader.create_clean_data(clean_data_path)

    periods = [100, 75, 50, 25]
    strategy = MomentumStrategy(periods=periods)
    processor = DataProcessor(loader=loader, strategy=strategy, clean_data_path=clean_data_path)

    top_stocks = processor.processTop(12)
    print(top_stocks)

if __name__ == "__main__":
    main()