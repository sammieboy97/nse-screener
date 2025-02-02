import yfinance as yf
import pandas as pd

clean_data_path = "data/ind_nifty50list.csv"
symbol_list_df = pd.read_csv(clean_data_path)

def store_prices():
    start_date = '2020-01-01'
    end_date = '2025-01-31'

    # Download historical data
    prices = pd.DataFrame()
    for symbol in symbol_list_df["Symbol"]:
        df = yf.download(symbol + ".NS", start=start_date, end=end_date, progress=False)
        print("Downloaded", symbol)
        prices[symbol] = df['Close']

    prices.to_csv("data/nifty50_prices2020.csv")

    print(prices)

# store_prices()

def backtest():
    prices = pd.read_csv("data/nifty50_prices2020.csv", index_col=0)
    prices.index = pd.to_datetime(prices.index)
    prices.dropna(axis=1, how='all', inplace=True)

    prices = prices.resample('M').last()

    momentum = (prices.shift(1) / prices.shift(13)) - 1

    # momentum = momentum.dropna(how='all')

    selected_stocks = momentum.apply(lambda x: x.nlargest(10).index.tolist(), axis=1)
    # prices.loc['2024-07-31', 'TRENT'] / prices.loc['2024-06-30', 'TRENT'] to get momentum of each stock
    portfolio_returns = pd.Series(index=prices.index, dtype=float)

    for i in range(len(selected_stocks)):
        if i < 12:
            continue
        if i + 1 >= len(prices):
            break
        current_date = selected_stocks.index[i]
        next_date = prices.index[i + 1]
        stocks = selected_stocks.iloc[i]
        if len(stocks) > 0:
            current_prices = prices.loc[current_date, stocks]
            next_prices = prices.loc[next_date, stocks]

            # Calculate returns for each stock: (next_price / current_price) - 1
            stock_returns = (next_prices / current_prices) - 1

            # Average the returns across all selected stocks
            avg_return = stock_returns.mean()
            # Store the average return
            portfolio_returns.loc[next_date] = avg_return
            print(stocks)

    portfolio_returns.dropna(inplace=True)

    print(portfolio_returns)
    print(selected_stocks)

    cumulative_growth = (1 + portfolio_returns).cumprod()

    # Calculate final value of the investment
    initial_investment = 1000
    final_value = initial_investment * cumulative_growth.iloc[-1]

    # Calculate total returns
    total_returns = final_value - initial_investment

    print("Final Value of Investment:", final_value)
    print("Total Returns:", total_returns)

    # Calculate number of years
    start_date = portfolio_returns.index[0]
    end_date = portfolio_returns.index[-1]
    n_years = (end_date - start_date).days / 365.25  # Account for leap years

    # Calculate CAGR
    cagr = (final_value / initial_investment) ** (1 / n_years) - 1

    print("CAGR (%):", cagr * 100)


backtest()