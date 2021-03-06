import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
import datasets as data
import graphs
from apps.models import models_layout
from apps.eda import eda_layout
from apps.team65 import team65_layout

# Definición del layout, es decir, la página en sí
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), # Permite actualizar el url y cambiar entre páginas
    dbc.Row([
        dbc.Col(
            dbc.NavbarSimple([ # Barra de navegación
                dbc.Row([
                    dbc.Col(dbc.NavItem(dbc.NavLink("EDA", href="/eda")), ),
                    dbc.Col(dbc.NavItem(dbc.NavLink("Modelos", href="/models")), ),
                    dbc.Col(dbc.NavItem(dbc.NavLink("Team65", href="/team65")),),
                    # dbc.Col(dbc.NavItem(dbc.NavLink("Acerca del problema", href="/about")), ),
                ], no_gutters=True)],
                color="dark",
                dark=True,
                brand="Caracterización de la población reincidente en Colombia",
                brand_href="/",
                # fixed='top'
            ),
        width={'size': 12, "offset": 0}),
    ]),
    dbc.Row([
        dbc.Col(
            html.Div(id='page-content'),
            width={'size': 10, 'offset': 1},
        )
    ])

], className='background')

server = app.server

# Callback para el cambio de página en la barra de navegación
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/models':
        return models_layout
    # elif pathname == '/about':
    #     return html.Div('Contenido de acerca')
    elif pathname == '/team65':
        return team65_layout
    elif (pathname == '/') or (pathname == '/eda'):
        return eda_layout
    else:
        return html.Div([html.H1('Error hijueputa!!')])

if __name__ == '__main__':
    app.run_server(debug=True)
