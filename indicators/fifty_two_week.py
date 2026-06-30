def fifty_two_week_high(df):

    return df["high"].max()


def distance_from_52w_high(df):

    current = df["close"].iloc[-1]

    high_52w = fifty_two_week_high(df)

    distance = (
        (current - high_52w)
        / high_52w
    ) * 100

    return distance