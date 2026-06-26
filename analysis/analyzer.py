from indicators.ema import calculate_ema
from indicators.returns import weekly_return
from indicators.returns import monthly_return
from indicators.volume import average_volume


def analyze(df):

    current_price = df["close"].iloc[-1]

    ema50 = calculate_ema(df, 50)
    ema200 = calculate_ema(df, 200)

    weekly = weekly_return(df)
    monthly = monthly_return(df)

    volume = average_volume(df)

    above_ema50 = current_price > ema50
    above_ema200 = current_price > ema200

    # qualified = (
    #     above_ema50
    #     and above_ema200
    #     and weekly > 0
    #     and monthly > 0
    # )

    reasons = []

    if not above_ema50:
        reasons.append("Below EMA50")

    if not above_ema200:
        reasons.append("Below EMA200")

    if weekly <= 0:
        reasons.append("Negative Weekly Momentum")

    if monthly <= 0:
        reasons.append("Negative Monthly Momentum")

    qualified = len(reasons) == 0

    return {
        "current_price": current_price,
        
        "ema50": ema50,
        "ema200": ema200,

        "above_ema50": above_ema50,
        "above_ema200": above_ema200,

        "weekly_return": weekly,
        "monthly_return": monthly,

        "avg_volume": volume,

        "reasons": reasons,
        
        "qualified": qualified
        
    }