#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output 
import dash_bootstrap_components as dbc

from app import app
from apps import home, apple_analysis, sentiment_analysis, about



url_content_layout = html.Div(children=[
    dcc.Location(id="url",refresh=False),
    html.Div(id="output-div")
])

# Creating the TweetitBig Dash app
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.ZEPHYR, dbc.icons.BOOTSTRAP])
# Altering the title and favicon from default to custom
app.title = "TweetitBig" 
'''
    In order to execute the favicon code, folder named assets is required as it takes the path for 
    it by default and cannot be altered.
    Save the favicon icon inside assets folder to successfully execute this below code.
'''
app._favicon = ("logo.png") 
app.layout = url_content_layout

app.validation_layout = html.Div([
    url_content_layout,
    home.home_layout,
    apple_analysis.apple_analysis_layout,
    sentiment_analysis.sentiment_analysis_layout,
    about.about_layout,
])


@app.callback(Output(component_id="output-div",component_property="children"),Input(component_id="url",component_property="pathname"))
def update_output_div(pathname):
    if pathname == "/about":
        return  about.about_layout
    elif pathname == "/apple_analysis":
        return apple_analysis.apple_analysis_layout
    elif pathname == "/sentiment_analysis":
        return sentiment_analysis.sentiment_analysis_layout
    else:
        return home.home_layout


if __name__ == "__main__":
    app.run_server(debug=False)