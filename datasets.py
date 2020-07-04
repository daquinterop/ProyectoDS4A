import plotly.express as px
import pandas as pd
iris = px.data.iris() # iris is a pandas DataFrame

df = pd.DataFrame(
    {
        "" : ['Promedio', 'Desviación'],
        "Variable 1": [3, 2],
        "Variable 2": [2, 3],
        "Variabñe 3": [4, 4],
        "Variable 4": [4, 5],
    },
)

