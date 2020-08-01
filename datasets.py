import plotly.express as px
import pandas as pd
import json 

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

data = pd.read_pickle('DataFrame_4.pkl')

with open('dptos_colombia.json') as json_file:
    colombia_dptos_geo = json.load(json_file)

# Data de reincidentes
recidivism_index = data.groupby('departamento_corregido').agg({'internoen': 'nunique', 'pop': 'mean'})
recidivism_index = (recidivism_index['internoen'] / recidivism_index['pop']).to_frame()
recidivism_index.columns = ['index']
for indicator in ['shdi', 'healthindex', 'incindex', 'edindex',
        'lifexp', 'gnic', 'esch', 'msch']:
    recidivism_index[indicator] = data.groupby('departamento_corregido').agg({indicator: 'mean'})
recidivism_index.index = recidivism_index.index.str.lower()