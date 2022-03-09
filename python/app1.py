from dash import Dash, Input, Output, callback, dash_table, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px


# external JavaScript files
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]



app = Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

df =  pd.read_csv('/Users/kurtbembridge/Downloads/train.csv')

dropper = ['Pclass', 'Sex', ]
df = df.drop('PassengerId', axis= 1)

df = df.groupby(['Embarked', 'Sex']).mean()

fig = px.parallel_coordinates(df, color="Survived", color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)

#fig.show()

app.layout = dbc.Container([
    dbc.Label('Click a cell in the table:'),
    dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], id='tbl'),
    dbc.Alert(id='tbl_out'),
    dcc.Graph(
        id='example-graph',
        figure = fig
    )
])

@callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"

if __name__ == "__main__":
    app.run_server(debug=True)