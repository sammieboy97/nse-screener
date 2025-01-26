from NiftyDataLoader import NiftyDataLoader
from NiftyDataProcessor import NiftyDataProcessor

def main():
    loader = NiftyDataLoader(csv_path="data/ind_nifty500list.csv")
    processor = NiftyDataProcessor(loader)
    # processor.create_clean_data()
    processor.get_top_symbols_for_period(100)


if __name__ == "__main__":
    main()