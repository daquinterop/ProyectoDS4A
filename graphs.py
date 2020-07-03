import plotly.express as px
import datasets as data

def test_graph(iris):
    fig = px.scatter(iris, x="sepal_width", y="sepal_length")
    fig["layout"].update(paper_bgcolor="rgb(255, 255, 255, 0.1)", plot_bgcolor='rgb(255, 255, 255, 0.1)')
    fig.update_traces(
        marker=dict(
            size=12,
            line=dict(width=2,
            color='DarkSlateGrey'))  
    )
    fig.update_traces(textposition='top center')

    fig.update_layout(
        yaxis=dict(color='black'),
        xaxis=dict(color='black')
    )
    return fig