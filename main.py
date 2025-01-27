from NiftyDataLoader import NiftyDataLoader
from data_processor import DataProcessor
from strategy.momentum_strategy import MomentumStrategy
import pandas as pd

def main():
    loader = NiftyDataLoader(csv_path="data/ind_nifty500list.csv")
    clean_data_path = "data/filtered_nifty500.csv"
    # The below line is commented as the clean data for nifty500list.csv is created. If need a new one, uncomment and get the data
    # loader.create_clean_data(clean_data_path)

    periods = [25, 50]
    strategy = MomentumStrategy(periods=periods)
    processor = DataProcessor(loader=loader, strategy=strategy, clean_data_path=clean_data_path)

    # Just to screen, uncomment the below line
    # top_stocks = processor.screen_top(10, snapshot__back_in_days=1)
    # print(top_stocks)

    snapshot__back_in_days = 1
    profitTrade = 0
    lossTrade = 0
    noTrade = 0
    totalDifferencePercentageSum = 0a
    totalCapitalNeeded = 0
    while snapshot__back_in_days > 0:
        top_stocks = processor.screen_top(10, snapshot__back_in_days)
        df = loader.read_clean_data(clean_data_path)
        totalDifferencePercentage, capitalNeeded = strategy.execute_trade(df, top_stocks, snapshot__back_in_days-1, snapshot__back_in_days-24)
        if totalDifferencePercentage > 0:
            profitTrade += 1
        elif totalDifferencePercentage == 0:
            noTrade += 1
        else:
            lossTrade += 1
        # Accumulate the total difference percentage and capital needed
        totalDifferencePercentageSum += totalDifferencePercentage * capitalNeeded
        totalCapitalNeeded += capitalNeeded
        # Print the snapshot__back_in_days and the totalDifferencePercentage
        print(f"Snapshot Back in Days: {snapshot__back_in_days}, Total Difference Percentage: {totalDifferencePercentage}")
        snapshot__back_in_days -= 25

    # Calculate the overall percentage profit or loss
    overallPercentage = (totalDifferencePercentageSum / totalCapitalNeeded) if totalCapitalNeeded != 0 else 0
    print(f"Profit Trade: {profitTrade}, Loss Trade: {lossTrade}, No Trade: {noTrade}")
    print(f"Overall Percentage Profit or Loss: {overallPercentage}")


if __name__ == "__main__":
    main()