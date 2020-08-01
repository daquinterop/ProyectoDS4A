import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app

team65_layout = html.Div([
    dbc.Row([
        html.Br(),
        dbc.Col([
            html.H4('''
            Este trabajo fue desarrollado por un equipo multidiciplinario de 6 integrantes durante el transcurso del 
            curso Data Science for All, gracias a una beca otorgada por el Ministerio de Tecnologías de la Información y Comunicaciones, y a la información
            entregada por el Ministerio de Justicia y del Derecho.
            ''')
        ], width={'size': 8, 'offset': 2})
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Img(src=app.get_asset_url('Daniel.png'), width=200)
        ], width={'size': 2, 'offset': 2}, align='center'),
        dbc.Col([
            dcc.Markdown(""" 
            ## [Daniel Enrique Cerón Satizábal](https://www.linkedin.com/in/danielceron/)
            Ingeniero electrónico graduado de la Universidad Javeriana Cali. He tenido experiencia en el área de las 
            telecomunicaciones y automatización de procesos industriales, no obstante, en el último año he tenido gran 
            interés en temas como machine learning y esa motivación me condujo a estudiar y profundizar en el área de 
            ciencia de datos. Actualmente soy estudiante y perteneciente al equipo 65 del curso DS4A por Correlation 
            One patrocinado por MinTic.
            """)
        ], width={'size': 6}, align='center')
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            ## [Diego Andrés Quintero Puentes](https://www.linkedin.com/in/diego-quintero-341567141/)

            Ingeniero Agrícola graduado de la Universidad Nacional, con maestría en Meteorología de la misma universidad. Dos años 
            de experiencia en procesamiento y análisis de datos, enfocado en información agrometeorológica y productos derivados 
            de modelos de predicción numérica del tiempo. Actualmente es investigador en el área de ciencia de datos y meteorología
            en la Federación Nacional de Arroceros.
            ''')
        ], width={'size': 6, 'offset': 2}, align='center'),
        dbc.Col([
            html.Img(src=app.get_asset_url('Diego.png'), width=200)
        ], width={'size': 2}, align='center')
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Img(src=app.get_asset_url('Emiliano.png'), width=200)
        ], width={'size': 2, 'offset': 2}, align='center'),
        dbc.Col([
            dcc.Markdown('''
            ## [Emiliano Rodríguez Arango](https://www.linkedin.com/in/emiliano-rodr%C3%ADguez-b832351a8/)
            Maestría en Ciencias Estadísticas Universidad Nacional de Colombia-Bogotá.
            Especialización en Estadística Universidad Nacional de Colombia-Bogotá.
            Licenciado en Matemáticas Universidad de Sucre-Sincelejo.
            Experiencia en Docencia en  Universidad, en cursos de Probabilidad, Estadísticas, Diseños de Experimentos y Modelos.
            Experiencia en Empresas(consultorías), como analista de datos.
            ''')
        ], width={'size': 6}, align='center')
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            ## [Jonathan Nayid Orozco Bohorquez](https://www.linkedin.com/in/jnayid/)
            Ingeniero Electrónico graduado de la Universidad de los Andes, con especialización en Finanzas Corporativas del CESA 
            y un Global MBA de EDHEC Business School (Francia). Emprendedor con más de 8 años de experiencia en análisis de negocios. 
            Actualmente me desempeño como Director de Desarrollo de Negocios en una empresa de consultoría en servicios de ingeniería. 
            ''')
        ], width={'size': 6, 'offset': 2}, align='center'),
        dbc.Col([
            html.Img(src=app.get_asset_url('Nayid.png'), width=200)
        ], width={'size': 2}, align='center')
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Img(src=app.get_asset_url('Jorge.png'), width=200)
        ], width={'size': 2, 'offset': 2}, align='center'),
        dbc.Col([
            dcc.Markdown('''
            ## [Jorge Armando Millán Gómez](https://www.linkedin.com/in/jorge-millan-043954129/)
            Especialista en Ingeniería de Software, Ingeniero en control y profesional graduado en Tecnología en electrónica 
            de la Universidad Distrital "Francisco José de Caldas" con la capacidad de diseñar y desarrollar aplicaciones que 
            involucren sistemas electrónicos, plantear proyectos de investigación y desarrollo tecnológico, plantear proyectos 
            de investigación científica con base tecnológica , organizar, participar en equipos multidisciplinarios que tengan 
            como objetivo plantear, desarrollar y ejecutar soluciones tecnológicas. Comprender y aplicar sistemas electrónicos 
            enfocados al análisis y el diseño de circuitos computacionales, de control y comunicaciones que conforman sistemas 
            de instrumentación, proponer soluciones en el campo TI/SI según requerimientos empresariales, de la región, estado 
            o país. Así como también poseo grandes habilidades y competencias en Ingeniería de Software con base en diversos 
            lenguajes de programación, con conocimiento en el diseño, arquitectura empresarial, desarrollo de software y 
            administración de bases de datos. Tengo 5 años de experiencia en el campo TI/SI y actualmente soy líder técnico 
            del área de desarrollo de aplicaciones de software en Claro Colombia.

            ''')
        ], width={'size': 6}, align='center')
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            ## [Mauricio Stefan Cerpa Hernández](https://www.linkedin.com/in/mauricio-cerpa-hern%C3%A1ndez-808528199/)
            Matemático graduado de la Universidad del Norte, con maestría en Matemáticas en la misma universidad. 
            Tengo experiencia en el campo de la docencia desde el 2015.
            ''')
        ], width={'size': 6, 'offset': 2}, align='center'),
        dbc.Col([
            html.Img(src=app.get_asset_url('Mauricio.png'), width=200)
        ], width={'size': 2}, align='center')
    ]),
])