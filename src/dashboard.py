'''
    Code contributed by Bikramdeep Singh
    Time stamp: 13-Nov-2022 12:24 PM
'''

'''
    Underlying necessary libraries are installed which are further imported in the code
    pip install dash
'''

#Importing necessary libraries to work on building with TweetitBig dashboard
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px