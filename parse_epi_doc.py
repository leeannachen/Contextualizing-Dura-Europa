import csv
import requests
import xml.etree.ElementTree as ET
import os
import sqlite3
import pandas as pd

def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    newsitems = []
    for item in root.findall('./channel/item'):
        news = {}
        newsitems.append(news)
    return newsitems


def savetoCSV(newsitems, filename):
    # specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']
    # writing to csv file
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newsitems)

def convert_to_db(csv):
    df = pd.read_csv(csv)
    df.columns = df.columns.str.strip()
    con = sqlite3.connect("sample.db")
    df.to_sql("MyTable", con)
    con.close()

if __name__ == "__main__":
    csv = 'translations.csv'
    for filename in os.listdir("/XML"):
        cur_translation = parseXML(filename)
        savetoCSV(cur_translation, csv)
    convert_to_db(csv)