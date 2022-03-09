import numpy as np
import pandas as pd
import plotly 
import plotly.express as px
import os
from dash import Dash, Input, Output, callback, dash_table, dcc, html
from dash.dependencies import Input, Output

df = pd.read_csv('/Users/kurtbembridge/Downloads/train.csv')
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Div(
        dcc.Graph(id='graph',
                  style={'height': 400, 'width': 800}
                  ),
    ),
    html.Div([
                html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
                dcc.RadioItems(
                    id='radio',
                    options=[
                             {'label': 'graph1', 'value': 'graph1'},
                             {'label': 'graph2', 'value': 'graph2'},
                    ],
                    value='age',
                    style={"width": "60%"}
                ),
        ])

])

# ---------------------------------------------------------------
@app.callback(
    Output('graph', 'figure'),
    [Input(component_id='radio', component_property='value')]
)
def build_graph(value):
    if value == 'graph1':
        return px.scatter(
            df,
            x="Age",
            y="Fare",
            color="Sex",
            size_max=20,  # differentiate markers by color
            opacity=0.90)

    else:
        return px.scatter(
            df,
            x="Age",
            y="Pclass",
            color="Sex",
            size_max=20,  # differentiate markers by color
            opacity=0.90)

if __name__ == '__main__':
    app.run_server(debug=True)
    app.run_server("192.168.0.37","9090")