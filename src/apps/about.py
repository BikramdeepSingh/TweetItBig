'''
    Code contributed by Bikramdeep Singh
    Time stamp: 12-Dec-2022 00:10 PM
'''

import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output 
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import navigation

# about_layout = html.Div(children=[
#     navigation.navbar,
#     html.H1(children="This is the about page for TweetitBig")
# ])

about_layout = html.Div((
    html.Div(children=[
        navigation.navbar,
    ]),
    html.Div(children=[
        html.Br(),
        html.H3(children="Why TweetitBig?",
        style = { # Styling quote
                'color': 'yellow',
                'text-align': 'center',
                'margin-top:': 20,
                }
        ),
        html.Br(),
        html.P("""
        TweetitBig is a web application which dynamically allows you to analyse the tweets on selected keywords in the scope 
        of the big company 'apple'. How the trends are being followed and looked up by the tweeters lets you get a in short 
        summary using graphs, plots and charts. 
        """),
        html.P("""
        To not limit its scope, TweetitBog also allows the user to use the 'Keyword Search' section to enter their own keyword
        and get the sentiment interms of subjectivity and polarity scores, which also plots the mean of them.
        """),
        html.P("""
        The goal of subjectivity detection is to eliminate "factual" or "neutral" content, or objective text devoid of 
        any opinion.
        """),
        html.P("""
        The goal of polarity detection is to categorize an opinion as "positive" or "negative."
        """),
    ],
    className="about_card_container"),

))
