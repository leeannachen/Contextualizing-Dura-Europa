import os
import sqlite3
from sqlite3 import Error
from flask import Flask, flash, redirect, render_template, request, session
import flask_session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd



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
db = None#SQL("sqlite:///sample.db")

# # Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Show portfolio of stocks"""
    connection = sqlite3.connect("finance.db")
    crsr = connection.cursor()
    crsr.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES(1, 2, 3, 4)")
    answer = list(crsr.execute(f'SELECT * from transactions'))
    connection.commit()
    connection.close()
    print(answer)
    return render_template('index.html')


@app.route("/choose", methods=["GET", "POST"])
def choose():
    """Buy shares of stock"""
    connection = sqlite3.connect("finance.db")
    crsr = connection.cursor()
    answer = crsr.execute(f'SELECT * FROM transactions')
    connection.commit()
    connection.close()
    print(answer)
    return apology("TODO")


@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')


@app.route("/quote", methods=["GET", "POST"])
def quote():
    """Get stock quote."""
    return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
def sell():
    """Sell shares of stock"""
    return apology("TODO")