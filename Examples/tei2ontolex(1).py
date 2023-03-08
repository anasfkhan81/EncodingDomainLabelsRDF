import rdflib as r
import lxml.etree as e
import sys
import os
from os import listdir
from os.path import isfile, join

def convert2rdf(file):
    g=r.Graph()
    xslt_doc = e.parse('TEI2Ontolex.xsl')
    xslt_transformer = e.XSLT(xslt_doc)
    source_doc = e.parse(file)
    output_doc = xslt_transformer(source_doc)
    new_file = file[:-4]+"_rdf.xml"
    destination = file[:-4]+"_rdf.ttl"
    output_doc.write(new_file, pretty_print=True)
    g.parse(new_file)
    g.serialize(destination)

def listof():
    return [f for f in listdir() if isfile(join(f))]   
    

