import pandas as pd

def transform_twitter_username(twitter_username):
    if not twitter_username is not None:
        return f'https://twitter.com/{twitter_username}'
    else:
        return ''

def transform_instagram_username(instagram_username):
    if not instagram_username is not None:
        return f'https://instagram.com/{instagram_username}'
    else:
        return ''


def split_contracts(df):
    df['address'] = df['contracts'].apply(lambda x: x[0]['address'])
    df['chain'] = df['contracts'].apply(lambda x: x[0]['chain'])

    return df

