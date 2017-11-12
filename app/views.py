from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/printers/riso')
def printersRiso():
    return render_template("riso-base.html")


@app.route('/printers/toshiba')
def printersToshiba():
    return render_template("toshiba-base.html")


@app.route('/printers/riso/comcolor/fw5230')
def risofw5230():
    return render_template("riso-comcolor-fw5230.html")