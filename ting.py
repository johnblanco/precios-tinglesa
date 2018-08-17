#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import requests
from bs4 import BeautifulSoup
from datetime import date

def extract_price(str):
    digits = ''
    for c in str:
        if c.isdigit():
            digits += c

    return int(digits)


f = open('/Users/jblanco/ting/result.csv', 'a')
d = date.today().isoformat()
products = open('/Users/jblanco/ting/products', 'r').readlines()

for url in products:
    url = url.replace("\n","")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    s = soup.find_all(id='TXTPRICE')[0]
    price = extract_price(s.get_text())

    f.write('{},{},{}\n'.format(d, url, price))

f.close()