import plotly.express as px
import datasets as data
import dash_bootstrap_components as dbc

def test_graph(iris):
    fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
    return fig

table = dbc.Table.from_dataframe(data.df, striped=True, bordered=True, hover=True)