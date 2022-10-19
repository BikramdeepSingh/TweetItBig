#############################################################
# [2022-10-17]: Created by Bikramdeep & Surya
#############################################################

# Importing libraries and modules
import pandas as pd
from data_fetch import fetch
from clean_data import clean
from model import vader_run
import time


print('\n###################### TweetItBig ######################\n')

print('\nStart Time: ', time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

# The keywords to scrape and analyze upon
searches = ["iphone", "iphone14", "iphone 14", "ios", "ios16", "ios 16", "apple"]
print("Scraping data for search terms: ", searches)

# Fetching data around the keywords
tweets_df = fetch(searches)

print('\nTime after data fetch: ', time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

# Cleaning rules for the tweet's text
tweets_df = clean(tweets_df)

print("Shape of data extracted today: ", tweets_df.shape)

# Extracting sentiment using Vader
print("\n\nRunning Vader...")

tweets_df = vader_run(tweets_df)

print('\nTime after modelling: ', time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

print("\nResultant sentiment counts: ")
print(tweets_df.Vader_sentiment.value_counts())

print('End Time: ', time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))