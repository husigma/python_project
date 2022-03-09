# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash 
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import numpy as np



df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

app = dash.Dash(__name__)



data = [[1, 20, 30],
                 [20, 1, 60],
                 [30, 60, 110]]

data = pd.DataFrame(data)

fig = px.imshow(data)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)