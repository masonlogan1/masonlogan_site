from flask import Flask
from flask import render_template, url_for

app = Flask('app', template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('home.html')
