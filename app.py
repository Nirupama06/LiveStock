from dash import Dash, dcc, html, callback, Input, Output, State
# import dash_core_components as dcc
# import dash_html_components as html
from datetime import date
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px


app=Dash(__name__)

server=app.server
app.layout = html.Div([
    html.Div([
        html.Div([
            html.A('Link to stock codes',href="https://stockanalysis.com/stocks/", )
        ], className="link"),
        html.H1('Welcome to the stock dash app! ', className="start"),
        html.Div([
            html.P('Input Stock Code'),
            dcc.Input(id="stockCode", type="text", placeholder="stockCode", style={'marginRight':'10px'}, value="MSFT"),
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
            html.Button('Stock Price', id='btn-Stock-Price', n_clicks=0),
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
            # html.Img(id="logo",src="",alt="logo"),
            #COMPANY NAME
            html.Div(id='name'),
            html.Div(id='information'),
        
        ], className="header"),

        html.Div([
            #Description
        ], className="description_ticker"),
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

@app.callback(
    [
    Output(component_id="information",component_property="children"),
    Output(component_id="name",component_property="children"),
    ],
    [Input(component_id="btn-Stock-Price",component_property="n_clicks")],
    [State(component_id="stockCode", component_property="value")]
    )

def update_data(n,companyCode): # input parameter(s)
    if(len(companyCode)>0):
        company = yf.Ticker(companyCode)
        name=company.info['longName']
        information=company.info['longBusinessSummary']
        return [html.P(information)], [html.H3('Company: '+name)]
    else:
        company = yf.Ticker("MSFT")
        name=company.info['longName']
        information=company.info['longBusinessSummary']
        return [html.P(information)], [html.H3('Company: '+name)]



if __name__ == '__main__':
    app.run_server(debug=True)