#############################################################
# [2022-10-17]: Created by Surya & Bikramdeep
#############################################################

# Importing libraries and modules
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import sys, os
file_path = os.path.abspath(__file__)
repo_path = file_path[:file_path.find('TweetItBig\\') + len('TweetItBig\\')]
sys.path.append(repo_path)

import config


def vader_run(df):
    '''
    NLTK's Vader model is selected to detect sentiment of tweets as it has been trained on twitter data as well which gives it an edge to interpret informal english slangs, emojis and punctuation.
    '''

    # Extracting the Vader's compound sentiment score which ranges from -1 to +1
    df["Vader_score"] = [SentimentIntensityAnalyzer().polarity_scores(i)['compound'] for i in df["cleaned_text"]]

    # setting boundary between Negative, Neutral and Positive at 0
    cutoff = 0
    df["Vader_sentiment"] = ''
    df.loc[df.Vader_score > cutoff, 'Vader_sentiment'] = 'Positive'
    df.loc[df.Vader_score.abs() <= cutoff, 'Vader_sentiment'] = 'Neutral'
    df.loc[df.Vader_score < -cutoff, 'Vader_sentiment'] = 'Negative'
    
    print("\nResultant sentiment counts: ")
    print(df.Vader_sentiment.value_counts())

    # Fetching old output file and appending the current results
    old = pd.read_excel(config.data_dir+'Final_output.xlsx')
    old.date = old.date.astype(str)
    
    full_df = pd.concat([old, df], ignore_index=True)

    print("Full data shape before insertion\t\t: ",full_df.shape)
    full_df.sort_values(by=['datetime'], ascending=False)
    full_df.drop_duplicates(subset=['text'], ignore_index=True, inplace=True)
    print("Full data shape after insertion (after duplicated deletion)\t: ",full_df.shape)

    full_df.to_excel(config.data_dir+'Final_output.xlsx', index=False)

    print("Output file updated and saved.")
    
    return df
