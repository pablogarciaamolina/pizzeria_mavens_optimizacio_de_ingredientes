import os
from load_stock_xml import create_xml
import xhtml2pdf as pdf

if 'mavens_xml.xml' not in os.listdir(): create_xml()
XML = open('mavens_xml.xml', encoding='utf_8')


