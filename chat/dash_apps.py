import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from .models import Cigar
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

app = DjangoDash('SimpleExample')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.DataFrame(list(Cigar.objects.order_by('-pub_date').values()))
#df = px.data.tips()

print(df.describe())
print(df.pub_date.describe())
df['DateTime'] = pd.to_datetime(df['pub_date'], format='%y-%d-%m %H:%M')
print("HOla?")
fig = px.bar(df, x="DateTime", y="stopped")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',

        figure= fig
    )
])
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


listap = DjangoDash("ListaCigars")
aux = pd.DataFrame(list(Cigar.objects.order_by('-pub_date').values()))
listap.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(aux)
])
#https://chart-studio.plotly.com/create/
print(aux)