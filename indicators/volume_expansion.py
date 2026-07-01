def detect_volume_expansion(df):

    recent_volume = (
        df["volume"]
        .tail(5)
        .max()
    )

    average_volume = (
        df["volume"]
        .iloc[-25:-5]
        .mean()
    )

    volume_ratio = (
        recent_volume
        / average_volume
    )

    if volume_ratio < 1:
        status = "WEAK"
        score = 0
        passed = "No"

    elif volume_ratio < 1.2:
        status = "NORMAL"
        score = 50
        passed = "No"

    elif volume_ratio < 1.5:
        status = "STRONG"
        score = 80
        passed = "Yes"

    else:
        status = "EXPLOSIVE"
        score = 100
        passed = "Yes"

    return {

        "recent_volume": int(
            recent_volume
        ),

        "average_volume": round(
            average_volume,
            2
        ),

        "volume_ratio": round(
            volume_ratio,
            2
        ),

        "status": status,

        "score": score,

        "passed": passed
    }