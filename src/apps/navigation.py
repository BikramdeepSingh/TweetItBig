'''
    Code contributed by Bikramdeep Singh
    Time stamp: 10-Dec-2022 10:12 AM
'''

# Importing necessary libraries to work navbar of TweetitBig dashboard

import dash_bootstrap_components as dbc
from dash import html
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container
#from app import app


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col([
                            html.Img(src="/assets/logo.png", height="30px"),
                            dbc.NavbarBrand("TweetitBig", className="ms-2")
                            ]),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),

            dbc.Row([
                dbc.Col([
                    dbc.Nav([
                        dbc.NavItem(dbc.NavLink("Home", href="/home")),
                        dbc.NavItem(dbc.NavLink("Apple Analysis", href="/apple_analysis")),
                        dbc.NavItem(dbc.NavLink("Keyword Search", href="/sentiment_analysis")),
                        dbc.NavItem(dbc.NavLink("Dataset", href="https://github.com/BikramdeepSingh/TweetItBig/tree/main/data")),
                        dbc.NavItem(dbc.NavLink("About", href="/about")),
                    ],
                    navbar=True,
                    )
                ],
                width={"size":"auto"}
                )
            ],
            align="center",
            className="g-0",
            ),

            dbc.Row([
                dbc.Col([
                    dbc.Nav([
                        dbc.NavItem(dbc.NavLink(html.I(className="bi bi-github"), href="https://github.com/BikramdeepSingh/TweetItBig",external_link=True)),
                        dbc.NavItem(dbc.NavLink(html.I(className="bi bi-twitter"), href="https://twitter.com/apple?lang=en",external_link=True)),
                    ],
                    navbar=True,
                    ),
                ])
            ],
            align="center",
            className="g-0",
            ),
        ],
        fluid=False,
    ),
    color="dark", #can also be kept as primary, light
    dark=True,
    sticky='top',
    expand= 'sm',
    className="g-0",
)