import plotly.express as px
import datasets as data
import dash_bootstrap_components as dbc
import json
import plotly.io as pio

def test_graph(iris):
    fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
    return fig

def load_json_figure(json_path):
    with open(json_path, 'r') as f:
        json_figure = json.load(f)
    return pio.from_json(json.dumps(json_figure))

table = dbc.Table.from_dataframe(data.df, striped=True, bordered=True, hover=True)