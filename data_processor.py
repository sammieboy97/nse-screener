from strategy.base_strategy import Strategy

class DataProcessor:
    def __init__(self, loader, strategy: Strategy, clean_data_path):
        self.loader = loader
        self.strategy = strategy
        self.clean_data_path = clean_data_path

    def processTop(self, instrument_count = 10):
        df = self.loader.read_clean_data(self.clean_data_path)
        return self.strategy.screen_top(df, instrument_count)
    
    def processBottom(self, instrument_count = 10):
        df = self.loader.read_clean_data(self.clean_data_path)
        return self.strategy.screen_bottom(df, instrument_count)