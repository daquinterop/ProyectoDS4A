import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import datasets as data
import graphs
import lorem
from app import app

def make_item(i, cardtext):
    # Función para generar los items de los elementos colapsables
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2(
                    dbc.Button(
                        f"Cluster #{i}",
                        color="link",
                        id=f"group-{i}-toggle",
                    )
                )
            ),
            dbc.Collapse(
                dbc.CardBody(cardtext),
                id=f"collapse-{i}",
            ),
        ]
    )

# Clase para el modelo knn
class kModes:
    def __init__(self):
        self.name = 'K-Modes' # Nombre del algoritmo
        
        self.aside = html.Div([ # Elemento aside correspondiente a este modelo
            html.H3('Clustering'),
            dcc.Markdown('''
                Clustering es la agrupación de un set de objetos, de tal manera que los que estén en el mismo grupo (Cluster)
                son lo más similares entre sí a comparación con los otros grupos. Es una actividad exploratoria de datos, y una
                técnica estadística común para el análsis de datos.

                Un modelo de clustering fue usado para agrupar a la población reincidentes de acuerdo a algunas variables 
                seleccionadas, esto para obtener una caracterización de la población. Se utilizó el método de clustering K-modes,
                obteniendo seis clusters. Estos clusters pueden verse representados en la gráfica de la derecha, donde cada 
                eje representa uno de los tres componentes principales.
            '''),
            html.Div(className='div-line'),
            html.H3('K-Modes'),
            dcc.Markdown('''
                K-Modes es un método de clustering utilizado para variables categóricas. Este método define clusters basado en el 
                número de categorías coincidentes entre los diferentes puntos del Dataset. Este método es alternativo al mucho más 
                conocido método de K-Means, que es utilizado para información numérica tomando como base la distancia euclidiana.
            '''),
            html.Div(className='div-line'),
            html.H3('Resultados'),
            dcc.Markdown('''
                Según la estructura de los datos, se determinó que lo óptimo es definir seis clusters. Las carácterísticas de cada
                cluster definido se encuentran en los desplegables bajo la gráfica.
            ''')

        ], className='aside')
        
        self.layout = html.Div([ # Contenido de la página para este modelo
            html.Div([
                html.H3('Clasificación propuesta utilizando K-Modes'),
                html.Embed(
                    src=app.get_asset_url('clustering.html'),
                    height=900, width=900
                ),
            ],),
            html.Div([
                html.H3(['Se identificaron los siguientes seis clusters con las siguientes características:']),
                html.Div([
                    make_item(
                        0, 
                        dcc.Markdown("""
                        Los individuos del Cluster 0 comparten las siguientes características:

                        * Entre 28 y 32 años de edad
                        * Completaron la primaria
                        * Realizaron actividades (educación, trabajo o enseñanza) durante la reclusión
                        * En estado intramuros al momento del ingreso
                        * Tienen hijos menores
                        * Han reincidido solo una vez
                        * El Hurto es el delito que más cometen
                        * Han cometido solo un delito
                        * Los delitos contra el patrimonio económico son los que más cometen
                        * En una escala de donde 1 es el delito menos grave, y 5 el más grave, la máxima gravedad es 2
                        """)
                    ), 
                    make_item(
                        1,
                        dcc.Markdown("""
                        Los individuos del Cluster 1 comparten las siguientes características:

                        * Entre 35 y 36 años de edad
                        * Completaron la primaria
                        * Realizaron actividades (educación, trabajo o enseñanza) durante la reclusión
                        * En estado intramuros al momento del ingreso
                        * Tienen hijos menores
                        * Han reincidido solo una vez
                        * El Tráfico, fabricación o porte de estupefacientes es el delito que más cometen
                        * Han cometido solo un delito
                        * Los delitos contra la salud pública los que más cometen
                        * En una escala de donde 1 es el delito menos grave, y 5 el más grave, la máxima gravedad es 4
                        """)
                    ),
                    make_item(
                        2,
                        dcc.Markdown("""
                        Los individuos del Cluster 2 comparten las siguientes características:

                        * Entre 33 y 37 años de edad
                        * Completaron la primaria
                        * Realizaron actividades (educación, trabajo o enseñanza) durante la reclusión
                        * En estado intramuros al momento del ingreso
                        * Tienen hijos menores
                        * Han reincidido solo una vez
                        * La fabricación, tráfico y porte de armas de fuego o municiones es el delito que más cometen
                        * Han cometido dos delitos
                        * Los delitos contra la seguridad pública son los que más cometen
                        * En una escala de donde 1 es el delito menos grave, y 5 el más grave, la máxima gravedad es 5
                        """)
                    ),
                    make_item(
                        3,
                        dcc.Markdown("""
                        Los individuos del Cluster 3 comparten las siguientes características:

                        * Entre 28 y 30 años de edad
                        * Completaron la primaria
                        * Realizaron actividades (educación, trabajo o enseñanza) durante la reclusión
                        * En estado intramuros al momento del ingreso
                        * Tienen hijos menores
                        * Han reincidido dos veces
                        * El hurto es el delito que más cometen
                        * Han cometido dos delitos
                        * Los delitos contra el patrimonio económico son los que más cometen.
                        * En una escala de donde 1 es el delito menos grave, y 5 el más grave, la máxima gravedad es 2
                        """)
                    ),
                    make_item(
                        4,
                        dcc.Markdown("""
                        Los individuos del Cluster 4 comparten las siguientes características:

                        * Entre 28 y 38 años de edad
                        * Completaron la primaria
                        * No realizaron actividades (educación, trabajo o enseñanza) durante la reclusión
                        * En estado prisión domiciliaria al momento del ingreso
                        * Tienen hijos menores
                        * Han reincidido una vez
                        * La fabricación, tráfico y porte de armas de fuego o municiones es el delito que más cometen
                        * Han cometido un delito
                        * Los delitos contra el patrimonio económico son los que más cometen.
                        * En una escala de donde 1 es el delito menos grave, y 5 el más grave, la máxima gravedad es 5
                        """)
                    ),
                    make_item(
                        5,
                        dcc.Markdown("""
                        Los individuos del Cluster 5 comparten las siguientes características:

                        * Entre 32 y 37 años de edad
                        * Completaron la primaria
                        * Sí realizaron actividades (educación, trabajo o enseñanza) durante la reclusión
                        * En estado intramuros al momento del ingreso
                        * Tienen hijos menores
                        * Han reincidido una vez
                        * El homicidio es el delito que más cometen
                        * Han cometido un delito
                        * Los delitos contra la seguridad pública.
                        * En una escala de donde 1 es el delito menos grave, y 5 el más grave, la máxima gravedad es 5
                        """)
                    )
                ], className="accordion")
            ], className='content_box', style={'text-align': 'left'})
        ])

    
class RF:
    def __init__(self):
        self.name = 'Random-Forest' # Nombre del algoritmo
        
        self.aside = html.Div([ # Elemento aside correspondiente a este modelo
            html.H3('Clasificación binaria'),
            dcc.Markdown('''
                La clasificación bianria es una técnica de aprendizaje supervisado donde el objetivo es predecir una variable
                categórica que es discreta y no ordenada, como por ejemplo Sí/No, Aprobó/Falló, etc.

                Este modelo es usado para identificar si los presos reincidentes tienen o no proababilidad de volver a hacerlo según sus
                características. Este análsis es hecho entrenando un modelo con las caracterísiticas que normalmente presentan los 
                internos que han reincidido más de una vez. Para hacer esta clasificación se seleccionó el algoritmo Random Forest,
                que fue implementado usando la librería [PyCaret](https://pycaret.org/). Se obtivieron los resultados demostrados en las 
                gráficas de la derecha.

            '''),
            html.Div(className='div-line'),
            html.H3('Random Forest'),
            dcc.Markdown('''
                Los bosques aleatorios (Random Forest) son una combinación de árboles predictores tal que cada árbol depende de los 
                valores de un vector aleatorio probado independientemente, y que comparte la misma distribución entre cada árbol.
                Un árbol de desiciones es simplemente una herramienta para llegar a un valor luego de la validación de la ocurrrencia
                o no de ciertas condiciones específicas. Un bosque aleatorio combina muchos árboles de decisiones, y entrega la desición
                de la mayoría de estos.
            '''),
            html.Div(className='div-line'),
            html.H3('Resultados'),
            dcc.Markdown('''
                Al evaluar el modelo, se obtuvo una presición del 0.9251, y un área bajo la curva (AUC) de 0.9806. Como referencia,
                obtener un valor de 1 en estas dos métricas siginifica que el modelo clasifica perfectamente todos los datos
                evaluados. Por otro lado, unna presición de 0.5 equipara lel modelo a una decisión aleatoria.

                En conclusión, según la validación del modelo, al momento de clasificar si un reincidente lo volverá a hacer,
                el modelo acertará en su estimación en 9 de cada 10 internos.
            '''),
            html.Div(className='div-line'),
            
        ], className='aside')
        
        self.layout = html.Div([ # Contenido de la página para este modelo
            html.Div([
                html.H3('Clasificación binaria de la población reincidente'),
                html.H5('Curva ROC'),
                dcc.Markdown('''
                    La curva ROC representa la sensibilidad de un clasificador binario frente al umbral de clasificación.
                    Esta curva representa la razón de verdadros positivos frente a la razión de falsos positivos. Cuanto mayor
                    sea el área bajo la curva, es mejor el clasificador.
                '''),
                html.Img(
                    src=app.get_asset_url('AUC.png'),
                    # height=900, width=900
                ),
                html.Br(),
                html.H5('Matriz de confusión'),
                dcc.Markdown('''
                    La matriz de confusión representa la presición del modelo de clasificación. En el caso de un clasificador
                    binario, la matriz de confusión muestra en su primer cuadrante la cantidad de verdaderos negativos, en el segundo
                    cuadrante la cantidad de falsos positivos, en el tercer cuadrante los verdaderos positivos, y en el último los
                    falsos negativos. En cuanto mayores sean las diagonales de la matriz, en relación con el resto de la matriz, es mejor
                    el clasificador.
                '''),
                html.Img(
                    src=app.get_asset_url('Confusion Matrix.png'),
                    # height=900, width=900
                ),
            ],),

        ])
