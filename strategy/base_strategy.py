import pandas as pd
from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def screen_stocks(self, isTop, df: pd.DataFrame, instrument_count = 10, snapshot__back_in_days = 1) -> pd.DataFrame:
        pass

    def screen_top(self, df: pd.DataFrame, instrument_count: int = 10, snapshot__back_in_days = 1) -> pd.DataFrame:
        df = self.screen_stocks(True, df, instrument_count, snapshot__back_in_days)
        return df

    def screen_bottom(self, df: pd.DataFrame, instrument_count: int = 10, snapshot__back_in_days = 1) -> pd.DataFrame:
        df = self.screen_stocks(False, df, instrument_count, snapshot__back_in_days)
        return df
    
    