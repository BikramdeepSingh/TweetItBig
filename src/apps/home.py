'''
    Code contributed by Bikramdeep Singh
    Time stamp: 11-Dec-2022 09:20 PM
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
#import navigation_old
import navigation

# home_layout = html.Div(children=[
#     navigation.navbar,
#     html.Br(),
#     html.H4(
#         children="What capabilities does twitter provide?", # Quote of TweetitBig
#         style = { # Styling quote
#                 'color': 'Black',
#                 'text-align': 'left',
#                 'margin-top:': 20,
#                 }
#     ),
#     html.P(
#         children="""
#         Twitter enables users to follow people or businesses who post content they enjoy reading, find articles about 
#         the biggest news and events of the day, or just connect with pals. Additionally, PR departments and marketers 
#         can utilize Twitter to engage their audience and raise brand awareness.
#         """,
#         style={
#             'color': 'Black',
#             'text-align': 'left',
#             'margin-top:': 20,
#         }
#     ),
#     html.H3(
#         children="Don't just be a Tweeter, make use of it!", # Quote of TweetitBig
#         style = { # Styling quote
#                 'color': 'Black',
#                 'text-align': 'center',
#                 'margin-top:': 20,
#                 }
#     ),
# ],
# className="card_container"
# )
dash.register_page(__name__,path='/')

home_layout = html.Div((
    html.Div(children=[
        navigation.navbar,
        html.Br(),
    ]),
    html.Div(children=[
        html.Br(),
        html.Img(src="/assets/cover.jpg", className="home_image"),
        html.Br(),
        html.H3(
            children="Welcome to the world of tweets!", # Quote of TweetitBig
            style = { # Styling quote
                    'color': 'Black',
                    'text-align': 'center',
                    'margin-top:': 20,
                    'font-family': 'Comic Sans MS',
                    }
        ),
        html.Br(),
        html.Div(children=[
            html.H1(children="Simple and Powerful Twitter Analytics",
            style={
                'font-family': 'Cooper Black',
                'color': '#0300ff',
            }),
        ],
        className="home_tagline"),
        html.Br(),
        html.Div(children=[
            html.H4(children="Understand what you need. Plan how to approach. \n Use the power of TweetitBig to get a quick analysis.",
            style={
                'font-family': 'Comic Sans MS',
            })
        ], 
        className="home_base_tagline"),
        html.Br(),
    ],
    ),
    # html.Div(children=[
    #     html.H3(
    #     children="Welcome to the world of tweets!", # Quote of TweetitBig
    #     style = { # Styling quote
    #             'color': 'cyan',
    #             'text-align': 'center',
    #             'margin-top:': 20,
    #             }
    # ),
    # ],
    # className="card_container"),
    html.Div(children=[
        html.H4(
        children="What capabilities does twitter provide?", # Quote of TweetitBig
        style = { # Styling quote
                'color': 'White',
                'text-align': 'left',
                'margin-top:': 20,
                }
        ),
        html.P(
        children="""
        Twitter enables users to follow people or businesses who post content they enjoy reading, find articles about 
        the biggest news and events of the day, or just connect with pals. Additionally, PR departments and marketers 
        can utilize Twitter to engage their audience and raise brand awareness.
        """,
        style={
            'color': 'White',
            'text-align': 'left',
            'margin-top:': 20,
            'font-size': 18,
        }
        ),
    ],
    className="card_container"),

    html.Div(children=[
        html.H3(
        children="Don't just be a Tweeter, make use of it!", # Quote of TweetitBig
        style = { # Styling quote
                'color': 'cyan',
                'text-align': 'center',
                'margin-top:': 20,
                }
    ),
    ],
    className="card_container"),

    html.Div(children=[
        html.Div(children=[
            html.Img(src="https://www.pngkit.com/png/full/497-4979790_splash-twitter-icon-png-hd-image-free-download.png", alt="twitter png",width="250", height="220",)
        ],
        className="home_left_align"),
        html.Div(children=[
             html.P("Is there any way to forecast the use of tweets for any good?",
             style={
            'color': 'White',
            'text-align': 'center',
            'margin-top:': 20,
            'font-size': 24,
        }),
             html.P("""
             TweetitBig is the use case proposed using twitter handle. Having bulk of data all across the internet 
             is of no use if that can’t be converted into information. Forming informational content from flowing 
             pipelines of data and marking the point of interest for each user is what can excite a ‘Tweeter’. 
             """,
             style={
            'color': 'White',
            'text-align': 'center',
            'margin-top:': 20,
            'font-size': 18,
        }),
             
        ],
        className="home_right_align"),
    ],className="parent_side_by_side"),

))
