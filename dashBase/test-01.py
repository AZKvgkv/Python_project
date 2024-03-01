import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

df = pd.read_excel('fruits.xlsx', sheet_name='表1')
df.columns = ['fruits', 'year', 'amount']
fig = px.bar(df, x='fruits', y='amount', color='year', barmode='group')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Dash App -- 2021~2023 水果销量图'),
    html.Div('常见水果'),
    dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run_server(debug=True)
