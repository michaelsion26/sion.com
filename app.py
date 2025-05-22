from flask import Flask, render_template, request, jsonify
import pandas as pd
import random, csv
from datetime import datetime

app = Flask(__name__)

preguntas_df = pd.read_excel('data/Versiculos_Biblia_v6.xlsx')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz_page():
    return render_template('quiz.html')

@app.route('/get_quiz', methods=['POST'])
def get_quiz():
    cantidad = int(request.json['cantidad'])
    preguntas = preguntas_df.sample(n=cantidad).to_dict(orient='records')

    quiz_data = []
    for p in preguntas:
        opciones = [p['Response'], p['Opcion1'], p['Opcion2'], p['Opcion3']]
        random.shuffle(opciones)
        quiz_data.append({'question': p['Verse'], 'options': opciones, 'answer': p['Response']})

    return jsonify(quiz_data)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    data = request.json
    score, total = data['score'], data['total']
    nombre, tiempo_usado = data['nombre'], data['tiempo_usado']
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    vigesimal = round((score / total) * 20, 2)

    with open('results/history.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([fecha, nombre, tiempo_usado, vigesimal])

    return jsonify({'score_vigesimal': vigesimal})

if __name__ == '__main__':
    app.run(debug=True)
