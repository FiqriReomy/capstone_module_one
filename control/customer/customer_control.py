import config.config as cf
from tabulate import tabulate  # type: ignore
import datetime

def get_user_cart(users):
    user_cart = list(filter(lambda x:x['user_id'] == users[0]['user_id'],cf.cart))
    return user_cart

def update_user_cart(select_product,user_cart, quantity, condition):
    product_id = select_product['product_id']
    product_name = select_product['name']
    product_price = select_product['price']

    if len(user_cart) == 0 and condition == 'add' :
        new_cart =  {"user_id": user_cart[0]['user_id'], "product_id": product_id ,"name": product_name, "price": product_price, "quantity": quantity}
        cf.cart.append(new_cart)
        cf.cart_save()
        
    else :
        for cart in cf.cart :
            if cart['user_id'] == user_cart[0]['user_id'] and cart['product_id'] == product_id and condition == 'add':
                cart['quantity'] += quantity
                cf.cart_save()
                
            elif cart['user_id'] == user_cart[0]['user_id'] and cart['product_id'] == product_id and condition == 'remove':
                cf.cart.remove(cart)
                cf.cart_save()
            

def add_to_cart(mycart, product, users, quantity):
    user_id = users[0]['user_id']
    product_id = product['product_id']
    product_name = product['name']
    product_price = product['price']
    item_cart = list(filter(lambda x:x['product_id'] == product_id, mycart))
    
    if len(item_cart) == 0 :
        new_cart =  {"user_id": user_id, "product_id": product_id ,"name": product_name, "price": product_price, "quantity": quantity}
        cf.cart.append(new_cart)
        cf.cart_save()
        
    else :
        for cart in cf.cart :
            if cart['user_id'] == user_id and cart['product_id'] == product_id:
                cart['quantity'] += quantity
                cf.cart_save()

def checkout_check(checkout_cart, item, value):
    cart_item = item[value - 1]
    

    if len(checkout_cart) == 0:
        checkout_cart.append(cart_item)
        return checkout_cart
    

    for existing_item in checkout_cart:
        if existing_item['product_id'] == cart_item['product_id']:
            return checkout_cart  
    checkout_cart.append(cart_item)
    return checkout_cart



def add_checkout_item(cart_item, selected_item):
    checkout_item = [cart_item[index - 1] for index in selected_item if index <= len(cart_item)]
    return checkout_item

def remove_checkout_item(checkout_item):
    for item in checkout_item:
        cf.cart = [cart for cart in cf.cart if not (cart['user_id'] == item['user_id'] and cart['product_id'] == item['product_id'])]
        cf.cart_save()
    
def update_product_sold(checkout_item):
    for item in cf.products :
        for check in checkout_item:
            if item['id'] == check['product_id']:
                item['sold'] += check['quantity']
                cf.products_save()
                
def update_product_quantity(selected_item, users):
    for item in cf.products :
        for selected in selected_item:
            if item['id'] == selected['product_id']:
                item['stock'] += selected['quantity']
                for cart in cf.cart :
                    if cart['user_id'] != users and cart['product_id'] != selected['product_id']:
                        cf.cart_save()
                cf.products_save()
                
def show_cart(user_cart):
    headers = ["No", "Name", "Price", "Quantity", "Total"]
    data = []
    for index, cart in enumerate(user_cart):
        total = cart['quantity'] * cart['price']
        data.append([
            index + 1,
            cart['name'],
            cart['price'],
            cart['quantity'],
            total
        ])
        
    print(tabulate(data, headers=headers, tablefmt="grid"))
    
def show_checkout(user_cart):
    headers = ["No", "Name", "Price", "Quantity", "Total"]
    data = []
    total_amount = 0
    for index, cart in enumerate(user_cart):
        total = cart['quantity'] * cart['price']
        data.append([
            index + 1,
            cart['name'],
            cart['price'],
            cart['quantity'],
            total
        ])
        total_amount += total
        
    data.append(["", "", "", "Total Price", total_amount])
    print(tabulate(data, headers=headers, tablefmt="grid"))
    return total_amount


def get_user_history(users):
    user_history = list(filter(lambda x:x['user_id'] == users, cf.history))
    return user_history

def show_user_history(user_history):
    headers = ["No", "Name", "Price", "Quantity", "date"]
    data = []
    for index, history in enumerate(user_history):
        data.append([
            index + 1,
            history['name'],
            history['price'],
            history['quantity'],
            history['date'],
        ])
    print(tabulate(data, headers=headers, tablefmt="grid"))



def update_purchase_history(checkout_item):
    current_date = datetime.date.today()
    for item in checkout_item:
        purchase_history = {
            "user_id": item['user_id'],
            'product_id': item['product_id'],
            'name': item['name'],
            'price': item['price'],
            'quantity': item['quantity'],
            'date': current_date.strftime("%d-%m-%Y")
        }
        cf.history.append(purchase_history)
        cf.history_save()

            

def update_product_stock(selected_product, condition) : 
    for product in cf.products :
        if product['id'] == selected_product['product_id'] and condition == 'add' :
            product['stock'] += selected_product['quantity']
            cf.products_save()
        elif product['id'] == selected_product['product_id'] and condition == 'substract' :
            product['stock'] -= selected_product['quantity']
            cf.products_save()
            
def update_account_info(users, newpassword):
    for user in cf.users :
        if users == users['username'] :
            user['password'] = newpassword
            cf.user_save()
            break

def amount_verification(amount):
    
        if not amount.isdigit() :
            return None, 'Invalid number of input  '
    
        elif int(amount) < 10000 or int(amount) > 1000000 :
            return False, "Minimum amount is 10.000 and maximum is 1000.000"  
        
        elif int(amount) >= 10000 and int(amount) < 1000000 :
            return True, f"Top up amount : {amount} is success, Please check your balance" 


def update_account_info(users , newpassword) :
    for user in cf.users :
        if user['user_id'] == users['user_id']:
            user['password'] = newpassword
            cf.users_save()
    return 'Password is updated'

                           