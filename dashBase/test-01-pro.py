# 升级成面向对象的方式
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html


class MyDashApp:
    def __init__(self):
        self.fig = None
        self.colors = {
            'background': '#111111',
            'text': '#7FDBFF'
        }
        self.dash_data()
        self.dash_layout()

    def dash_data(self):
        """数据与业务逻辑处理"""
        df = pd.read_excel('fruits.xlsx', sheet_name='表1')
        df.columns = ['fruits', 'year', 'amount']
        self.fig = px.bar(df, x='fruits', y='amount', color='year', barmode='group')
        self.fig.update_layout(
            plot_bgcolor=self.colors['background'],
            paper_bgcolor=self.colors['background'],
            font_color=self.colors['text']
        )

    def dash_layout(self):
        """布局"""
        app.layout = html.Div(
            style={'backgroundColor': self.colors['background']},
            children=[
                html.H1(
                    id='title',
                    style={'textAlign': 'center', 'color': self.colors['text'], 'fontSize': 30, 'margin': '10px'},
                    children='Dash App -- 2021~2023 水果销量图'),
                html.Div(
                    id='subtitle',
                    style={'textAlign': 'center', 'color': self.colors['text'], 'fontSize': 15, 'margin': '10px'},
                    children='常见水果'),
                dcc.Graph(id='example-graph-fruits',
                          figure=self.fig)
            ])


if __name__ == '__main__':
    app = dash.Dash(__name__)
    MyDashApp()
    app.run_server(debug=True)
