#############################################################
# [2022-10-17]: Created by Surya & Mobassir
#############################################################

# Importing libraries and modules
import pandas as pd
import tweepy as tw
from datetime import datetime, timedelta

import sys, os
file_path = os.path.abspath(__file__)
repo_path = file_path[:file_path.find('TweetItBig\\') + len('TweetItBig\\')]
sys.path.append(repo_path)

from config import my_api_key1, my_api_secret1 


def tdf(tweets, tweets_df, search):
    '''
    This function traverse the json response files returned by the API calls and convert them to pandas dataframe for analysis 
    '''
    for tweet in tweets:
        tweets_df = pd.concat(
            [tweets_df, pd.DataFrame({
                'user_name': [tweet.user.name], 
                'user_location': [tweet.user.location],
                'user_description': [tweet.user.description],
                'user_verified': [tweet.user.verified],
                'followers_cnt': [tweet.user.followers_count],
                'account_date': [tweet.user.created_at.strftime("%Y-%m-%d")],
                'result_type': [tweet.metadata['result_type']],
                'favourites_cnt': [tweet.user.favourites_count],
                'date': [str(tweet.created_at.strftime("%Y-%m-%d"))],
                'datetime': [tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")],
                'text': [tweet.full_text], 
                'hashtags': str([i['text'] for i in tweet.entities["hashtags"] if i]),
                'source': [tweet.source],
                'favourite_cnt': [tweet.favorite_count],
                'retweet_cnt': [tweet.retweet_count],
                'reply_uid': [tweet.in_reply_to_user_id],
                'reply_sm': [tweet.in_reply_to_status_id],
                'search_term': [search]
            })], ignore_index=True)

    return tweets_df

def fetch(searches=[]):
    '''
    This function helps in fetching 20k+ tweets since last week (7 days) using a combination of same API calls with different parameters
    '''
    tweets_df = pd.DataFrame()
    # authenticate using the api keys
    auth = tw.OAuthHandler(my_api_key1, my_api_secret1)
    api = tw.API(auth, wait_on_rate_limit=True)
    for search in searches:
        search_query = search +" -filter:retweets"
   
        tweets = tw.Cursor(api.search_tweets, 
                          q=search_query,
                          lang="en",
                         tweet_mode='extended'
                         ).items(4000)

        tweets_df = tdf(tweets, tweets_df, search)
        
        tweets = api.search_tweets(q=search_query,
                                    lang="en", 
                                    count = 100,
                                    result_type="popular",
                                    tweet_mode='extended')

        tweets_df = tdf(tweets, tweets_df, search)

        tweets = api.search_tweets( q=search_query,
                                    lang="en", 
                                    until=(datetime.today() - timedelta(days=7)).strftime("%Y-%m-%d"),
                                    count = 100,
                                    result_type="recent",
                                    tweet_mode='extended')

        tweets_df = tdf(tweets, tweets_df, search)

        id1 = max([i.id for i in tweets])

        for d in range(6,0,-1):
            tweets = api.search_tweets(
                                    q=search_query,
                                    lang="en",
                                    until=(datetime.today() - timedelta(days=d)).strftime("%Y-%m-%d"),
                                    count = 100,
                                    tweet_mode='extended',
                                    result_type="recent",
                                    since_id = id1
                                    )
            if len(tweets)>0:
                id1 = max([i.id for i in tweets])

                tweets_df = tdf(tweets, tweets_df, search)
                
        tweets_df.drop_duplicates(inplace=True, ignore_index=True)
        
    #print(f"\nFor search term : {search}")
    print(f"Data Extracted from {min(tweets_df.datetime)} to {max(tweets_df.datetime)}")
    #print(f"Latest length of dataset: {len(tweets_df)}")
    
    # We need to drop any duplicate tweets fetched (if any) due to overlapping API calls
    print("Tweets before deletion\t:",tweets_df.shape)
    tweets_df.sort_values(by=['datetime'], ascending=False)
    tweets_df.drop_duplicates(subset=['text'], ignore_index=True, inplace=True)
    print("Tweets after deletion\t:",tweets_df.shape)

    # Uncomment below line in case we need to store the raw data
    #tweets_df.to_excel(f'{config.data_dir}{"_".join(searches)}_{datetime.now().strftime("%d-%m-%y")}.xlsx', index=False)
    
    return tweets_df
