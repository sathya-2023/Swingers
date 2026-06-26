from datetime import datetime, timedelta

import pandas as pd
import upstox_client
from upstox_client.rest import ApiException

from config import UPSTOX_ACCESS_TOKEN
from core.instrument_service import get_key

configuration = upstox_client.Configuration()
configuration.access_token = UPSTOX_ACCESS_TOKEN

client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryV3Api(client)


def get_daily_history(symbol: str):

    stock = get_key(symbol)

    if stock is None:
        raise Exception(f"{symbol} not found")

    instrument_key = get_key(symbol)

    to_date = datetime.today().strftime("%Y-%m-%d")
    from_date = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

    try:

        response = history_api.get_historical_candle_data1(
            instrument_key=instrument_key,
            unit="days",
            interval="1",
            to_date=to_date,
            from_date=from_date,
        )

        # return response
        candles = response.data.candles

        df = pd.DataFrame(
            candles, columns=[
                "date",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "oi"]
        )
        
        # Upstox returns newest first.
        # We want oldest first.

        df = df.iloc[::-1].reset_index(drop=True)

        # Convert date column

        df["date"] = pd.to_datetime(df["date"])

        return df

    except ApiException as e:
        print(e)
        return None


if __name__ == "__main__":

    data = get_daily_history("HCLTECH")

    print(data)
