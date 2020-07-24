import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app
import base64
import os
import lorem
import graphs
import datasets

data = datasets.data

delito_tab = html.Div([
    dbc.Row([
        # Espacio para el gráfico
        dbc.Col([
            dcc.Graph(
                figure=graphs.plot_kde(data, 'min_pena', 'num_reincidencia', [1, 2, 3]),
                id='dist-penas',
                # className='figure'
            )
        ], width={'size': 8}, className='page_content'),
        dbc.Col([
            html.H3(["Gravedad del delito según el número de reincidencia"]),
            html.H6('Seleccione la reincidencia'),
            dcc.Dropdown(
                options=[
                    {'label': 'Pena mínima', 'value': 'min_pena'},
                    {'label': 'Pena media', 'value': 'avg_pena'},
                    {'label': 'Pena máxima', 'value': 'max_pena'},
                    {'label': 'Gravedad del delito', 'value': 'gravedad_delito'}
                ],
                value='min_pena',
                id='dd-gravedad-delito'
            ),
            html.H6('Seleccione el indicador de gravedad de pena'),
            dcc.Dropdown(
                options=[
                    {'label': 'Primera', 'value': 1},
                    {'label': 'Segunda', 'value': 2},
                    {'label': 'Tercera', 'value': 3},
                    {'label': 'Cuarta', 'value': 4},
                    {'label': 'Quinta', 'value': 5},
                    {'label': 'Sexta', 'value': 6},
                ],
                value=[1, 2, 3],
                multi=True,
                id='dd-reincidencia'
            ), 
            html.P(["""

            """])
        ], width={'size': 4}, className='aside-element', align='center')
    ]),
    dbc.Row([
        # Espacio para el gráfico
        dbc.Col([
            html.Div(className='div-line'),
            html.Img(src=app.get_asset_url('plot_test.png'), )
        ], width={'size': 8}, className='page_content'),
        dbc.Col([
            html.H3(["Movimiento a través de diferentes delitos"]),
            html.P(["""
                Using the top 20 of the crimes in the dataset that was given to the team during the process, 
                the team decided to plot the evolution of the recidivism, from the previous analysis we could 
                see that the majority of the prisoners stayed in HURTO during their evolution of crimes in recidivism. 
                Mostly due to the fact that HURTO is one of the felonies with lower punishment, meaning that 
                prisoners can pay their penalty and could fall over again.
            """])
        ], width={'size': 4}, className='aside-element', align='center')
    ]),
    dbc.Row([
        # Espacio para el gráfico
        dbc.Col([
            html.Div(className='div-line'),
            html.Img(src=app.get_asset_url('plot_test2.png'))
        ], width={'size': 8},className='page_content'),
        dbc.Col([
            html.H3(['Evolución de las penas a través de las rencidencias']),
            html.P(["""
                The next boxplot graph shows repeat offense event number on the x-axis, and average imprisonment 
                time for the crime on the y-axis. A distinction is made between having or no children under 18. 
                It is found that for the first repeat offense the imprisonment time is higher, and that imprisonment
                    time is reduced for the next repeat offense events. It can be said that there is no difference 
                    between having or no children under 18.
            """])
        ], width={'size': 4}, className='aside-element', align='center'),
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(className='div-line'),
            dcc.Graph(figure=graphs.load_json_figure('plots/figure.json'))
        ], width={'size': 8},className='page_content'),
        dbc.Col([
            html.H3([lorem.sentence()]),
            html.P([lorem.paragraph()])
        ], width={'size': 4}, className='aside-element', align='center'),
    ]),
])

eda_layout = html.Div([
    dbc.Row([ # Pestañas para la selección de factores
        dbc.Alert("Seleccione el factor de análisis", color="dark", fade=True, duration=5000),
        dbc.Col([
            dbc.Tabs([
                dbc.Tab([delito_tab], label="Por delito", tab_id='delito'),
                dbc.Tab(label="Por edad", tab_id='edad'),
                dbc.Tab(label="Por educación", tab_id='educacion'),
                dbc.Tab(label="Por establecimiento carcelario", tab_id='establecimiento'),
                dbc.Tab(label="Por lugar de origen", tab_id='lugar'),
            ], id='tabs-eda', active_tab='delito')
        ], width={'size': 12})
    ]),
    # Contenido
    
])


@app.callback(Output('dist-penas', 'figure'),
              [Input('dd-gravedad-delito', 'value'),
              Input('dd-reincidencia', 'value')])
def plot_dist_penas(gravedad, reincidencia):
    return graphs.plot_kde(data, gravedad, 'num_reincidencia', reincidencia)