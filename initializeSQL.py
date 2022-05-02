import pandas as pd
import sqlite3

with open('temple.csv', 'r') as f:
    con = sqlite3.connect("translations2.db")
    cursor_object = con.cursor()
    df = pd.read_csv('temple.csv')
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace('.','')
    df.to_sql("temple", con)

    df = pd.read_csv('gate.csv')
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace('.', '')
    df.to_sql("gate", con)