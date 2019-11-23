#!/Users/juan/anaconda3/bin/python3
import requests
from bs4 import BeautifulSoup
from datetime import date

def extract_price(str):
    digits = ''
    for c in str:
        if c.isdigit():
            digits += c

    return int(digits)

def run():
    path = '/Users/juan/projects/precios-tinglesa'

    f = open(path + '/result.csv', 'a')
    d = date.today().isoformat()
    products = open(path + '/products', 'r').readlines()

    for url in products:
        url = url.replace("\n","")
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        s = soup.find_all(id='TXTPRICE')[0]
        price = extract_price(s.get_text())
        product_id = url.split('?')[1]

        f.write('{},{},{}\n'.format(d, product_id, price))

    f.close()

if __name__ == '__main__':
    run()