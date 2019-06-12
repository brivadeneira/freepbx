# coding: utf-8

import dash
import dash_core_components as dcc
import dash_html_components as html

import requests

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dash_app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)
dash_app.config['suppress_callback_exceptions']=True

url_resultados = 'http://localhost:8000/'
req_resultados = requests.get(url_resultados)
resultados = req_resultados.json()

opciones = []
for key in resultados.keys():
    opciones.append({'label': key, 'value': key})

dash_app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=opciones,
        placeholder='Seleccione una opción'
    ),
    dcc.Graph(id='my-graph'),
    dcc.Interval(
            id='interval-component',
            interval=1000, # in milliseconds
            n_intervals=0
        )
#    html.Div(id='output-container')
])

@dash_app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    [dash.dependencies.Input('my-dropdown', 'value')])

def update_graph(selected_dropdown_value):
    res = resultados[selected_dropdown_value]
    x = list(res.keys())
    y = list(res.values())
    
    return {
        'data': [
            {
            'x': x,
            'y': y,
            'name': selected_dropdown_value,
            'marker': {'size': 1},
            'showlegend': True,
            'type': 'bar'
            }
        ]
    }


@dash_app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    return 'Usuario: "{}"'.format(value)

if __name__ == '__main__':
    dash_app.run_server(
        host="localhost",
        port=8001,
        debug=True)

    