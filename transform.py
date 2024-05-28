import pandas as pd

def transform_twitter_username(twitter_username: str) -> str:
    if twitter_username:
        return f'https://twitter.com/{twitter_username}'
    else:
        return None
    

def transform_instagram_username(instagram_username: str) -> str:
    if instagram_username:
        return f'https://instagram.com/{instagram_username}'
    else:
        return None


def split_contracts(df: pd.DataFrame) -> pd.DataFrame:
        df['address'] = df['contracts'].apply(lambda x: x[0]['address'] if x else None)
        df['chain'] = df['contracts'].apply(lambda x: x[0]['chain'] if x else None)
        return df

