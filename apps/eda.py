import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app
import base64
import os


delito_tab = html.Div([
    dbc.Row([
        # Espacio para el gráfico
        dbc.Col([
            html.Img(src=app.get_asset_url('plot_test.png'))
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
