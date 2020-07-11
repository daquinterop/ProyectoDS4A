import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import datasets as data
import graphs

def make_item(i):
    # Función para generar los items de los elementos colapsables
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2(
                    dbc.Button(
                        f"Collapsible group #{i}",
                        color="link",
                        id=f"group-{i}-toggle",
                    )
                )
            ),
            dbc.Collapse(
                dbc.CardBody(f"This is the content of group {i}..."),
                id=f"collapse-{i}",
            ),
        ]
    )

# Clase para el modelo knn
class knn:
    def __init__(self):
        self.name = 'K-Nearest Neighbours'
        self.plot = graphs.test_graph(data.iris)
        self.table = graphs.table
        
        self.aside = html.Div([
            html.H3('Características del modelo'),
            dcc.Slider(
                min=1,
                max=5,
                marks={i: f'{10**i}' for i in [1, 2, 3, 4, 5]},
                value=3,
            )  
        ], className='aside')
        
        self.layout = html.Div([
            html.Div([
                html.H3('Clasificación propuesta'),
                dcc.Graph(
                    id='main_graph',
                    figure=self.plot,
                    className='graph'
                ),
            ],),
            html.Div([
                html.H3(['Se identificaron los siguientes grupos con las siguientes características:']),
                html.Div(
                    [make_item(1), make_item(2), make_item(3)], className="accordion"
                )
            ], className='content_box')
        ])

    
        
        