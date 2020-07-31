import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import figure_factory as ff
import datasets as data
import dash_bootstrap_components as dbc
import json
import plotly.io as pio
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

def test_graph(iris):
    fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
    return fig

def load_json_figure(json_path):
    with open(json_path, 'r') as f:
        json_figure = json.load(f)
    return pio.from_json(json.dumps(json_figure))


def plot_kde(data, column, filter_column, filter_values):
    if 'pena' in column:
        x_label = 'Duración de la pena (años)'
    else:
        x_label = 'Gravedad del delito (Mayor es más grave)'
    data_list = []
    label = []
    for value in filter_values:
        data_tmp = data.loc[data[filter_column] == value, column].values
        data_list.append(data_tmp[~np.isnan(data_tmp)])
        label.append(value)
    fig = ff.create_distplot(data_list, label, show_hist=False, show_rug=False)
    fig.update_layout(
        margin=go.layout.Margin(
            l=80, #left margin
            r=80, #right margin
            b=30, #bottom margin
            t=30  #top margin
        ),
        xaxis_title=x_label
    )
    return fig


def step_hist(data, column, filter_column, filter_values, xlabel_function):
    traces = []
    x_max = data[column].max()
    for value in filter_values:
        x = data.loc[(data[filter_column] == value) & (~data[column].isna()), column]
        x = list(x)
        x += [0, x_max]
        binned = np.histogram(x, bins=25, density=True)
        plot_y = np.cumsum(binned[0])

        # Line
        traces.append(go.Scatter(
            x=binned[1],
            y=plot_y,
            mode='lines',
            name=value,
            hoverinfo='all',
            )
        )
    layout = dict(
        legend=dict(
            y=0.5,
            traceorder='reversed',
            font=dict(
                size=16
            ),
        ),
        xaxis=dict(title=xlabel_function(column))
    )
    # Make figure
    fig = go.Figure(data=traces, layout=layout)
    return fig



def recidivsm_map_plot(recidivism_index, geojson, index):
    if index != 'index':
        color_scale = 'RdYlGn'
    else:
        color_scale = 'RdYlGn_r'
    fig = px.choropleth_mapbox(recidivism_index, geojson=geojson, locations=recidivism_index.index, color=index,
                    color_continuous_scale=color_scale, center={'lon': -73, 'lat': 4}, zoom=4.5,
                    mapbox_style="open-street-map", opacity=0.7, height=500)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig


def recidivsm_scatter(recidivism_index, index, variable_desc=''):
    labels = {'index': 'Índice de reincidencia (reincidentes / 1M de habitantes)',
        'shdi': 'Índice de desarrollo humano subnacional',
        'healthindex': 'Índice de salud',
        'edindex': 'Índice de educación', 
        'lifexp': 'Expectativa de vida', 
        'msch': 'Años de escolaridad promedio',
        'incindex': 'Índice de ingreso'
    }
    fig = px.scatter(
        recidivism_index, y='index', x=index,
        labels={
                "index": "Reincidentes por 1M de habitantes",
                index: labels[index],
            },
        title=f'Correlación: {recidivism_index.corr()["index"][index]:.3f}',
        height=500
    )
    return fig


def delito_treemap(data, reincidencia):
    hierarquical_df = (
        data[data['num_reincidencia'] == reincidencia]
        .groupby(['titulo_delito', 'delito'])
        .agg({'subtitulo_delito': 'count', 'min_pena': 'mean'})
        .reset_index()
    )
    hierarquical_df['count'] = 100 * hierarquical_df.subtitulo_delito / hierarquical_df.subtitulo_delito.sum()
    hierarquical_df = hierarquical_df.drop(columns='subtitulo_delito')
    hierarquical_df['total'] = 'total'

    fig = px.treemap(hierarquical_df, path=['total', 'titulo_delito', 'delito'], values='count',
                    color='min_pena', hover_data=['delito'],
                    color_continuous_scale='RdYlBu_r', range_color=(0, 30)
                    )
    return fig


def age_kde(data, filter_values):
    column = 'edad'
    filter_column='num_reincidencia'
    data_list = []
    label = []
    for value in filter_values:
        data_tmp = data.loc[data[filter_column] == value, column].values
        data_list.append(data_tmp[~np.isnan(data_tmp)])
        label.append(value)
    fig = ff.create_distplot(data_list, label, show_hist=False, show_rug=False)
    fig.update_layout(
        margin=go.layout.Margin(
            l=80, #left margin
            r=80, #right margin
            b=30, #bottom margin
            t=30  #top margin
        ),
        xaxis_title='Edad',
        height=600
    )
    return fig


def age_kde_binary(data, filter_column):
    si_no = {0:'No', 1:'Sí'}
    column = 'edad'
    data_list = []
    label = []
    for value in data[filter_column].unique():
        data_tmp = data.loc[data[filter_column] == value, column].values
        data_list.append(data_tmp[~np.isnan(data_tmp)])
        if not isinstance(value, str):
            label.append(si_no.get(value, str(value)))
        else:
            label.append(value)
    fig = ff.create_distplot(data_list, label, show_hist=False, show_rug=False)
    fig.update_layout(
        margin=go.layout.Margin(
            l=80, #left margin
            r=80, #right margin
            b=30, #bottom margin
            t=30  #top margin
        ),
        xaxis_title='Edad',
        legend={'title': filter_column},
        height=600
    )
    return fig


table = dbc.Table.from_dataframe(data.df, striped=True, bordered=True, hover=True)