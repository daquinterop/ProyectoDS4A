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
colombia_dptos_geo = datasets.colombia_dptos_geo
recidivism_index = datasets.recidivism_index

def xlabel_step_hist(xlabel):
    if 'pena' in xlabel:
        return 'Duración de la pena (años)'
    else:
        return 'Gravedad del delito (Mayor es más grave)'

delito_tab = html.Div([
    # Distribución delito por reincidencia
    dbc.Row([
        # Espacio para el gráfico
        dbc.Col([
            dcc.Graph(
                figure=graphs.step_hist(data, 'min_pena', 'num_reincidencia', [1, 2, 3], xlabel_step_hist),
                id='dist-penas',
                # className='figure'
            )
        ], width={'size': 8}, className='page_content'),
        dbc.Col([
            html.H3(["Gravedad del delito según el número de reincidencia"]),
            html.H6('Seleccione el indicador de gravedad del delito'),
            dcc.Dropdown(
                options=[
                    {'label': 'Pena mínima', 'value': 'min_pena'},
                    {'label': 'Pena media', 'value': 'avg_pena'},
                    {'label': 'Pena máxima', 'value': 'max_pena'},
                    # {'label': 'Gravedad del delito', 'value': 'gravedad_delito'}
                ],
                value='min_pena',
                id='dd-gravedad-delito'
            ),
            html.H6('Seleccione la reincidencia'),
            dcc.Dropdown(
                options=[
                    {'label': 'Primera', 'value': 1},
                    {'label': 'Segunda', 'value': 2},
                    {'label': 'Tercera', 'value': 3},
                    {'label': 'Cuarta', 'value': 4},
                    {'label': 'Quinta', 'value': 5},
                ],
                value=[1, 2, 3],
                multi=True,
                id='dd-reincidencia'
            ), 
            html.Br(),
            dcc.Markdown("""
                Los delitos más graves tienen castigos más severos, es decir, una mayor duración de la pena.
                El gráfico de la izquierda muestra la distribución acumulada de la duración de la pena (mínima,
                promedio y máxima) según el número de la reincidencia. Estas penas fueron obtenidas del código
                penal colombiano.

                En este gráfico, si la curva está por encima de otra, significa que la población que representa esa curva
                (primeros reincidentes, segundos reincidentes, etc.) en general tiene penas más cortas, es decir que 
                cometen delitos menos graves.

                El análisis demuestra que en general, a medida que continúan reincidiendo, normalmente cometen delitos
                que son "menos graves" (i.e. penas menos severas).
            """)
        ], width={'size': 4}, className='aside-element', align='center')
    ]),
    # Treemap Delito
    dbc.Row([
        dbc.Col([
            html.Div(className='div-line'),
            dcc.Graph(
                figure=graphs.delito_treemap(data, 1),
                id='treemap-delito',
                # className='figure'
            )
        ], width={'size': 8}, className='page_content'),
        dbc.Col([
            html.H3(["Delitos cometidos según la reincidencia"]),
            html.H6('Seleccione la reincidencia'),
            dcc.Dropdown(
                options=[
                    {'label': 'Primera', 'value': 1},
                    {'label': 'Segunda', 'value': 2},
                    {'label': 'Tercera', 'value': 3},
                    {'label': 'Cuarta', 'value': 4},
                    {'label': 'Quinta', 'value': 5},
                    {'label': 'Sexta', 'value': 6},
                ],
                value=1,
                id='dd-reincidencia-treemap'
            ),
            html.Br(),
            dcc.Markdown('''
                El gráfico treemap permite establecer la proporción del total en un grupo. En este caso, muestra
                la proporción de delitos cometidos dentro de una población que cometió una enésima reincidencia.
                El tamaño del cuadro es proporcional a la cantiadad de personas que cometieron ese delito. El color
                representa la gravedad del delito, donde azul son los menos graves, y rojo los más graves.

                Se evidencia que los delitos al patrimonio económico son los más cometidos, en especial, el hurto.
                A medida que reinciden, la proporción de hurto aumenta, y los delitos más graves disminuyen.
            ''')
        ], width={'size': 4}, className='aside-element', align='center')
    ]),
    dbc.Row([
        # Espacio para el gráfico
        dbc.Col([
            html.Div(className='div-line'),
            html.Embed(src=app.get_asset_url('chord1_2.html'),
                    height=900, width=900, id='chordplot')
        ], width={'size': 8}, className='page_content'),
        dbc.Col([
            html.H3(["Movimiento a través de diferentes delitos"]),
            html.H6('Seleccione el movimiento de reincidencias'),
            dcc.Dropdown(
                options=[
                    {'label': 'Primera a segunda', 'value': '1_2'},
                    {'label': 'Segunda a tercera', 'value': '2_3'},
                    {'label': 'Tercera a cuarta', 'value': '3_4'},
                    {'label': 'Cuarta a quinta', 'value': '4_5'},
                    {'label': 'Quinta a sexta', 'value': '5_6'},
                ],
                value='1_2',
                id='dd-chordplot'
            ),
            html.Br(),
            dcc.Markdown(["""
                La gráfica de cuerdas de la izquierda representa la evolución de la reincidencia individual. Cada cuerda 
                representa a un interno, y su tránsito de un delito a otro, de una reincidencia a la siguiente.

                Usando los 20 delitos más comunes dentro del dataset, el equipo de trabajo decidió graficar la evolución
                de la reincidencia individual. Del análisis previo se puede ver que la mayoría de los reincidentes 
                permanecieron reincidiendo en hurto durante toda su evolución de delitos. Esto puede ser debido al hecho
                de que hurto es uno de los delitos con el menor castigo, significando que los reincidentes pueden
                pagar su condena y volver a delinquir.
            """])
        ], width={'size': 4}, className='aside-element', align='center')
    ]),
])


edad_tab = html.Div([
    dbc.Row([
        # Espacio para el gráfico
        dbc.Col([
            dcc.Graph(id='edad_kde', figure=graphs.age_kde(data, [1]))
        ], width={'size': 8}, className='page_content'),
        dbc.Col([
            html.H3(["Distribución de la edad según el número de reincidencia"]),
            html.H6('Seleccione el número de la reincidencia'),
            dcc.Dropdown(
                options=[
                    {'label': 'Primera', 'value': 1},
                    {'label': 'Segunda', 'value': 2},
                    {'label': 'Tercera', 'value': 3},
                    {'label': 'Cuarta', 'value': 4},
                    {'label': 'Quinta', 'value': 5},
                    {'label': 'Sexta', 'value': 6},
                ],
                value=[1],
                id='dd-edad-reincidencia',
                multi=True  
            ),
            html.Br(),
            dcc.Markdown(["""
                No parece haber una diferencia sustancial en la edad para las diferentes reincidencias. La mayoría 
                de los reincidentes tienen edades entre los 20 y los 40 años.
            """])
        ], width={'size': 4}, className='aside-element', align='center')
    ],align='center'), 
    dbc.Row([
        # Espacio para el gráfico
        dbc.Col([
            dcc.Graph(id='edad_kde_bin', figure=graphs.age_kde_binary(data, 'genero'))
        ], width={'size': 8}, className='page_content'),
        dbc.Col([
            html.H3(["Distribución de la edad según categorías"]),
            html.H6('Seleccione la variable categórica'),
            dcc.Dropdown(
                options=[
                    {'label': 'Tentativa', 'value': 'tentativa'},
                    {'label': 'Agravado', 'value': 'agravado'},
                    {'label': 'Calificado', 'value': 'calificado'},
                    {'label': 'Género', 'value': 'genero'},
                    {'label': 'Actividades de trabajo', 'value': 'actividades_trabajo'},
                    {'label': 'Actividades de estudio', 'value': 'actividades_estudio'},
                    {'label': 'Actividades de enseñanza', 'value': 'actividades_enseñanza'},
                    {'label': 'Tiene hijos menores', 'value': 'hijos_menores'},
                ],
                value='genero',
                id='dd-edad-bin',
            ),
            html.Br(),
            dcc.Markdown(["""
                En este gráfico se puede observar la distribución de la edad teniendo en cuenta diferentes variables
                categóricas. Al revisar estas distribuciones, se aprecía alguna diferencia en la distribución cuando el
                delito es calificado, según el género, según si realizó o no actividades de enseñanza o según si tiene o no
                hijos menores.

                Según esto, en promedio las personas que cometen un delito calificado son más jóvenes que quienes no. Igualmente,
                en promedio los hombres reincidentes son más jóvenes que las mujeres reincidentes. En promedio, quienes realizan actividades
                de enseñanza son de mayor edad que quienes no la realizan. Finalmente, los reincidentes con hijos son en promedio de 
                mayor edad que los reincidentes sin hijos.
            """])
        ], width={'size': 4}, className='aside-element', align='center')
    ],align='center'), 
])


basic_tab = html.Div([
    dbc.Row([
        # Espacio para el gráfico
        dbc.Col([

        ], width={'size': 8}, className='page_content'),
        dbc.Col([
            html.Br(),
            dcc.Markdown(["""

            """])
        ], width={'size': 4}, className='aside-element', align='center')
    ], className='parent-row', align='center')
])

location_tab = html.Div([
    dbc.Row([
        # Espacio para el gráfico
        dbc.Col([
            html.Div([
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(
                            figure=graphs.recidivsm_map_plot(recidivism_index, colombia_dptos_geo, 'index'),
                            id='indexes-map',
                        )
                    ]),
                    dbc.Col([
                        dcc.Graph(
                            figure=graphs.recidivsm_scatter(recidivism_index, 'index'),
                            id='indexes-scatter',
                        )
                    ])
                ])
            ],)
        ], width={'size': 8}, className='page_content'),
        dbc.Col([
            html.H3(["Reincidencia estandarizada e indicadores de desarrollo humano"]),
            html.H6('Seleccione el indicador a mostar en el mapa'),
            dcc.Dropdown(
                options=[
                    {'label': 'Índice de reincidencia (reincidentes / 1M de habitantes)', 'value': 'index'},
                    {'label': 'Índice de desarrollo humano subnacional', 'value': 'shdi'},
                    {'label': 'Índice de salud', 'value': 'healthindex'},
                    {'label': 'Índice de educación', 'value': 'edindex'},
                    {'label': 'Expectativa de vida', 'value': 'lifexp'},
                    {'label': 'Años de escolaridad promedio', 'value': 'msch'},
                    {'label': 'Índice de ingreso', 'value': 'incindex'},
                ],
                value='index',
                id='dd-index'
            ),
            html.Br(),
            dcc.Markdown(["""
            De acuerdo con el lugar de origen manifestado por el reincidente, el número de reincidencias estandarizadas 
            fue calculado para cada departamento de Colombia. Para calcular este valor, se dividió el total de reincidentes
            diferentes sobre la población del departamento, obteniendo así el número de reincidentes por millón de habitantes.

            En el mapa de la izquierda se muestra el valor de la incidencia estandarizada para cada departamento. En el desplegable
            de arriba, se puede elegir el índice a mostrar, dentro de una lista de índices de desarrollo humano subnacionales. Se 
            evidencia que los departamentos de Caldas, Quindío, San Andrés y Providencia, Tolima y Caquetá, son quienes
            presentan las tasas de reincidentes más altas.

            En el diagrama de dispersión que acompaña al mapa, se puede establecer visualmente la correlación entre la tasa
            de reincidentes y el valor de los índices de desarrollo húmano. En todos estos índices, cuanto más alto el valor, mejor,
            caso contrario a la tasa de reincidentes calculada.

            El índice incindex muestra la correlación más significativa. Este índice hace referencia al ingreso per cápita 
            de cada departamento, siendo más alto en los departamentos donde en promedio una persona tiene un mayor ingreso. Esto sugiere,
            que la mayor tasa de reincidentes se presenta en departamentos más desarrollados según los lineamientos del índice de 
            desarrollo humano.
            """])
        ], width={'size': 4}, className='aside-element', align='center')
    ], className='parent-row', align='center')
])

eda_layout = html.Div([
    dbc.Row([ # Pestañas para la selección de factores
        dbc.Alert("Seleccione el factor de análisis", color="dark", fade=True, duration=5000),
        dbc.Col([
            dbc.Tabs([
                dbc.Tab([delito_tab], label="Por delito", tab_id='delito'),
                dbc.Tab([edad_tab], label="Por edad", tab_id='edad'),
                # dbc.Tab(label="Por educación", tab_id='educacion'),
                # dbc.Tab(label="Por establecimiento carcelario", tab_id='establecimiento'),
                dbc.Tab([location_tab], label="Por lugar de origen", tab_id='lugar'),
            ], id='tabs-eda', active_tab='delito')
        ], width={'size': 12})
    ]),
    # Contenido
    
])



@app.callback(Output('dist-penas', 'figure'),
              [Input('dd-gravedad-delito', 'value'),
              Input('dd-reincidencia', 'value')])
def plot_dist_penas(gravedad, reincidencia):
    return graphs.step_hist(data, gravedad, 'num_reincidencia', reincidencia, xlabel_step_hist)

@app.callback([Output('indexes-map', 'figure'),
               Output('indexes-scatter', 'figure')],
              [Input('dd-index', 'value'),
               Input('dd-index', 'label')])
def plot_recidivism_index(index, label):
    return (graphs.recidivsm_map_plot(recidivism_index, colombia_dptos_geo, index),
        graphs.recidivsm_scatter(recidivism_index, index, label))


@app.callback(Output('treemap-delito', 'figure'),
    [Input('dd-reincidencia-treemap', 'value')])
def treemap_delito(reincidencia):
    return graphs.delito_treemap(data, reincidencia)


@app.callback(Output('edad_kde', 'figure'),
    [Input('dd-edad-reincidencia', 'value')])
def kde_edad(reincidencia):
    return graphs.age_kde(data, reincidencia)


@app.callback(Output('edad_kde_bin', 'figure'),
    [Input('dd-edad-bin', 'value')])
def kde_edad_bin(column):
    return graphs.age_kde_binary(data, column)


@app.callback(Output('chordplot', 'src'),
    [Input('dd-chordplot', 'value')])
def chordplot(value):
    return app.get_asset_url(f'chord{value}.html')