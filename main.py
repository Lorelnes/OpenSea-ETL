from constants import url, params, headers
from extract import make_api_call
from transform import transform_instagram_username, transform_twitter_username, split_contracts
from load import load_raw_to_json, load_data_to_database

"""
GENERAL COMMENT (APPLIES NOT ONLY TO THIS .py FILE): all in all this is too simple for your level.
ETLs are much more complex simply having couple of extract transform load functions will not do.

there are some fundamental things I would like for you to take a look at and be more cautious next time

- commit your code as you go, you need to understand how git works (git vs github (they are different))
helps you recover in case anything happens, easy to see code development, easier to manage, maintain

- use OOP (functional programming is great but at a scale its challenging to manage),
for example you could have DatabaseConnector, Transform, Extract, Load classes.
Define and structure your code well, create files/folders logically

- understand how functions work (what is return type and side effect),
how parameters are passed to functions (!!!!!!!variables defined inside a function are not global!!!!!)

- instead of printing everything use logger to log relative information

- use proper error handling, try...except Exception is mostly too general, proper error handling can boost your code in many ways

- you have problems with indentation, in python indent (4 spaces) is essential for the interpreter to understand what block of code goes were
try and undertand how it works

####### this will work #######
def func():
    print("hello world")

####### this will not work #######
def func():
  print("hello world")

- working with database in this case PostgreSQL, take a look what realtional databases are how they work,
difference between database, table. how to write queries. define table schemas in advance
"""


# Extraction
df, next_token = make_api_call(url=url, headers=headers, params=params)
for i in range(5): #TODO: 5 was used for testing, why are you extracting only 5 pages worth of data

    params['next'] = next_token
    df, next_token = make_api_call(url=url, headers=headers, params=params)
    filename = load_raw_to_json(df, "ethereum", next_token) # TODO: load_raw_to_json does not return anything, why assign it to filename


    # Transformation
    df['twitter_username'] = df['twitter_username'].apply(transform_twitter_username)
    df['instagram_username'] = df['instagram_username'].apply(transform_instagram_username)
    df = split_contracts(df)

    # Loading
    load_raw_to_json(df, "ethereum", next_token) #TODO: calling load_raw_to_json twice, will you create same file twice?

    # TODO: these fields can be moved to constants as well
    # moved some fields to constants
    transformed_df_selected = transformed_df[selected_columns]

    load_data_to_database(transformed_df_selected)




