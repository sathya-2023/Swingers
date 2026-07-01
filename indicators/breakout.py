def detect_breakout(
        current_price,
        resistance_price):

    breakout_distance = (
        (
            current_price
            - resistance_price
        )
        / resistance_price
    ) * 100

    if breakout_distance < -3:
        status = "FAR"
        score = 0
        passed = False

    elif breakout_distance < -1:
        status = "APPROACHING"
        score = 0
        passed = False

    elif breakout_distance < 0:
        status = "READY"

        if breakout_distance >= -0.5:
            score = 90
        else:
            score = 80

        passed = True

    elif breakout_distance <= 2:
        status = "BREAKOUT"

        if breakout_distance <= 0.5:
            score = 100

        elif breakout_distance <= 1:
            score = 95

        else:
            score = 85

        passed = True

    else:
        status = "EXTENDED"
        score = 0
        passed = False

    return {
        "resistance_price": resistance_price,
        "current_price": current_price,
        "distance": round(
            breakout_distance,
            2
        ),
        "status": status,
        "score": score,
        "passed": passed
    }