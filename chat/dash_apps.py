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
df = pd.DataFrame(list(Cigar.objects.order_by('pub_date').values()))
filt = df.loc[df['stopped'] == 1]
df = pd.DataFrame(list(Cigar.objects.order_by('pub_date').values()))
nofilt = df.loc[df['stopped'] == -1]
#df = px.data.tips()

fig = go.Figure()
fig.add_trace(go.Histogram(
    x=filt['pub_date'],
    y=filt['stopped'],
    name='control', # name used in legend and hover labels
    xbins=dict( # bins used for histogram
        end='2021-3-31 12:00',
        size= 3600000.0,
        start='2021-1-01 12:00'
    ),
    marker_color='green',
    opacity=0.75
))

fig.add_trace(go.Histogram(
    x=nofilt['pub_date'],
    y=nofilt['stopped'],
    name='control', # name used in legend and hover labels
    xbins=dict( # bins used for histogram
        end='2021-3-31 12:00',
        size= 3600000.0,
        start='2021-1-01 12:00'
    ),
    marker_color='red',
    opacity=0.75
))
fig.update_layout(barmode='stack')

def layouto():
    return html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),



    dcc.Graph(
        id='example-graph',

        figure= fig
    ),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div([
    dcc.Markdown(id='hoverdata-text')
])
])

app.layout = layouto


@app.callback(dash.dependencies.Output('hoverdata-text','children'),
             [dash.dependencies.Input('example-graph','figure')])
def callback_stats(hoverData):
    return str(hoverData['data'][0]['xbins'])


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
print(aux.describe())
listap.layout = html.Div(children=[
    html.H4(children='DataRawShowed'),
    generate_table(aux)
])


#https://chart-studio.plotly.com/create/
print(aux)