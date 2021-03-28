# Importando Bibliotecas
import numpy as np
import os
import joblib
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import MinMaxScaler 

# Criando o APP
app = Flask(__name__)

# Função para fazer previsão com dados do formulário
def previsao_diabates(lista):
    entrada = np.asarray(lista).reshape(1, 8)
    entrada_normalizada = joblib.load('scaler.sav')
    input_variables = entrada_normalizada.transform(entrada)
    melhor_modelo = joblib.load('model.sav')
    output = melhor_modelo.predict(input_variables)
    return output[0]

# Função para abrir página HTML e digitar valores
@app.route('/')
def entrada():
    return render_template('formulario.html')

# Função para pegar os valores dapágina HTML e plotar o resultado
@app.route('/result', methods=['POST'])
def saida():
    if request.method=='POST':
        reposta_formulario = request.form.to_dict()
        reposta_formulario = list(reposta_formulario.values())
        reposta_formulario = map(float, reposta_formulario)
        reposta_formulario = list(reposta_formulario)
        inferencia = previsao_diabates(reposta_formulario)
        if int(inferencia)==1:
            diagnostico = 'O paciente é diabético.'
        else:
            diagnostico = 'O paciente não é diabético.'
    return render_template('resultado.html', previsao=diagnostico)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
