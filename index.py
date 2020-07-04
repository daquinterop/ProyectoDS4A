import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
import datasets as data
import graphs

# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.css.append_css('styles.css')
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # Contenedor del segundo nivel
    html.Div([
        dbc.Row(
            dbc.Col(
                # Header
                html.Header([
                    html.Img(
                        src='https://www.danielperico.com/images/ds4a.jpg',
                        className='header_image'
                    ),
                    html.H1('Clasificación de la población reincidente en Colombia')
                ]),
            )
        ),
        
        # Body
        dbc.Row([
            dbc.Col([
                # Elemento Aside
                html.Aside([
                    # Dropdown
                    html.Div([
                        html.H5('Filtre el Dataset según el grupo de delitos'),
                        dcc.Dropdown(
                            id='demo-dropdown',
                            options=[
                                {'label': 'Contra el patrimonio económico', 'value': 'NYC'},
                                {'label': 'Contra la integridad', 'value': 'MTL'},
                                {'label': 'Contra la salud púlbica', 'value': 'SF'}
                            ],
                            value='NYC'
                        ),
                    ], className='interactive_container'),
                    # Botones
                    html.Div([
                        html.H5('Seleccione el modelo de clasificación'),
                        dbc.ButtonGroup(
                            [
                                dbc.Button("KNN", color="success"),
                                dbc.Button("Random Forest", color="success"),
                                dbc.Button("Naive - Bayes", color="success"),
                                dbc.Button("Hierarquical", color="success"),
                            ],
                            vertical=True,
                        )
                    ], className='interactive_container'),
                    # Slider
                    html.Div([
                        html.H5('Tamaño de la muestra aleatoria'),
                        dcc.Slider(
                            min=1,
                            max=5,
                            marks={i: f'{10**i}' for i in [1, 2, 3, 4, 5]},
                            value=3,
                        )  
                    ], className='interactive_container'),
                    html.Div([
                        html.H5('Ajuste de parámetros del modelo'),
                        html.H6(['Número de vecinos'], style={'margin-top': '15px'}),
                        dcc.Input(
                            id="dtrue", type="number",
                            debounce=True, placeholder="Número de vecinos",
                        ),
                        html.H6(['Peso'], style={'margin-top': '15px'}),
                        dcc.Dropdown(
                            options=[
                                {'value': 'uniform', 'label': 'uniform'},
                                {'value': 'distance', 'label': 'distance'},
                            ],
                            value='MTL',
                            placeholder="Peso"
                        ),
                        html.H6(['Algoritmo'], style={'margin-top': '15px'}),
                        dcc.Dropdown(
                            options=[
                                {'value': 'auto', 'label': 'auto'},
                                {'value': 'ball_tree', 'label': 'ball_tree'},
                                {'value': 'kd_tree', 'label': 'kd_tree'},
                                {'value': 'brute', 'label': 'brute'},
                            ],
                            value='MTL',
                            placeholder="Algoritmo"
                        ) 
                    ], className='interactive_container'),
                    html.Div([
                        dbc.Button("Entrenar el modelo", color="warning"),
                    ], className='interactive_container')
                ]),
            ], width={'size': 3,}),
            dbc.Col([
                html.Div([
                    html.Div([
                        dcc.Upload(
                            id='upload-image',
                            children=html.Div([
                                'Arrastre o ',
                                html.A('seleccione su dataset')
                            ], className='upload_files'),
                            # Allow multiple files to be uploaded
                            multiple=False
                        )
                    ]),
                    html.Div([
                        html.H3('Clasificación propuesta'),
                        dcc.Graph(
                            id='main_graph',
                            figure=graphs.test_graph(data.iris),
                            className='graph'
                        ),
                    ], className='content_box'),
                    html.Div([
                        html.H3(['Se identificaron los siguientes grupos con las siguientes características:']),
                        dbc.ListGroup([
                            dbc.ListGroupItem([
                                dbc.ListGroupItemHeading('Grupo 1'),
                                dbc.ListGroupItemText([graphs.table])
                            ]),
                            dbc.ListGroupItem([
                                dbc.ListGroupItemHeading('Grupo 2'),
                                dbc.ListGroupItemText([graphs.table])
                            ]),
                            dbc.ListGroupItem([
                                dbc.ListGroupItemHeading('Grupo 3'),
                                dbc.ListGroupItemText([graphs.table])
                            ])
                        ])
                        
                    ], className='content_box')
                ], className='page_content'),
            ], width={'size': 9},)
        ])
    ], className='second_level')
    
], className='background')

if __name__ == '__main__':
    app.run_server(debug=True)
