#############################################
# THIS IS THE ENTRY POINT OF THE PROGRAM      #
# program should start executing from main.py #
# I will give you a blueprint of how the flow #
# should look like                            #
#############################################

"""
every (most of them) functionality you defined in extract.py transform.py load.py should happen here,
you import them and create a flow in the main.py

for example (THIS IS AN EXAMPLE DO NOT TRY TO DO IT EXACTLY SAME)
data = make_api_call()

load_raw_to_json(data, file_name)

data = transform_twitter_username(data)
data = transform_instagram_username(data)
data = split_contracts(data)

load_data_to_database(data)

WARNING:
    flow that I have created and the functions defined will not work, they are just a blueprint
    to guide, help you understand the way ETL pipelines are created, while working on this you are welcome (you should)
    add your own functions, modify mine, to make the pipeline work.

ANOTHER WARNING:
    DO NOT FORGET API PAGINATION (there is more then 100 collections, 100 is for just one page)

ANOTHER WARNING:
    I WILL KNOW IF THE CODE WAS WRITTEN BY  CHATGPT

P.S
    please, commit your code to github as you work so I can the the progress for different stages
"""