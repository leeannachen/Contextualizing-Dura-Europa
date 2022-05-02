import os
import sqlite3
from sqlite3 import Error
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd
import csv
import csv
import requests
import xml.etree.ElementTree as ET
import os
import sqlite3
import pandas as pd
import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# db = sqlite3("sqlite:///temple.db")

# # Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")
first = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    # """Show portfolio of stocks"""
    # connection = sqlite3.connect("finance.db")
    # crsr = connection.cursor()
    # crsr.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES(1, 2, 3, 4)")
    # answer = list(crsr.execute(f'SELECT * from transactions'))
    # connection.commit()
    # connection.close()
    # print(answer)
    return render_template('index.html')


@app.route("/choose", methods=["GET", "POST"])
def choose():
    """Buy shares of stock"""
    # connection = sqlite3.connect("finance.db")
    # crsr = connection.cursor()
    # answer = crsr.execute(f'SELECT * FROM transactions')
    # connection.commit()
    # connection.close()
    # print(answer)
    return apology("TODO")

@app.route("/about",  methods=["GET", "POST"])
def about():
    return render_template('about.html')

@app.route("/gate")
def gate():
    return render_template('gate.html')

@app.route("/temple", methods=["GET", "POST"])
def temple():
    global first
    if request.method == "POST":
        con = sqlite3.connect("translations.db")
        cursor_object = con.cursor()
        script = "SELECT * FROM temple WHERE No = ?"
        answer = cursor_object.execute(script, (str(request.form.get("block").strip()),))
        keys = ['', 'no','inscription', 'transcription','translation','source','image', 'period', 'block' ,'height', 'bibliography', 'app', 'notes']
        dic = dict()
        results = []
        for info in answer:
            i = 0
            dic = dict()
            for piece in info:
                if i != 0:
                    dic[keys[i]] = piece
                i+=1
            results.append(dic)
        return render_template('metadata.html', translations=results)
    else:
        con = sqlite3.connect("translations.db")
        cursor_object = con.cursor()
        answer = cursor_object.execute("SELECT No , Translation FROM temple;")
        results = []
        for result in answer:
            if result != None:
                if str(result) != '(None, None)':
                    results.append(list(result))
        return render_template('temple.html', translations=results)

@app.route("/metadata", methods=["GET", "POST"])
def metadata():
    return render_template('metadata.html', translations=[])#translations=[{'image':"../static/images/Kaitlyn.jpeg", 'inscription':"Inscription",
                                            # 'transcription': "Transcription", 'translation':"Translation",'source':"Translation Source", 'period': "Period", 'block':"Block" ,
                                            #  'height':"Letter Height", 'bibliography':"Bibliography", 'app':"Apparatus",'notes':"Commentary"},
                                            # {'image': "../static/images/Kaitlyn.jpeg",
                                            # 'inscription': "Inscription2",'transcription': "Transcription2",
                                            # 'translation': "Translation2", 'source': "Translation Source2",
                                            # 'period': "Period2", 'block': "Block2",
                                            # 'height': "Letter Height2", 'bibliography': "Bibliography2",
                                            # 'app': "Apparatus2", 'notes': "Commentary2"}
                                            # ])