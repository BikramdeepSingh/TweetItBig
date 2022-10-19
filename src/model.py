#############################################################
# [2022-10-17]: Created by Surya & Bikramdeep
#############################################################

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
    df["Vader_score"] = [SentimentIntensityAnalyzer().polarity_scores(i)['compound'] for i in df["text"]]

    cutoff = 0
    df["Vader_sentiment"] = ''
    df.loc[df.Vader_score > cutoff, 'Vader_sentiment'] = 'Positive'
    df.loc[df.Vader_score.abs() <= cutoff, 'Vader_sentiment'] = 'Neutral'
    df.loc[df.Vader_score < -cutoff, 'Vader_sentiment'] = 'Negative'

    old = pd.read_excel(config.data_dir+'Final_output.xlsx')
    old.date = old.date.astype(str)
    
    full_df = pd.concat([old, df], ignore_index=True)

    print("Full data shape with duplicates\t: ",full_df.shape)
    full_df.sort_values(by=['datetime'], ascending=False)
    full_df.drop_duplicates(subset=['text'], ignore_index=True, inplace=True)
    print("Full data shape without duplicates\t: ",full_df.shape)

    full_df.to_excel(config.data_dir+'Final_output.xlsx', index=False)

    return df
