import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import datasets as data
import graphs
import modelsObjects
from app import app

knn = modelsObjects.knn()

models_layout = html.Div([
    dbc.Row([ # Pestañas para la selección de modelos
        dbc.Col([
            dbc.Tabs([
                dbc.Tab(label="KNN", tab_id='knn'),
                dbc.Tab(label="Random Forest", tab_id='random-forest'),
                dbc.Tab(label="Naive Bayes", tab_id='naive-bayes'),
                dbc.Tab(label="Modelo 4", tab_id='modelo4'),
                dbc.Tab(
                    "This tab's content is never seen", label="Modelo oculto", disabled=True
                )
            ], id='tabs', active_tab='knn')
        ], width={'size': 12})
    ]),
    # Contenido
    dbc.Row([
        # Elemento Aside, lo que está en la parte izquierda la página
        dbc.Col([
            # Elemento aside del modelo
            html.Div(id='model-aside', className='interactive_container'),
            # Elemento para subir el dataset
            html.H5('Suba su Dataset para ser clasificado'),
            dcc.Markdown("""
                El dataset debe estar en formato `csv` y contener las siguientes columnas, con una fila para cada individuo:

                * Columna 1
                * Columna 2
                * Columna 3
            """),
            html.Div([
                dcc.Upload(
                    id='upload-image',
                    children=html.Div([
                        'Arrastre o ',
                        html.A('seleccione su dataset')
                    ], className='upload_files'),
                    # Allow multiple files to be uploaded
                    multiple=False
                ),
                dbc.Button("Clasificar", color="success", id='classif-button', block=True)
            ], className='interactive_container')
        ], width={'size': 4},className='aside-element'),

        # Contenido principal de la página
        dbc.Col([
            # Contenido del modelo, gráfico, descripción y grupos encontrados
            html.Div(id='model-page'),
            # Plot del dataset ya clasificado.
            html.Span(id='plot-new-dataset')
        ], width={'size': 8}, className='page_content')
    ])
])

# Callback para las pestañas de modelos
@app.callback(
    [Output("model-page", "children"),
    Output('model-aside', 'children')], 
    [Input("tabs", "active_tab")]   
    )
def switch_tab(at):
    if at == "knn":
        return knn.layout, knn.aside
    elif at == 'random-forest':
        return html.Div("Random Forest"), html.Div('Que no')
    else:
        return html.P("This shouldn't ever be displayed..."), html.Div('Que no')


# Para los desplegables donde se describen los grupos 
@app.callback(
    [Output(f"collapse-{i}", "is_open") for i in range(1, 4)],
    [Input(f"group-{i}-toggle", "n_clicks") for i in range(1, 4)],
    [State(f"collapse-{i}", "is_open") for i in range(1, 4)],
)
def toggle_accordion(n1, n2, n3, is_open1, is_open2, is_open3):
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "group-1-toggle" and n1:
        return not is_open1, False, False
    elif button_id == "group-2-toggle" and n2:
        return False, not is_open2, False
    elif button_id == "group-3-toggle" and n3:
        return False, False, not is_open3
    return False, False, False

# Para el plot del dateset que entran
@app.callback(
    [Output('plot-new-dataset', 'children')],
    [Input('classif-button', "n_clicks")]
)
def on_button_click(n):
    if n is None:
        return ['']
    else:
        return [dcc.Graph(children=graphs.test_graph(data.iris) ,id='plot2')]