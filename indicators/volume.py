def average_volume(df):

    return df["volume"].tail(20).mean()