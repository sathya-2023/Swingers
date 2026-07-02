def create_trade_plan(
        support,
        resistance,
        target_pct=5,
        entry_buffer=0.2):

    entry = (
        resistance *
        (1 + entry_buffer/100)
    )

    stop = support

    target = (
        entry *
        (1 + target_pct/100)
    )

    risk_pct = (
        (
            entry - stop
        )
        / entry
    ) * 100

    reward_pct = (
        (
            target - entry
        )
        / entry
    ) * 100

    rr = (
        reward_pct
        / risk_pct
    )

    return {

        "entry": round(
            entry,
            2
        ),

        "stop": round(
            stop,
            2
        ),

        "target": round(
            target,
            2
        ),

        "risk_pct": round(
            risk_pct,
            2
        ),

        "reward_pct": round(
            reward_pct,
            2
        ),

        "rr": round(
            rr,
            2
        )
    }