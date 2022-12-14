import dash
import dash_bootstrap_components as dbc
from dash import html


#use_pages=True
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.UNITED, dbc.icons.BOOTSTRAP],suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div(children=[
    dash.page_container
])


# if __name__ == "__main__":
#     #app.run_server(debug=True)
#     app.run_server(debug=False,port=8080)