from nsepython import *
import pandas as pd

def loadNifty500():
    return pd.read_csv("data/ind_nifty500list.csv")

def getNifty500Symbols():
    bseList = loadNifty500()
    return bseList['Symbol']

def loadNifty50():
    return pd.read_csv("data/ind_nifty50list.csv")

def getNifty50Symbols():
    bseList = loadNifty50()
    return bseList['Symbol']

def createFilteredData():
    symbols = getNifty50Symbols()

    series = "EQ"
    start_date = "25-01-2024"
    end_date ="26-01-2025"

    filtered_dfs = []
    for symbol in symbols:
        df = equity_history(symbol, series, start_date, end_date)

        # Adjust the column names based on the actual DataFrame structure
        if 'CH_CLOSING_PRICE' in df.columns and 'CH_SYMBOL' in df.columns:
            df = df[['CH_CLOSING_PRICE', 'CH_SYMBOL', 'CH_TIMESTAMP']]

            # Calculate the percentage difference between consecutive rows
            df['Percentage_Diff'] = df['CH_CLOSING_PRICE'].pct_change() * 100

            # Check if the difference is greater than 30%
            df['Greater_Than_30'] = df['Percentage_Diff'].abs() > 30

            # If no row has a difference greater than 30%, add the DataFrame to the filtered list. just of handling Corporate actions like Split, Bonus etc.
            if not df['Greater_Than_30'].any():
                print(f"Symbol {symbol} has no percentage difference greater than 30%. So adding into the clean data")
                filtered_dfs.append(df)

        else:
            print(f"Required columns not found for symbol {symbol}")

    filtered_df = pd.concat(filtered_dfs)

    print(filtered_df)
    # filtered_df.to_csv("filtered_nifty50.csv", index=False)


# read filtered_nifty50.csv
def readFilteredData():
    return pd.read_csv("filtered_nifty50.csv")

def getTop10SymbolsForPeriod(period):
    df = readFilteredData()

    df = df.iloc[::-1]

    # Group the data by Symbol and calculate the percentage difference between the last and last-period rows for each symbols
    df = df.groupby('CH_SYMBOL').apply(lambda x: x['CH_CLOSING_PRICE'].pct_change(periods=period) * 100)

    # Form df with the value calculated of the last value of each group (Symbol)
    df = df.groupby('CH_SYMBOL').last()

    # Sort the data by the percentage difference Descending order
    df = df.sort_values(ascending=False)

    print(df.head(10))



def main():
    # createFilteredData()
    getTop10SymbolsForPeriod(100)


if __name__ == "__main__":
    main()