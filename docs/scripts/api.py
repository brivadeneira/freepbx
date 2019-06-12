import json
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

f = open('full', 'r')

playing = []
res_encuesta = {'edades': {'18-21': 0, '21-30': 0, '30-40': 0},
               'géneros': {'F': 0, 'M': 0, 'NE': 0},
               'sabores': {'chocolate': 0, 'crema': 0, 'frutilla': 0, 'mascarpone': 0}}
               
for linea in f:
    if 'Playing' in str(linea):
        playing.append(linea)
        
for elem in playing:
    if '18-21' in elem:
        res_encuesta['edades']['18-21'] += 1
    elif '21-30' in elem:
        res_encuesta['edades']['21-30'] += 1
    elif '30-40' in elem:
        res_encuesta['edades']['30-40'] += 1
    if 'femenino' in elem:
        res_encuesta['géneros']['F'] += 1
    elif 'masculino' in elem:
        res_encuesta['géneros']['M'] += 1
    elif 'no-especifico' in elem:
        res_encuesta['géneros']['NE'] += 1
    if 'chocolate' in elem:
        res_encuesta['sabores']['chocolate'] += 1
    elif 'crema' in elem:
        res_encuesta['sabores']['crema'] += 1
    elif 'mascarpone' in elem:
        res_encuesta['sabores']['mascarpone'] += 1
        
@app.route('/')
def resultado_encuesta():
    return res_encuesta
    
if __name__ == '__main__':

    # Run app
    app.run(host="localhost",
            port=8000,
            debug=True)