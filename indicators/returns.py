def weekly_return(df):

    current = df["close"].iloc[-1]
    previous = df["close"].iloc[-6]

    return ((current - previous) / previous) * 100


def monthly_return(df):

    current = df["close"].iloc[-1]
    previous = df["close"].iloc[-22]

    return ((current - previous) / previous) * 100