
########################################################
#     FOR TRANSFORMATION FUNCTIONALITY ONLY             #
# here you should write functions, classes (whatever    #
# you prefer) to modify the data you get from the API.  #
# I will provide you with example transformations, you  #
# can work on them or decide to do some other (THEY     #
# SHOULD MAKE SENSE)                                    #
########################################################


def transform_twitter_username():
    """
    if the collection has a Twitter user_name, it is just the username, you can do something like:
    if username is ===> Raiser_Art
    transform it to be the whole url ===> https://twitter.com/Raiser_Art
    """
    pass


def transform_instagram_username():
    """
    should be same as get_full_twitter_url() but for instagram usernames
    """
    pass


def split_contracts():
    """
    every response contains field contracts that is a list and has address and chain in them.

    e.g
        "contracts": [
        {
            "address": "0x76a6d1020f584193bd7192c6a7e95ec9f80fab55",
            "chain": "ethereum"
        }
    ]

    you should implement this function so that it splits contracts and if you have a dataframe
    adds two new columns to the dataframe, address and chain
    """
    pass