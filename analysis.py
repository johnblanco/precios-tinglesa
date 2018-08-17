import csv

lines = open('result.csv', 'r').readlines()
products = {}
for l in lines:
    l = l.replace("\n", "")
    date = l.split(",")[0]
    product_name = l.split(",")[1].replace('https://www.tiendainglesa.com.uy/', '')
    price = l.split(",")[2]

    if product_name in products:
        p = products[product_name]
        p[date] = price
    else:
        products[product_name] = {'name': product_name, date: price}

first_product = products[list(products.keys())[0]]

with open('analysis.csv', 'w') as f:
    w = csv.DictWriter(f, first_product.keys())
    w.writeheader()
    for p in products:
        w.writerow(products[p])