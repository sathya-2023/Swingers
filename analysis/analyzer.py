from indicators.ema import calculate_ema
from indicators.returns import weekly_return
from indicators.returns import monthly_return
from indicators.volume import average_volume
from ranking.scorer import score
from ranking.relative_strength import calculate_relative_strength
from indicators.fifty_two_week import (fifty_two_week_high, distance_from_52w_high)


def analyze(df):

    current_price = df["close"].iloc[-1]

    ema50 = calculate_ema(df, 50)
    ema200 = calculate_ema(df, 200)

    weekly = weekly_return(df)
    monthly = monthly_return(df)

    volume = average_volume(df)
    
    high_52w = fifty_two_week_high(df)
    distance_52w = distance_from_52w_high(df)

    above_ema50 = current_price > ema50
    above_ema200 = current_price > ema200

    # qualified = (
    #     above_ema50
    #     and above_ema200
    #     and weekly > 0
    #     and monthly > 0
    # )

    # reasons = []
    strengths = []
    weaknesses = []

    if above_ema50:
        strengths.append("Above EMA50")
    else:
        weaknesses.append("Below EMA50")
        
    if above_ema200:
        strengths.append("Above EMA200")
    else:
        weaknesses.append("Below EMA200")

    if distance_52w >= -10:
        strengths.append("Close to 52W High")
    else:
        weaknesses.append("Far from 52W High")

    if weekly > 0:
        strengths.append("Positive Weekly Momentum")
    else:
        weaknesses.append("Negative Weekly Momentum")
        
    if monthly > 0:
        strengths.append("Positive Monthly Momentum")
    else:
        weaknesses.append("Negative Monthly Momentum")

    qualified = len(weaknesses) == 0
    
    ranking_score = score({
        "above_ema50": above_ema50,
        "above_ema200": above_ema200,
        "weekly_return": weekly,
        "monthly_return": monthly
    })

    relative_strength = calculate_relative_strength({
        "weekly_return": weekly,
        "monthly_return": monthly
    })

    return {
        "current_price": current_price,
        
        "ema50": ema50,
        "ema200": ema200,

        "above_ema50": above_ema50,
        "above_ema200": above_ema200,

        "weekly_return": weekly,
        "monthly_return": monthly,

        "avg_volume": volume,

        # "reasons": reasons,
        "high_52w": high_52w,
        "distance_52w": distance_52w,
        
        "qualified": qualified,
        
        "strengths": strengths,
        "weaknesses": weaknesses,
        "qualified": qualified,
        "score": ranking_score,
        "relative_strength": relative_strength

    }