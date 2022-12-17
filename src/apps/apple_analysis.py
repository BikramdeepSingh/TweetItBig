'''
    Code contributed by Bikramdeep Singh
    Time stamp: 11-Dec-2022 10:39 PM
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
import os
from app import app

# # Loading the dataset from data directory
# TiB_data = pd.read_excel('data/Final_output.xlsx')
TiB_data = pd.read_excel(os.path.join(os.path.dirname(__file__),'..','..','data','Final_output.xlsx'))
TiB_data.head()

# # Creating the TweetitBig Dash app
# app = dash.Dash(__name__,external_stylesheets=[dbc.themes.ZEPHYR, dbc.icons.BOOTSTRAP])
# # Altering the title and favicon from default to custom
# app.title = "TweetitBig" 
# '''
#     In order to execute the favicon code, folder named assets is required as it takes the path for 
#     it by default and cannot be altered.
#     Save the favicon icon inside assets folder to successfully execute this below code.
# '''
# app._favicon = ("logo.png") 


# Coloring scheme which is used for sentiment identification
sentiment_colors = ['rgb(0, 255, 0)', 'rgb(0, 0, 255)', 'rgb(255, 0, 0)']

# Setting up the app layout
# app.layout = html.Div(children=[
# apple_analysis_layout = html.Div(children=[
#     navigation.navbar,
#     html.Br(),
#     # html.H1(children='TweetitBig', # Giving heading to website
#     #         style = { # Styling the heading
#     #                 'color': '#4169e1',
#     #                 'text-align': 'center'
#     #                 }
#     #         ),
#     # html.H3(
#     #     children="Don't just be a Tweeter, make use of it!", # Quote of TweetitBig
#     #     style = { # Styling quote
#     #             'color': 'Black',
#     #             'text-align': 'center',
#     #             'margin-top:': 20,
#     #             }
#     # ),
#     # Creating a dropdown list for search keywords i.e. apple to update scatter plot on selection
#     dcc.Dropdown(id='search-dropdown', 
#                 options=[{'label':i, 'value':i}
#                         for i in TiB_data['search_term'].unique()], # Only displaying the unique values in dropdown list
#                 value='apple'), # Setting default value for dropdown to apple
#     dcc.Graph(id='search-graph'), # Graph to be rendered
    
    
#     # dcc.Dropdown(
#     #     id="scattermatrix_dropdown",
#     #     options=[{'label':i, 'value':i}
#     #               for i in TiB_data['Vader_sentiment'].unique()],
#     #     value='Positive',
#     #     multi=True
#     # ),

#     # dcc.Graph(id="pie-graph"), # Graph to be rendered
#     # dcc.Interval(id = 'search_update', interval= 300*1000, n_intervals = 0), # This code updates the plot after every 5 minutes
    
#     # dcc.Graph(id="hist-graph"),
#     # dcc.Interval(id = 'search_hist_update', interval= 300*1000, n_intervals = 0), # This code updates the plot after every 5 minutes

#     # dcc.Graph(id="multi-column-graph"), # Rendering a 2 column graph in a single row
#     # html.P("Width Slider:"), # Implementing width slider for multi-column-graph
#     # # Setting slider properties
#     # dcc.Slider(
#     #     id='slider-width', 
#     #     min=.1, 
#     #     max=.9, 
#     #     value=0.5, 
#     #     step=0.1),
# ])


apple_analysis_layout = dbc.Container([
	html.Div(children=[
        navigation.navbar,
    ]
        ),
    html.Br(),
    html.Div(
        children=[
            html.Div(children=[
            html.H3("Analysis on Apple Keywords",
            style = { # Styling quote
                    'color': 'yellow',
                    'text-align': 'center',
                    'margin-top:': 20,
                    }
            ),
            html.Br(),
            dcc.Dropdown(id='search-dropdown', 
                    options=[{'label':i, 'value':i}
                            for i in TiB_data['search_term'].unique()], # Only displaying the unique values in dropdown list
                    value='apple'), # Setting default value for dropdown to apple
            html.Br(),
            dcc.Graph(id='search-graph'),
        ],
        className="scatter_div left_graph"
        ),
        html.Div(children=[
            html.H3("Sentiment Distribution",
            style = { # Styling quote
                    'color': 'yellow',
                    'text-align': 'center',
                    'margin-top:': 20,
                    }
            ),
            html.Br(),
            dcc.Graph(id="pie-graph"), # Graph to be rendered
            dcc.Interval(id = 'search_update', interval= 300*1000, n_intervals = 0), # This code updates the plot after every 5 minutes
        ],
        className="scatter_div right_graph"
        ),
        ],
        className="parent_graph",
    ),
    html.Div(
        children=[
            html.H3("Most frequent words in positive tweets",
            style = { # Styling quote
                    'color': 'yellow',
                    'text-align': 'center',
                    'margin-top:': 20,
                    }
            ),
            html.Br(),
            dcc.Graph(id="hist-graph"),
            dcc.Interval(id = 'search_hist_update', interval= 300*1000, n_intervals = 0), # This code updates the plot after every 5 minutes
        ],
        className="scatter_div"
    ),
], fluid=True)

# Setting up the callback function
'''
    Automatically called whenever an UI element is changed.
    In our case, updates to dropdown will be handled with callback
'''
@app.callback(
    Output(component_id='search-graph', component_property='figure'),
    Input(component_id='search-dropdown', component_property='value'),
)
# update function executed to work with dropdown list creating a scatter plot
def update_graph(selected_search):
    filtered_sentiment = TiB_data[TiB_data['search_term'] == selected_search]
    scatter_fig = px.scatter(
        filtered_sentiment, 
        x='date', 
        y='retweet_cnt', 
        color='Vader_sentiment', 
        title=f'Sentiment variation for tweets getting retweeted with {selected_search} keyword', 
        height=600,
    )
    return scatter_fig

@app.callback(
    Output("pie-graph", "figure"), 
    Input("search_update", "n_intervals"))
# update function executed to work with intervals list creating a pie chart
def update_pie(graph_params):
    pie_plot = px.pie(
                        TiB_data, 
                        values='favourites_cnt', 
                        names='Vader_sentiment', 
                        hole=.3, 
                        title=f'Categorical percent of favourite tweets', 
                        height=700
                     )
    pie_plot.update_traces(
        textposition='inside', 
        textinfo='percent+label', 
        marker_colors=sentiment_colors
        )
    return pie_plot


@app.callback(
    Output("hist-graph", "figure"), 
    Input("search_hist_update", "n_intervals"))
# update function executed to work with dropdown list creating a histogram
def update_hist(graph_params):
    hist_plot = px.histogram(
        TiB_data, 
        x="search_term", 
        y="Vader_sentiment", 
        pattern_shape="user_verified", 
        title=f'Sentiments count against keywords', 
        color='Vader_sentiment', 
        barmode='group', 
        histfunc='count', 
        text_auto=True, 
        height=700)
    hist_plot.update_yaxes(title_text="Sentiment Count")
    hist_plot.update_xaxes(title_text="Search Keyword")
    return hist_plot                 

# @app.callback(
#     Output("multi-column-graph", "figure"), 
#     Input("slider-width", "value"))
# # update function executed to work with slider and traces list creating multi-column-graph
# def customize_width(left_width):
#     fig = make_subplots(
#         rows=1, 
#         cols=2, 
#         column_widths=[left_width, 1 - left_width]
#         )

#     fig.add_trace(
#         row=1, 
#         col=1,
#         trace=go.Scatter(
#             x=TiB_data['date'], 
#             y=TiB_data['followers_cnt']
#             )
#         ) 
#     fig.update_xaxes(
#         title_text="xaxis 1 title", 
#         row=1, 
#         col=1
#         )
#     fig.update_yaxes(
#         title_text="Sentiment", 
#         row=1, 
#         col=1
#         )

#     fig.add_trace(
#         row=1, 
#         col=2,
#         trace=go.Scatter(
#             x=TiB_data['Vader_sentiment'], 
#             y=TiB_data['date']
#             )
#         )
#     fig.update_xaxes(
#         title_text="xaxis 2 title", 
#         row=1, 
#         col=2
#         )
#     fig.update_yaxes(
#         title_text="Sentiment", 
#         row=1, 
#         col=1
#         )

#     # Updating title and height
#     fig.update_layout(
#         title_text="Subplots testing", 
#         height=650
#         )
#     return fig