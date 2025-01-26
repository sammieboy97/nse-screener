import pandas as pd

class NiftyDataLoader:
    def __init__(self, nifty500_path="data/ind_nifty500list.csv", nifty50_path="data/ind_nifty50list.csv"):
        self.nifty500_path = nifty500_path
        self.nifty50_path = nifty50_path

    def load_nifty500(self):
        return pd.read_csv(self.nifty500_path)

    def get_nifty500_symbols(self):
        bse_list = self.load_nifty500()
        return bse_list['Symbol']

    def load_nifty50(self):
        return pd.read_csv(self.nifty50_path)

    def get_nifty50_symbols(self):
        bse_list = self.load_nifty50()
        return bse_list['Symbol']