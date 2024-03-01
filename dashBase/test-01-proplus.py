import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html


def generate_table(df, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df), max_rows))
        ])
    ])


class MyDashApp:
    def __init__(self):
        self.app = app
        self.df1 = None
        self.fig = None
        self.colors = {
            # 'background': '#111111',  # 深灰色
            'background': '#FFFFFF',  # 白色
            # 'background': '#FFA500',  # 橙色
            'text': '#7FDBFF'
        }
        self.dash_data()
        self.dash_layout()

    def dash_data(self):
        """数据与业务逻辑处理"""
        try:
            df = pd.read_excel('fruits.xlsx', sheet_name='表1')
            df.columns = ['fruits', 'year', 'amount']
            self.fig = px.bar(df, x='fruits', y='amount', color='year', barmode='group')
            self.fig.update_layout(
                plot_bgcolor=self.colors['background'],
                paper_bgcolor=self.colors['background'],
                font_color=self.colors['text']
            )
            self.df1 = pd.read_csv('usa-agricultural-exports-2011.csv')
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")
            return

    def dash_layout(self):
        """布局"""
        self.app.layout = html.Div(
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
                          figure=self.fig),
                html.H4('美国农业常量（2011）'),
                generate_table(self.df1)
            ])


if __name__ == '__main__':
    app = dash.Dash(__name__)
    my_app = MyDashApp()
    my_app.app.run_server(debug=True)
