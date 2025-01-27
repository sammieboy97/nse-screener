from strategy.base_strategy import Strategy

class DataProcessor:
    def __init__(self, loader, strategy: Strategy, clean_data_path):
        self.loader = loader
        self.strategy = strategy
        self.clean_data_path = clean_data_path

    def screen_top(self, instrument_count = 10, snapshot__back_in_days = 1):
        df = self.loader.read_clean_data(self.clean_data_path)
        return self.strategy.screen_top(df, instrument_count, snapshot__back_in_days)
    
    def screen_bottom(self, instrument_count = 10, snapshot__back_in_days = 1):
        df = self.loader.read_clean_data(self.clean_data_path)
        return self.strategy.screen_bottom(df, instrument_count, snapshot__back_in_days)