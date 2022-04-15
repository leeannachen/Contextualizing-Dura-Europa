# Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
import os

def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    # create empty list for news items
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




if __name__ == "__main__":
    for filename in os.listdir("/XML"):
        cur_translation = parseXML(filename)
        savetoCSV(cur_translation, 'translations.csv')
