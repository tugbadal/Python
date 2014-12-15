# -*- coding: utf-8 -*-
from lxml import html
from BeautifulSoup import BeautifulSoup
import requests
from lxml import etree as ET
from decimal import Decimal
import urllib2

url = 'xml url i ' 
request = urllib2.Request(url)
request.add_header('Accept-Encoding', 'utf-8')
response = urllib2.urlopen(request)
xml = response.read().decode('utf-8', 'ignore')
parser = ET.XMLParser(remove_blank_text=True)
root = ET.fromstring(xml ,parser)

yasak = ["ayakkabi","gomlek","mont","sort","ceket","pantolon","mama","kursun"]

def clear_lower(string):
    if string is None:
        return ""
    return string.lower().replace("ı".decode("utf-8"),"i").replace("ş".decode("utf-8"),"s").replace("ö".decode("utf-8"),"o")

for Product in root.findall('Product'):
    SellerPrice = Decimal(Product.find("SellerPrice").text)
    UnitInStock = int(Product.find("UnitInStock").text)
    ModelName = Product.find("ModelName").text
    CategoryPath = Product.find("CategoryPath").text
    if SellerPrice <= 1 and SellerPrice >= 2000:
        root.remove(Product)       

    elif UnitInStock <= 1:
        root.remove(Product)

    elif any(filter(lambda ysk: ysk in clear_lower(ModelName), yasak)) or any(filter(lambda ysk: ysk in clear_lower(CategoryPath), yasak)):
        root.remove(Product)
 
f = open("andoutdoor.xml", "w")
f.write(ET.tostring(root))
f.close()
