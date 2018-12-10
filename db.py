import sqlite3
from contextlib import closing
from business import Product, LineItem, Cart


conn = sqlite3.connect("products.sqlite")
conn.row_factory = sqlite3.Row

def update_products(cart):
    cart.business.getItemCount()


def make_product(row):
    return Product(row["productID"], row["name"], row["price"], row["discountPercent"])

def get_products():
    query = '''SELECT *, FROM products'''
    with closing(conn.cursor()) as c:
        c.execute(query,)
        results = c.fetchall()

    products = []
    for row in results:
        products.append(make_product(row))
    return products


def get_products_by_price(price):
    query = '''SELECT productID, products.name, price, discountPercent,
               WHERE price = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (price,))
        results = c.fetchall()

    products = []
    for row in results:
        products.append(make_product(row))
    return products


def add_product(product):
    sql = '''INSERT INTO products (productID, name, price, discountPercent) 
             VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (product.name, product.price,
                        product.discountPercent))
        conn.commit()


def delete_product(product_id):
    sql = '''DELETE FROM Product WHERE productID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (product_id,))
        test = conn.commit()
        print("Test", test)
