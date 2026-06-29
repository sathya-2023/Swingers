from core.history_service import get_daily_history
from analysis.analyzer import analyze


def scan(stocks):

    results = []

    for stock in stocks:

        print(f"Analyzing {stock}...")

        try:

            history = get_daily_history(stock)

            result = analyze(history)

            result["symbol"] = stock

            results.append(result)

        except Exception as e:

            print(f"Error: {stock} -> {e}")

    return results