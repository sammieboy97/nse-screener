import NiftyDataLoader as NiftyDataLoaderModule
import NiftyDataProcessor as NiftyDataProcessorModule

def main():
    loader = NiftyDataLoaderModule.NiftyDataLoader()
    processor = NiftyDataProcessorModule.NiftyDataProcessor(loader)
    # processor.create_filtered_data()
    processor.get_top_symbols_for_period(100)


if __name__ == "__main__":
    main()