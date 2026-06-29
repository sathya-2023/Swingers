# from config import (
#     UPSTOX_API_KEY,
#     UPSTOX_API_SECRET,
#     UPSTOX_REDIRECT_URI,
#     UPSTOX_ACCESS_TOKEN,
# )

# print("=" * 50)
# print("Swingers")
# print("=" * 50)

# print(f"API Key Loaded          : {'Yes' if UPSTOX_API_KEY else 'No'}")
# print(f"API Secret Loaded       : {'Yes' if UPSTOX_API_SECRET else 'No'}")
# print(f"Redirect URI Loaded     : {'Yes' if UPSTOX_REDIRECT_URI else 'No'}")
# print(f"Access Token Loaded     : {'Yes' if UPSTOX_ACCESS_TOKEN else 'No'}")

# =================================================

# # from config import UPSTOX_ACCESS_TOKEN

# # print(UPSTOX_ACCESS_TOKEN[:20])

# ===========================================
# from core.history_service import get_daily_history

# history = get_daily_history("HCLTECH")

# print(type(history))
# print(history)

# --------------------------------------
# print(type(history))
# print()

# print("Number of candles:")
# print(len(history.data.candles))
# print()

# print("Latest candle:")
# print(history.data.candles[0])
# print()

# print("Oldest candle:")
# print(history.data.candles[-1])

# ___________Sprint 4_____________________

# from core.history_service import get_daily_history

# from indicators.ema import calculate_ema
# from indicators.returns import weekly_return
# from indicators.returns import monthly_return
# from indicators.volume import average_volume

# history = get_daily_history("HCLTECH")

# current_price = history["close"].iloc[-1]

# ema50 = calculate_ema(history, 50)
# ema200 = calculate_ema(history, 200)

# weekly = weekly_return(history)
# monthly = monthly_return(history)

# volume = average_volume(history)

# print("=" * 40)
# print("HCLTECH")
# print("=" * 40)

# print()

# print(f"Current Price : {current_price:.2f}")

# print()

# print(f"EMA50         : {ema50:.2f}")
# print(f"EMA200        : {ema200:.2f}")

# print()

# print(f"Above EMA50   : {current_price > ema50}")
# print(f"Above EMA200  : {current_price > ema200}")

# print()

# print(f"Weekly Return : {weekly:.2f}%")
# print(f"Monthly Return: {monthly:.2f}%")

# print()

# print(f"Avg Volume    : {volume:,.0f}")


# ------------------Sprint 5----------------------
# from core.history_service import get_daily_history
# from analysis.analyzer import analyze

# history = get_daily_history("PIXTRANS")

# result = analyze(history)

# print()

# for key, value in result.items():
#     print(f"{key}: {value}")
    
# ---------------Sprint 6----------------------
from core.universe_service import load_universe
from scanner.scanner_v1 import scan

stocks = load_universe("nifty50")

results = scan(stocks)

for stock in results:

    print()
    print("=" * 40)
    print(stock["symbol"])
    print(
            "PASS"
            if stock["qualified"]
            else "FAIL"
        )
    
    print()
    print("Score:", stock["score"])
    
    print()
    print("Strengths:")
    print(stock["strengths"])
    
    print()
    print("Weaknesses:")
    print(stock["weaknesses"])
    print()

# -------------------adding universes-----------------------
# from core.universe_service import load_universe

# stocks = load_universe("nifty50")

# print(stocks)
# print()
# print(f"Total stocks: {len(stocks)}")