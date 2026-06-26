import pandas as pd

URL = "https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz"

df = pd.read_csv(URL, compression="gzip")
df = df[df["instrument_type"] == "EQUITY"]


def get_instrument(symbol: str):
    result = df[df["tradingsymbol"] == symbol.upper()]

    if result.empty:
        return None

    return result.iloc[0]


if __name__ == "__main__":

    stock = get_instrument("INFY")

    print(stock)