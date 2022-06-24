from os import link
from flask import Flask, render_template

app = Flask(__name__)

link_de_apostilas = 'http://www.alura.com.br/apostilas'

@app.route('/test')
def principal():
    return render_template('test.html', link = link_de_apostilas)

app.run()

