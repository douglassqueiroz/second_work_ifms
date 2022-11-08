from crypt import methods
from inspect import trace
from flask import Flask, render_template, request


meu_app = Flask(__name__)

@meu_app.route('/trabalho2', methods=['GET','POST'])
def principal():
    if request.method == 'GET':
        return render_template('/trabalho2.html')
    if request.method == 'POST':
        nome = request.form.get('nome')
        return render_template('trabalho2.html', nome = nome)

