from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/index/printers/riso')
def printersRiso():
    return 'Printers Riso Page'