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
        )
    )
    return fig

table = dbc.Table.from_dataframe(data.df, striped=True, bordered=True, hover=True)