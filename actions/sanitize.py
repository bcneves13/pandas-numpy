def sanitize(df, col):
    df[col] = df[col].astype(float)
    return df