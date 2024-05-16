#######################################################
#               FOR LOADING ONLY                       #
# usually it is better to have different functionality #
# for loading data to different sources but lets keep  #
# it simple for now. this file should load raw data to #
# csv files and transformed data to PostgreSQL table   #
#######################################################

def load_raw_to_json():
    """
    load the raw data (data that you get directly from the API) no transformations,
    data should stay exactly as it was. (that's the point of having raw data)

    load into .json files and the name of each file should be specific
    e.g
    {chain}-{current_page_next_token}.json ====> ethereum-LXBrPTMyMjEyNDY5.json

    raw data should be written in raw_data directory

    my advice: if you keep the data as a DataFrame, you can easily write it to
    json
    """


def load_data_to_database():
    """
    after the transformation is done on the data, load it do postgreSQL, do not use
    SQLAlchemy or sqlite3. use psychopg2 as a PostgreSQL connector
    """