from dash import Dash, dcc, html
# import dash_core_components as dcc
# import dash_html_components as html
from datetime import datetime as dt

app=Dash(__name__)

server=app.server
app.layout = html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Welcome to the stock dash app! ', className="start"),
        html.Div([
            # data range picker input
        ]),
        html.Div([
            # Stock price button
            # Indicators button
            # Number of days of forecast input
            # Forecast button
        ])
    ], className="nav"),
    html.Div([
        html.Div([
            #LOGO
            #COMPANY NAME
        ], className="header"),

        html.Div([
            #Description
        ], id="description", className="description_ticker"),
        html.Div([
            #Stock price plot
        ], id="graphs-content"),
        html.Div([
            #Indicator plot
        ], id="main-content"),
        html.Div([
            #Forecast plot
        ], id="forecast-content")
    ],className="Content"),
    
])


if __name__ == '__main__':
    app.run_server(debug=True)