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
    full_df.drop_duplicates(subset=['cleaned_text'], ignore_index=True, inplace=True)
    print("Full data shape after insertion (after duplicated deletion)\t: ", full_df.shape)

    try:
        full_df.to_excel(config.data_dir+'Final_output.xlsx', index=False)
    except:
        ### Ref: http://www.havnemark.dk/?p=185
        def escape_xlsx_char(ch):
            illegal_xlsx_chars = {
            '\x00':'\\x00',	#	NULL
            '\x01':'\\x01',	#	SOH
            '\x02':'\\x02',	#	STX
            '\x03':'\\x03',	#	ETX
            '\x04':'\\x04',	#	EOT
            '\x05':'\\x05',	#	ENQ
            '\x06':'\\x06',	#	ACK
            '\x07':'\\x07',	#	BELL
            '\x08':'\\x08',	#	BS
            '\x0b':'\\x0b',	#	VT
            '\x0c':'\\x0c',	#	FF
            '\x0e':'\\x0e',	#	SO
            '\x0f':'\\x0f',	#	SI
            '\x10':'\\x10',	#	DLE
            '\x11':'\\x11',	#	DC1
            '\x12':'\\x12',	#	DC2
            '\x13':'\\x13',	#	DC3
            '\x14':'\\x14',	#	DC4
            '\x15':'\\x15',	#	NAK
            '\x16':'\\x16',	#	SYN
            '\x17':'\\x17',	#	ETB
            '\x18':'\\x18',	#	CAN
            '\x19':'\\x19',	#	EM
            '\x1a':'\\x1a',	#	SUB
            '\x1b':'\\x1b',	#	ESC
            '\x1c':'\\x1c',	#	FS
            '\x1d':'\\x1d',	#	GS
            '\x1e':'\\x1e',	#	RS
            '\x1f':'\\x1f'}	#	US
            
            if ch in illegal_xlsx_chars:
                return illegal_xlsx_chars[ch]
            
            return ch
            
        # Wraps the function escape_xlsx_char(ch).
        def escape_xlsx_string(st):
            
            return ''.join([escape_xlsx_char(ch) for ch in st])
        
        # full_df.text = full_df.text.apply(lambda x: escape_xlsx_string(x))
        full_df.cleaned_text = full_df.cleaned_text.apply(lambda x: escape_xlsx_string(x))

    print("Output file updated and saved.")
    
    return df