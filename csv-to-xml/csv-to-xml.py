# importing needed libraries
from xml.dom import minidom
from xml.dom.minidom import parseString
from lxml import etree
import csv
import os
import sys
import glob

# purge all xml files before rebuilding
files = glob.glob("xml-result\\*")
for file in files:
	os.remove(file)

# change if you would like to purge the files
purge = False # True

if purge:
	sys.exit(0)

# initializing all variables
fields = []
rows = []

# specify path for input file
input_filename = "csv-input.csv"

# reading csv file
with open(input_filename, 'r', encoding="UTF-8") as csvfile:
	# creating a csv reader
	csvreader = csv.reader(csvfile)

	# extracting field names through first row
	fields = next(csvreader)

	# extracting rows from the rest of the file
	for row in csvreader:
		rows.append(row)

# handle minidom/xml document creation
templateXml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" \
			  "<?xml-model href=\"http://www.stoa.org/epidoc/schema/latest/tei-epidoc.rng\" schematypens=\"http://relaxng.org/ns/structure/1.0\"?>\n" \
			  "<?xml-model href=\"http://www.stoa.org/epidoc/schema/latest/tei-epidoc.rng\" schematypens=\"http://purl.oclc.org/dsdl/schematron\"?>\n"

# iterating through rows and creating xml files
for i, row in enumerate(rows):
	# specify path for output file
	output_filename = "xml-result\\inscription" + str(i) + ".xml"
	
	# create new file and append information to it
	with open(output_filename, 'w', encoding="UTF-8") as xmlfile:
		# create main document
		root = minidom.Document()

		# create parent wrapper element
		tei = root.createElement("TEI")
		tei.setAttribute("xmlns", "http://www.tei-c.org/ns/1.0")
		tei.setAttribute("xml:space", "preserve")
		tei.setAttribute("xml:lang", "en")
		root.appendChild(tei)

		# create header to store information
		teiHeader = root.createElement("teiHeader")
		tei.appendChild(teiHeader)

		# FILE DESCRIPTION
		fileDesc = root.createElement("fileDesc")
		teiHeader.appendChild(fileDesc)

		# TITLE STATEMENT
		titleStmt = root.createElement("titleStmt")
		fileDesc.appendChild(titleStmt)

		# TITLE
		title = root.createElement("title")
		titleStmt.appendChild(title)

		textNode = root.createTextNode(row[0])
		title.appendChild(textNode)

		# PUBLICATION STATEMENT
		publicationStmt = root.createElement("publicationStmt")
		fileDesc.appendChild(publicationStmt)

		authority = root.createElement("authority")
		publicationStmt.appendChild(authority)

		textNode = root.createTextNode("Yale University")
		authority.appendChild(textNode)

		idno = root.createElement("idno")
		idno.setAttribute("type", row[0])
		publicationStmt.appendChild(idno)

		# SOURCE DESCRIPTION
		sourceDesc = root.createElement("sourceDesc")
		fileDesc.appendChild(sourceDesc)

		msDesc = root.createElement("msDesc")
		sourceDesc.appendChild(msDesc)

		msIdentifier = root.createElement("msIdentifier")
		msDesc.appendChild(msIdentifier)

		repository = root.createElement("repository")
		msIdentifier.appendChild(repository)

		idno = root.createElement("idno")
		textNode = root.createTextNode("inventory number")
		idno.appendChild(textNode)
		msIdentifier.appendChild(idno)

		physDesc = root.createElement("physDesc")
		msDesc.appendChild(physDesc)

		objectDesc = root.createElement("objectDesc")
		physDesc.appendChild(objectDesc)

		supportDesc = root.createElement("supportDesc")
		objectDesc.appendChild(supportDesc)

		support = "<support>description of object/monument (likely to include <material/> and <objectType/> information, <dimensions/>, etc.)</support>"
		node = parseString(support).documentElement
		supportDesc.appendChild(node)

		layoutDesc = root.createElement("layoutDesc")
		objectDesc.appendChild(layoutDesc)

		layout = root.createElement("layout")
		textNode = root.createTextNode("description of text field/campus")
		layout.appendChild(textNode)
		layoutDesc.appendChild(layout)

		handDesc = root.createElement("handDesc")
		physDesc.appendChild(handDesc)

		handNote = "<handNote>description of letteres, possibly including <height>letter-heights</height></handNote>"
		node = parseString(handNote).documentElement
		handDesc.appendChild(node)

		history = root.createElement("history")
		msDesc.appendChild(history)

		origin = root.createElement("origin")
		history.appendChild(origin)

		origPlace = root.createElement("origPlace")
		textNode = root.createTextNode("Place of origin")
		origPlace.appendChild(textNode)
		origin.appendChild(origPlace)

		origDate = root.createElement("origDate")
		textNode = root.createTextNode("Date of origin")
		origDate.appendChild(textNode)
		origin.appendChild(origDate)

		provenance = root.createElement("provenance")
		provenance.setAttribute("type", "found")
		textNode = root.createTextNode("Findspot and circumstances/context")
		provenance.appendChild(textNode)
		history.appendChild(provenance)

		provenance = root.createElement("provenance")
		provenance.setAttribute("type", "observed")
		textNode = root.createTextNode("Modern location(s) (if different from repository, above)")
		provenance.appendChild(textNode)
		history.appendChild(provenance)

		# FAC SIMILE
		facsimile = root.createElement("facsimile")
		tei.appendChild(facsimile)

		# GRAPHIC OF INSCRIPTION
		graphic = root.createElement("graphic")
		graphic.setAttribute("url", "photograph of text or monument")
		facsimile.appendChild(graphic)

		# TEXT ELEMENT
		text = root.createElement("text")
		tei.appendChild(text)

		# BODY WRAPPER
		body = root.createElement("body")
		text.appendChild(body)

		# create unique DIVS to add
		for j, item in enumerate(row):
			# DIV ELEMENTS
			div = root.createElement("div")
			div.setAttribute("type", fields[j])
			body.appendChild(div)

			# PARAGRAPH ELEMENTS
			par = root.createElement("p")
			description = root.createTextNode(item)
			par.appendChild(description)
			div.appendChild(par)

		# convert xml data structures to their respective string versions
		xmlStr = templateXml + root.childNodes[0].toprettyxml(indent = '\t')

		# write xml string to the final xml file
		xmlfile.write(xmlStr)

# STILL NEED TO CONSIDER
# a lot of it is unfinished
# what happens with blank spaces
# fix a lot of the formatting
# decide on a more standard way of creating the spreadsheets
