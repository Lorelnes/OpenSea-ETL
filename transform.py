import pandas as pd

########################################################
#     FOR TRANSFORMATION FUNCTIONALITY ONLY             #
# here you should write functions, classes (whatever    #
# you prefer) to modify the data you get from the API.  #
# I will provide you with example transformations, you  #
# can work on them or decide to do some other (THEY     #
# SHOULD MAKE SENSE)                                    #
########################################################

from extract import response

def transform_twitter_username(twitter_username):
    return f'https://twitter.com/{twitter_username}'

response['twitter_url'] = response['twitter_username'].apply(transform_twitter_username)

def transform_instagram_username(instagram_username):
    return f'https://instagram.com/{instagram_username}'

response['instagram_url'] = response['instagram_username'].apply(transform_instagram_username)

def split_contracts(response):
    response['address'] = response['contracts'].apply(lambda x: x[0]['address'])
    response['chain'] = response['contracts'].apply(lambda x: x[0]['chain'])

    response.drop('contracts', axis=1, inplace=True)
    return response

df1 = split_contracts(response)

print(df1.address)


# #Checking if there are duplicate rows and removing them if present
duplicate_rows = response.duplicated()
num_duplicates = duplicate_rows.sum()
print('Number of duplicate rows:', num_duplicates)


#Checking if there are NaN values and filling them if present
nan_values = response.isnull().sum()
print('Number of NaN values:', nan_values)


