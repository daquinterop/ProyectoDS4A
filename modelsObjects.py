import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import datasets as data
import graphs
import lorem

def make_item(i):
    # Función para generar los items de los elementos colapsables
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2(
                    dbc.Button(
                        f"Grupo #{i}",
                        color="link",
                        id=f"group-{i}-toggle",
                    )
                )
            ),
            dbc.Collapse(
                dbc.CardBody(f"Descripción del grupo {i}..."),
                id=f"collapse-{i}",
            ),
        ]
    )

# Clase para el modelo knn
class knn:
    def __init__(self):
        self.name = 'K-Nearest Neighbours' # Nombre del algoritmo
        self.plot = graphs.test_graph(data.iris) # Gráfica
        self.table = graphs.table # Tabla
        
        self.aside = html.Div([ # Elemento aside correspondiente a este modelo
            html.H3('Espacio para la explicación de los gráficos'),
            dcc.Markdown(lorem.paragraph()),
            html.H4(lorem.sentence()),
            dcc.Markdown(lorem.paragraph()),
            html.P(lorem.paragraph()),
            html.H4(lorem.sentence()),
            html.P(lorem.paragraph())
        ], className='aside')
        
        self.layout = html.Div([ # Contenido de la página para este modelo
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

    
        
        