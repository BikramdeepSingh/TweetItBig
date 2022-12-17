'''
    Code contributed by Bikramdeep Singh
    Time stamp: 11-Dec-2022 11:16 PM
'''
import sys, os
file_path = os.path.abspath(__file__)
repo_path = file_path[:file_path.find('TweetItBig\\') + len('TweetItBig\\')]
sys.path.append(repo_path)
print("abc",repo_path)
import config 

from dash import Dash
from dash import html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
import tweepy
from textblob import TextBlob
import re
import emoji
import navigation



# function to clearn tweets from emojis and links and line breaks and more
def clean_tweets(txt):
	txt = re.sub(r"RT[\s]+", "", txt)
	txt = txt.replace("\n", " ")
	txt = re.sub(" +", " ", txt)
	txt = re.sub(r"https?:\/\/\S+", "", txt)
	txt = re.sub(r"(@[A-Za-z0–9_]+)|[^\w\s]|#", "", txt)
	txt = emoji.replace_emoji(txt, replace='')
	txt.strip()
	return txt


# Set authentication and access token
authenticate = tweepy.OAuthHandler(config.my_api_key2, config.my_api_secret2)
# #authenticate.set_access_token(accessToken, accessTokenSecret)

# Create Twitter API using authentication information
api = tweepy.API(authenticate, wait_on_rate_limit=True)

# sentiment_analysis_layout = dbc.Container([
# 	navigation.navbar,
#     html.Br(),
# 	html.H4("Search Term:", style={'textAlign': 'center'}),
# 	html.Center(
# 		user_search := dcc.Input(type='text', 
# 							 debounce=True, 
# 							 placeholder="Type search term for tweets", 
# 							 value='apple'),
# 		className='mb-2'
# 	),
	
# 	dbc.Row([
# 		dbc.Col(subj_figure := dcc.Graph(figure={}), width=6),
# 		dbc.Col(polrt_figure := dcc.Graph(figure={}), width=6)
# 	]),
	
# 	output_table := html.Div(children=[])

# ], fluid=True)	

sentiment_analysis_layout = dbc.Container([
	html.Div(children=[
		navigation.navbar,
    	html.Br(),
	]),
	html.Div(children=[
		html.Div(children=[
			html.H4("Search Term:", style={'textAlign': 'center', 'color': '#150a00',}),
			html.Center(
				user_search := dcc.Input(type='text', 
									debounce=True, 
									placeholder="Type search term for tweets", 
									value='apple',
									),
				className='mb-2'
			),
			html.H6("Press enter to start the anlysis process", style={'textAlign': 'center', 'color': '#150a00',}),
		]),
		html.Div(children=[
			dbc.Row([
				dbc.Col(subj_figure := dcc.Graph(figure={}), width=6),
				dbc.Col(polrt_figure := dcc.Graph(figure={}), width=6)
			]),
		],
		className="sub_pol_div"),
	],
	className="keyword_search_div"),
	html.Div(children=[
			html.H3("Analyzed Tweets",
            style = { # Styling quote
                    'color': 'yellow',
                    'text-align': 'center',
                    'margin-top:': 20,
                    }
            ),
            html.Br(),
			output_table := html.Div(children=[])
		],
		className="table_div"),
], fluid=True)

@callback(
	Output(output_table,'children'),
	Output(subj_figure, 'figure'),
	Output(polrt_figure, 'figure'),
	Input(user_search, 'value')
)
def update_app(search_term):
	tweets = api.search_tweets(q=search_term, lang="en", count=30, result_type="popular", tweet_mode='extended')
	if len(tweets)==0:
		tweets = api.search_tweets(q=search_term, lang="en", count=30, result_type="recent", tweet_mode='extended')

	cleaned_tweet, subjectivity_scores, polarity_scores = [], [], []
	for tweet in tweets:
		# Clean the tweet
		cleaned = clean_tweets(tweet.full_text)

		# Subjectivity analysis
		s = TextBlob(cleaned).sentiment.subjectivity
		subjectivity_scores.append(s)

		# Polarity analysis
		p = TextBlob(cleaned).sentiment.polarity
		polarity_scores.append(p)

		# Build list of all cleaned tweets
		cleaned_tweet.append(cleaned)
		
		cleaned_tweets = []
		for i in cleaned_tweet:
			if i not in cleaned_tweets:
				cleaned_tweets.append(i)


		# cleaned_tweets.drop_duplicates(inplace=True, ignore_index=True)

	# Calculate average of subjectivity and polarity scores
	average_subj = sum(subjectivity_scores) / len(subjectivity_scores)
	average_polrty = sum(polarity_scores) / len(polarity_scores)

	# Create Dash DataTable
	table_data = [{'Tweets being analyzed are listed below:': t[:160]} for t in cleaned_tweets]
	the_table = dash_table.DataTable(table_data, style_cell={'textAlign': 'left'})
	
	# Create Bar chart of subjectivity scores
	fig_s = go.Figure(data=[go.Bar(y=subjectivity_scores)])
	fig_s.add_hline(y=average_subj, annotation_text="Mean:"+str(round(average_subj,2)), annotation_font_color="black", annotation_position="top left", annotation_font_size=30)
	fig_s.update_traces(text=subjectivity_scores, textposition='inside', texttemplate='%{text:.2}')
	fig_s.update_xaxes(showticklabels=False)
	fig_s.update_layout(title="Subjectivity Scores")

	# Create Bar chart of Polarity (sentiment)
	fig_p = go.Figure(data=[go.Bar(y=polarity_scores)])
	fig_p.add_hline(y=average_polrty, annotation_text="Mean:"+str(round(average_polrty,2)), annotation_font_color="black", annotation_position="top left", annotation_font_size=30)
	fig_p.update_traces(text=polarity_scores, textposition='inside', texttemplate='%{text:.2}')
	fig_p.update_xaxes(showticklabels=False)
	fig_p.update_layout(title="Polarity Scores")

	return the_table, fig_s, fig_p