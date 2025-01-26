from NiftyDataLoader import NiftyDataLoader
from NiftyDataProcessor import NiftyDataProcessor

def main():
    loader = NiftyDataLoader(csv_path="data/ind_nifty500list.csv")
    processor = NiftyDataProcessor(loader)

    clean_data_path = "data/filtered_nifty500.csv"
    # The below line is commented as the clean data for nifty500list.csv is created. If need a new one, uncomment and get the data
    # processor.create_clean_data(clean_data_path)

    df = loader.read_clean_data(filepath=clean_data_path)
    
    processor.get_top_symbols_for_period(100, df)


if __name__ == "__main__":
    main()