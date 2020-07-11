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
            html.H3('Características del modelo'),
            dcc.Markdown("""
                ***Descripción***: El método de los k vecinos más cercanos ​ es un método de
                clasificación supervisada que sirve para estimar la función de densidad 
                de las predictoras por cada clase.
            """),
            html.H5('Parámetros del modelo'),
            dcc.Markdown("""
                ~~~python
                Parámetro_1: valor_del_parámetro_1.
                Parámetro_2: valor_del_parámetro_2.
                Parámetro_3: valor_del_parámetro_3.
                Parámetro_4: valor_del_parámetro_4.
                Parámetro_5: valor_del_parámetro_5.
            """),
            html.H5('Supuestos del modelo'),
            dcc.Markdown("""
                * Supuesto 1
                * Supuesto 2
                * Supuesto 3
            """),
            html.H5('Métricas de evaluación del modelo'),
            dcc.Markdown("""
                * Métrica 1 = Valor 1
                * Métrica 2 = Valor 2
                * Métrica 3 = Valor 3 
            """)
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

    
        
        