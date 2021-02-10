import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output

import pandas as pd 
import numpy as np 
from apyori import apriori
import plotly.graph_objs as go

panaderia = pd.read_csv('./BreadBasket_DMS.csv')
data = 

def reglas_asociacion(min_soporte, min_confianza):
    a_rules = apriori(data, min_support = min_soporte, min_confidence = min_confianza)
    a_results = list(a_rules)
    return a_results


def extraer_info(regla):
    antecedente = ', '.join(regla[2][0][0])
    consecuente = ', '.join(regla[2][0][1])
    soporte = regla[1]
    confianza = regla[2][0][2]
    lift = regla[2][0][3]
    return '{:s} --> {:s} <br><br>Soporte: {:.3f} <br>Confianza: {:.3f} <br>Lift: {:.3f}'.format(antecedente,consecuente, soporte, confianza, lift)




app = dash.Dash(__name__)
#app = dash.Dash(__name__, external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])


app.layout = html.Div([
    
])
    
    
    
    

@app.callback(
    Output(),
    [Input(),
     Input()])
def funcion():


    
    
    
    
if __name__ == '__main__':
    app.run_server(debug=True)
    
    
