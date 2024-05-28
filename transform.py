import pandas as pd

"""
GENERAL COMMENT (APPLIES NOT ONLY TO THIS .py FILE)
this transformation functionality is too simple for a data engineering intern, however lets keep it like that for now

aside functionality you can make your code more readable, try to add comments, doc strings, type annotations

I will modify your functions as an example
"""


def transform_twitter_username(twitter_username: str) -> str:
    #TODO: lets evaluate what you are checking here. if twitter_username is empty not twitter_username => True
    # True not None?????????
    if twitter_username:
        return f'https://twitter.com/{twitter_username}'
    else:
        return ''
    

def transform_instagram_username(instagram_username: str) -> str:
    if instagram_username:
        return f'https://instagram.com/{instagram_username}'
    else:
        return ''


def split_contracts(df: pd.DataFrame) -> pd.DataFrame:
    if not df['contracts'].empty:
        df['address'] = df['contracts'].apply(lambda x: x[0]['address'])
        df['chain'] = df['contracts'].apply(lambda x: x[0]['chain'])
    else:
        df['address'] = None
        df['chain'] = None

    return df

