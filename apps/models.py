import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import datasets as data
import graphs
import modelsObjects
from app import app
import base64
import datetime
import io
import pandas as pd
import dash_table

kModes = modelsObjects.kModes()
RF = modelsObjects.RF()

models_layout = html.Div([
    dbc.Row([ # Pestañas para la selección de modelos
        dbc.Col([
            dbc.Tabs([
                dbc.Tab(label="Clustering (K-Modes)", tab_id='kModes'),
                dbc.Tab(label="Clasificación (Random Forest)", tab_id='random-forest'),
            ], id='tabs', active_tab='kModes')
        ], width={'size': 12})
    ]),
    # Contenido
    dbc.Row([
        # Elemento Aside, lo que está en la parte izquierda la página
        dbc.Col([
            # Elemento aside del modelo
            html.Div(id='model-aside', className='interactive_container'),
            html.Div(id='upload-aside')
            
        ], width={'size': 4},className='aside-element'),

        # Contenido principal de la página
        dbc.Col([
            # Contenido del modelo, gráfico, descripción y grupos encontrados
            html.Div(id='model-page'),
            # Plot del dataset ya clasificado.
            html.Div(id='plot-new-dataset', style={'padding': '0px 50px 0px 50px'})
        ], width={'size': 8}, className='page_content')
    ])
])


upload_file_ly = html.Div([
    html.H4('Suba su Dataset para ser clasificado'),
    dcc.Markdown("""
        Seleccione su dataset para pronosticar una futura reincidencia. Al subir el dataset, se generará a la derecha
        una tabla con el resultado de la predicción. Este detaset debe cumplir las condiciones especificadas más adelante.
    """),
    dcc.Markdown("""
        El dataset debe estar en formato `csv` y contener las siguientes columnas, con una fila para cada individuo:

        * internoen: código del interno
        * genero: 'MASCULINO' o 'FEMENINO'
        * edad: edad en años
        * nivel_educativo: 'BACHILLERATO', 'PRIMARIA', 'BACHILLERATO INCOMPLETO', 'PRIMARIA INCOMPLETA', 'PROFESIONAL', 'ANALFABETA', 'TECNICO', 'POSTGRADO'
        * actividades: realizó actividades de estudio, enseñanza o trabajo (1, 0)
        * estado_ingreso: 'Intramuros', 'Prision Domiciliaria', 'Vigilancia Electronica', 'Detencion Domiciliaria', 'NINGUNO', 'Espera Traslado', 'Control Electronico'
        * hijos_menores: tiene hijos menores (1, 0)
        * total_reincidencias: número de reincidencias hasta ahora 
        * delito_moda: delito más cometido
        * total_delitos: total delitos cometidos hasta ahora
        * titulo_delito_moda: titulo donde ha cometido más delitos
        * max_gravedad: gravedad del delito más grave cometido (1, 2, 3, 4, 5) 
    """),
    html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arrastre o ',
                html.A('seleccione su dataset')
            ], className='upload_files'),
            # Allow multiple files to be uploaded
            multiple=True
        ),
        # dbc.Button("Clasificar", color="success", id='classif-button', block=True)
    ],)
])


# Callback para las pestañas de modelos
@app.callback(
    [Output("model-page", "children"),
    Output('model-aside', 'children'),
    Output('upload-aside', 'children')], 
    [Input("tabs", "active_tab")]   
    )
def switch_tab(at):
    if at == "kModes":
        return kModes.layout, kModes.aside, html.Div([])
    elif at == 'random-forest':
        return RF.layout, RF.aside, upload_file_ly
    else:
        return html.P("This shouldn't ever be displayed..."), html.Div('Que no')


# Para los desplegables donde se describen los grupos 
@app.callback(
    [Output(f"collapse-{i}", "is_open") for i in range(0, 3)],
    [Input(f"group-{i}-toggle", "n_clicks") for i in range(0, 3)],
    [State(f"collapse-{i}", "is_open") for i in range(0, 3)],
)
def toggle_accordion(n1, n2, n3, is_open1, is_open2, is_open3):
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "group-0-toggle" and n1:
        return not is_open1, False, False
    elif button_id == "group-1-toggle" and n2:
        return False, not is_open2, False
    elif button_id == "group-2-toggle" and n3:
        return False, False, not is_open3
    return False, False, False


def parse_contents(contents, filename, date, model, predict_model):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            df = predict_model(model, data=df)
            df = df[['internoen','Label', 'Score']]
            df['Label'].replace({1: 'Sí', 0: 'No'}, inplace=True)
            df.columns = ['Código Interno', '¿Reincidirá de nuevo?', 'Score']
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H3('DataSet clasificado'),
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])


from pycaret.classification import load_model, predict_model
@app.callback(Output('plot-new-dataset', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    model = load_model('random_forest')
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d, model, predict_model) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
    else:
        return ''

