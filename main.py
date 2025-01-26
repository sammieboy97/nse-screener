from NiftyDataLoader import NiftyDataLoader
from NiftyDataProcessor import NiftyDataProcessor

def main():
    loader = NiftyDataLoader(csv_path="data/ind_nifty500list.csv")
    processor = NiftyDataProcessor(loader)

    # The below line is commented as the clean data for nifty500list.csv is created. If need a new one, uncomment and get the data
    # processor.create_clean_data()
    
    processor.get_top_symbols_for_period(100)


if __name__ == "__main__":
    main()