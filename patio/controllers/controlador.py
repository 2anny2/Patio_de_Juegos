
from patio import app
from flask import render_template

@app.route('/') 
def play1():
    return render_template("juego.html")  

@app.route('/play/<int:numero>')          
def play_num(numero):
    return render_template("juego.html", numero=numero)  


@app.route('/play/<int:numero>/<color>')          
def play_num_color(numero, color):
    return render_template("juego.html", numero=numero, color=color)  

@app.errorhandler(404)          
def paginaNoEncontrada(e):
    return 'ESTA RUTA NO FUE ENCONTRADA!', 404
