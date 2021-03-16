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

#df = px.data.tips()
def figuron():
    df = pd.DataFrame(list(Cigar.objects.order_by('pub_date').values()))
    filt = df.loc[df['stopped'] == 1]
    df = pd.DataFrame(list(Cigar.objects.order_by('pub_date').values()))
    nofilt = df.loc[df['stopped'] == -1]
    print("Pues llamo a figure")
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=filt['pub_date'],
        y=filt['stopped'],
        name='control', # name used in legend and hover labels
        xbins=dict( # bins used for histogram
            end='2021-3-31 00:00',
            size= 3600000.0,
            start='2021-1-01 00:00'
        ),
        marker_color='green',
        opacity=0.75
    ))

    fig.add_trace(go.Histogram(
        x=nofilt['pub_date'],
        y=nofilt['stopped'],
        name='control', # name used in legend and hover labels
        xbins=dict( # bins used for histogram
            end='2021-3-31 00:00',
            size= 3600000.0,
            start='2021-1-01 00:00'
        ),
        marker_color='red',
        opacity=0.75
    ))
    fig.update_layout(barmode='stack')
    return fig

def layouto():
    print("pues llamamos a layout")
    return html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),



    dcc.Graph(
        id='egraph',

        figure= figuron()
    ),
    dcc.Dropdown(
        id='date-pick',
        options=[{'label': 'Day', 'value': 3600000*24},
                 {'label': 'Hour', 'value': 3600000},
                 {'label': '4 Hour', 'value': 3600000*4}],
        value=3600000
    ),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div([
    dcc.Markdown(id='hoverdata-text')
])
])

app.layout = layouto


@app.callback(dash.dependencies.Output('hoverdata-text','children'),
             [dash.dependencies.Input('egraph','figure')])
def callback_stats(hoverData):
    return str(hoverData['data'][0]['xbins'])


@app.callback(dash.dependencies.Output('egraph', 'figure'),
             [dash.dependencies.Input('date-pick', 'value')])
def ojala(child):
    df = pd.DataFrame(list(Cigar.objects.order_by('pub_date').values()))
    filt = df.loc[df['stopped'] == 1]
    df = pd.DataFrame(list(Cigar.objects.order_by('pub_date').values()))
    nofilt = df.loc[df['stopped'] == -1]
    print("Pues llamo a figure")
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=filt['pub_date'],
        y=filt['stopped'],
        name='control',  # name used in legend and hover labels
        xbins=dict(  # bins used for histogram
            end='2021-3-31 00:00',
            size=child,
            start='2021-1-01 00:00'
        ),
        marker_color='green',
        opacity=0.75
    ))

    fig.add_trace(go.Histogram(
        x=nofilt['pub_date'],
        y=nofilt['stopped'],
        name='control',  # name used in legend and hover labels
        xbins=dict(  # bins used for histogram
            end='2021-3-31 00:00',
            size=child,
            start='2021-1-01 00:00'
        ),
        marker_color='red',
        opacity=0.75
    ))
    fig.update_layout(barmode='stack')
    return fig

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