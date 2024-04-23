import math 
import config.config as cf
from tabulate import tabulate # type: ignore


def filter_params(product_name, category, min_price, max_price, product):
    if (not product_name or product_name.lower() in product['name'].lower()) and \
       (not category or product['category'].lower() == category.lower()) and \
       (min_price is None or product['price'] >= min_price) and \
       (max_price is None or product['price'] <= max_price):
        return True
    else:
        return False

def products_filter(product_name=None, category=None, min_price=None, max_price=None, params='name', order=False):
    filter_product = list(filter(lambda product: filter_params(product_name, category, min_price, max_price, product), cf.products))
    filter_product_sorted = sorted(filter_product, key=lambda x: x[params], reverse=order) 
    return filter_product_sorted


def sort_product(params, order=False):
        sorted_product = sorted(cf.products, key=lambda x: x[params], reverse=order) 
        return sorted_product
    
def filter_product(params, order=False):
    filtered_product = [product for product in cf.products if params in product['name']]
    sorted_product = sorted(filtered_product, key=lambda x: x['name'], reverse=order)
    return sorted_product


def show_product_list(products, start_index, total_page):
    headers = ["No", "Name", "Price", "Stock", "Category"]
    data = []
    for index, product in enumerate(products[start_index:(start_index + 5)]):
        data.append([
            start_index + (index + 1),
            product['name'],
            product['price'],
            product['stock'],
            product['category']
        ])
    print(tabulate(data, headers=headers, tablefmt="grid"))
    print(f"Page {(start_index // 5)+1 } of {total_page}")

        
def list_categories():
    unique_categories = set()
    for product in cf.products:
        unique_categories.add(product['category'])   
    return list(unique_categories)
        
def show_categories(categories):
    headers = ["No", "Category"]
    data = [(index + 1, category) for index, category in enumerate(categories)]
    print(tabulate(data, headers=headers, tablefmt="grid"))
    
def update_product_qty(product_id, quantity):
    for product in cf.products:
        if product['id'] == product_id['id']:
            product['stock'] -= quantity
            cf.products_save()
