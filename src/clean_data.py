#############################################################
# [2022-10-17]: Created by Tanishq & Gurvinder
#############################################################

# Importing libraries and modules
import pandas as pd
from cleantext import clean as cln #Cleantext is an excellent one-in-all text data cleaning library which works faster than traditional regex rules


def clean(df):
    '''
     To clean out URLs only, 
     avoiding cleaning out emojis, punctuations, bad words
    in order to help Vader better judge the sentiment behind the tweet
    '''
    
    df['cleaned_text'] = df.text.apply(lambda x: cln(x, no_urls=True))
    return df