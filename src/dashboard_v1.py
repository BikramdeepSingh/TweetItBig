'''
    Code contributed by Bikramdeep Singh
    Time stamp: 5-Dec-2022 12:24 PM
'''

'''
    Underlying necessary libraries are installed which are further imported in the code
    pip install dash
    pip install emoji
'''

# Importing necessary libraries to work on building with TweetitBig dashboard

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


# # Set authentication and access token
authenticate = tweepy.OAuthHandler("GjHSdsEXo251KIBS26eQILHLC", "qIzHTrs1ED7QVG3lUVtgqzxtlHqP8eZRdQ75kipAPhZ7VzqNJj")
# #authenticate.set_access_token(accessToken, accessTokenSecret)
# # Create Twitter API using authentication information
api = tweepy.API(authenticate, wait_on_rate_limit=True)

# # search tweets with a certain term and analyze them
# tweets = api.search_tweets(q="apple", lang="en", count=20)
# for tweet in tweets:
# 	#print(tweet.text)
# 	#print(tweet.retweet_count)

# 	# Clean the tweet
# 	cleaned = clean_tweets(tweet.text)
# 	s = TextBlob(cleaned).sentiment.subjectivity
# 	p = TextBlob(cleaned).sentiment.polarity
# 	print(f'Subjectivity is: {s}')
# 	print(f'Polarity/Sentiment is: {p}')
# 	print("---------------------")
# exit()



app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR])

# Altering the title and favicon from default to custom
app.title = "TweetitBig" 
'''
    In order to execute the favicon code, folder named assets is required as it takes the path for 
    it by default and cannot be altered.
    Save the favicon icon inside assets folder to successfully execute this below code.
'''
app._favicon = ("logo.png") 

app.layout = dbc.Container([
	navigation.navbar,
	html.H1("TweetitBig", style={
                    'color': '#4169e1',
                    'text-align': 'center'}),
    html.H3(
        children="Don't just be a Tweeter, make use of it!", # Quote of TweetitBig
        style = { # Styling quote
                'color': 'black',
                'text-align': 'center'
                }
    ),
	html.H4("Search Term:", style={'textAlign': 'center'}),
	html.Center(
		user_search := dcc.Input(type='text', 
							 debounce=True, 
							 placeholder="Type search term for tweets", 
							 value='apple'),
		className='mb-2'
	),
	
	dbc.Row([
		dbc.Col(subj_figure := dcc.Graph(figure={}), width=6),
		dbc.Col(polrt_figure := dcc.Graph(figure={}), width=6)
	]),
	
	output_table := html.Div(children=[])

], fluid=True)


@callback(
	Output(output_table,'children'),
	Output(subj_figure, 'figure'),
	Output(polrt_figure, 'figure'),
	Input(user_search, 'value')
)
def update_app(search_term):
	tweets = api.search_tweets(q=search_term, lang="en", count=100)

	cleaned_tweets, subjectivity_scores, polarity_scores = [], [], []
	for tweet in tweets:
		# Clean the tweet
		cleaned = clean_tweets(tweet.text)

		# Subjectivity analysis
		s = TextBlob(cleaned).sentiment.subjectivity
		subjectivity_scores.append(s)

		# Polarity analysis
		p = TextBlob(cleaned).sentiment.polarity
		polarity_scores.append(p)

		# Build list of all cleaned tweets
		cleaned_tweets.append(cleaned)

	# Calculate average of subjectivity and polarity scores
	average_subj = sum(subjectivity_scores) / len(subjectivity_scores)
	average_polrty = sum(polarity_scores) / len(polarity_scores)

	# Create Dash DataTable
	table_data = [{'Tweets': t} for t in cleaned_tweets]
	the_table = dash_table.DataTable(table_data, style_cell={'textAlign': 'left'})
	
	# Create Bar chart of subjectivity scores
	fig_s = go.Figure(data=[go.Bar(y=subjectivity_scores)])
	fig_s.add_hline(y=average_subj, annotation_text="Mean:"+str(round(average_subj,2)), annotation_font_color="black", annotation_position="top left", annotation_font_size=15)
	fig_s.update_traces(text=subjectivity_scores, textposition='outside', texttemplate='%{text:.2}')
	fig_s.update_xaxes(showticklabels=False)
	fig_s.update_layout(title="Subjectivity Scores")

	# Create Bar chart of Polarity (sentiment)
	fig_p = go.Figure(data=[go.Bar(y=polarity_scores)])
	fig_p.add_hline(y=average_polrty, annotation_text="Mean:"+str(round(average_polrty,2)), annotation_font_color="black", annotation_position="top left", annotation_font_size=15)
	fig_p.update_traces(text=polarity_scores, textposition='outside', texttemplate='%{text:.2}')
	fig_p.update_xaxes(showticklabels=False)
	fig_p.update_layout(title="Polarity Scores")

	return the_table, fig_s, fig_p


if __name__ == "__main__":
	app.run()