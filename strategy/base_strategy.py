import pandas as pd
from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def execute_strategy(self, df: pd.DataFrame, instrument_count = 10) -> pd.DataFrame:
        pass

    def screen_top(self, df: pd.DataFrame, instrument_count: int = 10) -> pd.DataFrame:
        df = self.execute_strategy(df, instrument_count)
        return df

    def screen_bottom(self, df: pd.DataFrame, instrument_count: int = 10) -> pd.DataFrame:
        df = self.execute_strategy(df, instrument_count)
        return df
    
    