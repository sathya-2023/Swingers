import pandas as pd

URL = "https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz"

df = pd.read_csv(URL, compression="gzip")
df = df[df["instrument_type"] == "EQUITY"]


def get_stock(symbol: str):
    result = df[df["tradingsymbol"] == symbol.upper()]

    if result.empty:
        return None

    return result.iloc[0]


def get_key(symbol: str):
    stock = get_stock(symbol)

    if stock is None:
        return None

    return stock["instrument_key"]


if __name__ == "__main__":
    print(get_stock("HCLTECH"))
    print(get_key("HCLTECH"))