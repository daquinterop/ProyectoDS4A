import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
import datasets as data
import graphs

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.css.append_css('styles.css')
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # Contenedor del segundo nivel
    html.Div([   
        # Header
        html.Header([
            html.Img(
                src='https://www.danielperico.com/images/ds4a.jpg',
                className='header_image'
            ),
            html.H1('Clasificación de la población reincidente en Colombia')
        ]),
        # Body
        html.Div([
            # Elemento Aside
            html.Aside([
                html.H3('Elementos interactivos'),
                # Dropdown
                html.Div([
                    html.H5('Dropdown bcc'),
                    dbc.DropdownMenu(
                        label="Seleccione el Dataset",
                        children=[
                            dbc.DropdownMenuItem("Dataset 1"),
                            dbc.DropdownMenuItem("Dataset 2"),
                            dbc.DropdownMenuItem("Dataset 3"),
                        ],
                        color="success"
                    ),
                ], className='interactive_container'),
                 # Botones
                html.Div([
                    html.H5('Seleccion el modelo (botones dbc)'),
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
                    html.H5('Slider dcc'),
                    dcc.Slider(
                        min=-5,
                        max=10,
                        step=0.5,
                        value=-3
                    ) 
                ], className='interactive_container'),
            ]),
            # Elementos del body
            html.Div([
                # Upload
                dcc.Upload(
                    id='upload-image',
                    children=html.Div([
                        'Arrastre o ',
                        html.A('seleccione su dataset')
                    ]),
                    style={
                        'max-width': 'iherit',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },
                    # Allow multiple files to be uploaded
                    multiple=True
                ),
                html.H3('Gráfico de prueba'),
                dcc.Graph(
                    id='main_graph',
                    figure=graphs.test_graph(data.iris),
                    className='graph'
                )
            ], id='page-content', className='page_content'),
        ], className='body')
        
    ], className='second_level')
    
], className='background')


# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/apps/app1':
#         return app1.layout
#     elif pathname == '/':
#         return dcc.Graph(graphs.test_graph(data.iris))
#     elif pathname == '/apps/app2':
#         return app2.layout
#     else:
#         return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
