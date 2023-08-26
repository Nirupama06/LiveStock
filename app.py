from dash import Dash, dcc, html
# import dash_core_components as dcc
# import dash_html_components as html
from datetime import date

app=Dash(__name__)

server=app.server
app.layout = html.Div([
    html.Div([
        html.H1('Welcome to the stock dash app! ', className="start"),
        html.Div([
            html.P('Input Stock Code'),
            dcc.Input(id="stockCode", type="text", placeholder="stockCode", style={'marginRight':'10px'}),
        ]),
        html.Div([
            dcc.DatePickerSingle(
                month_format='MMM Do, YY',
                placeholder='start->',
                date=date(2017, 6, 21),
                className="datePicker",
            )
        ]),
        html.Div([
            # Stock price button
            html.Button('Stock Price', id='btn-Stock-Price'),
            # Indicators button
            html.Button('Indicators', id='btn-Indicator'),
            # Number of days of forecast input
            dcc.Input(id="numOfDays", type="text", placeholder="Number of Days ", style={'marginRight':'10px'}),
            # Forecast button
            html.Button('Forecast', id='btn-Forecast'),
        ])
    ], className="inputs"),
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
    
],className="container")


if __name__ == '__main__':
    app.run_server(debug=True)