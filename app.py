from flask import Flask
from flask import render_template

app = Flask('app', template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('home.html')
