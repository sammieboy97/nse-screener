from NiftyDataLoader import NiftyDataLoader
from data_processor import DataProcessor
from strategy.momentum_strategy import MomentumStrategy

def main():
    loader = NiftyDataLoader(csv_path="data/ind_nifty500list.csv")
    strategy = MomentumStrategy(period = 100)
    processor = DataProcessor(loader, strategy)

    clean_data_path = "data/filtered_nifty500.csv"
    # The below line is commented as the clean data for nifty500list.csv is created. If need a new one, uncomment and get the data
    # loader.create_clean_data(clean_data_path)

    top_symbols = processor.processTop(clean_data_path)
    print("Top Symbols")
    print(top_symbols)

    bottom_symbols = processor.processBottom(clean_data_path)
    print("Bottom Symbols")
    print(bottom_symbols)


if __name__ == "__main__":
    main()