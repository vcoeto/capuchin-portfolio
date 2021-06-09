import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

from .nav import nav
load_dotenv()

app = Flask(__name__)

nav.init_app(app)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/ant')
def ant():
    return render_template('anthony.html', title="Anthony", url=os.getenv("URL"))
