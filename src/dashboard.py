'''
    Code contributed by Bikramdeep Singh
    Time stamp: 13-Nov-2022 12:24 PM
'''

'''
    Underlying necessary libraries are installed which are further imported in the code
    pip install dash
'''

# Importing necessary libraries to work on building with TweetitBig dashboard
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Loading the dataset from data directory
TiB_data = pd.read_excel('C:\Academics\Sem2\AISC2006_Step2\TweetItBig\TweetItBig\data\Final_output.xlsx')

# Creating the TweetitBig Dash app
app = dash.Dash()

# Set up the app layout
app.layout = html.Div(children=[
    html.H1(children='TweetitBig'),
    dcc.Dropdown(id='search-dropdown',
                    options=[{'label':i, 'value':i}
                             for i in TiB_data['search_term'].unique()],
                    value='apple'),
    dcc.Graph(id='search-graph')
])

# Setting up the callback function
@app.callback(
    Output(component_id='search-graph', component_property='figure'),
    Input(component_id='search-dropdown', component_property='value')
)
def update_graph(selected_search):
    filtered_sentiment = TiB_data[TiB_data['search_term'] == selected_search]
    line_fig = px.line(filtered_sentiment,
                        x='date', y='retweet_cnt', color='Vader_sentiment',
                        title=f'Sentiment variation for {selected_search}'
    )
    return line_fig

# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)