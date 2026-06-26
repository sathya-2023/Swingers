from datetime import datetime, timedelta

import upstox_client
from upstox_client.rest import ApiException

from config import UPSTOX_ACCESS_TOKEN
from data.instrument_loader import get_instrument

configuration = upstox_client.Configuration()
configuration.access_token = UPSTOX_ACCESS_TOKEN

client = upstox_client.ApiClient(configuration)

history_api = upstox_client.HistoryV3Api(client)


def get_history(symbol: str):

    stock = get_instrument(symbol)

    if stock is None:
        raise Exception(f"{symbol} not found")

    instrument_key = stock["instrument_key"]

    to_date = datetime.today().strftime("%Y-%m-%d")
    from_date = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

    try:

        response = history_api.get_historical_candle_data1(
            instrument_key=instrument_key,
            unit="days",
            interval="1",
            to_date=to_date,
            from_date=from_date
        )

        return response

    except ApiException as e:
        print(e)
        return None


if __name__ == "__main__":

    data = get_history("HCLTECH")

    print(data)