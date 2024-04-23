import json

def products_read():  
    with open('database/products.json','r') as json_file:
        items_data = json.load(json_file)
        return items_data
    
def cart_read():  
    with open('database/cart.json','r') as json_file:
        cart_data = json.load(json_file)
        return cart_data
    
def balance_read():  
    with open('database/balance.json','r') as json_file:
        balance_data = json.load(json_file)
        return balance_data
    
def users_read():  
    with open('database/users.json','r') as json_file:
        users_data = json.load(json_file)
        return users_data
    
def history_read():
    with open('database/history.json', 'r') as json_file:
        history_data = json.load(json_file)
        return history_data

users = users_read()  
products = products_read()
cart = cart_read()
balance = balance_read()
history = history_read()

    
def cart_save(): 
    with open('database/cart.json', 'w') as json_file:
        json.dump(cart, json_file)

def products_save(): 
    with open('database/products.json', 'w') as json_file:
        json.dump(products, json_file)

def balance_save(): 
    with open('database/balance.json', 'w') as json_file:
        json.dump(balance, json_file)

def users_save(): 
    with open('database/users.json', 'w') as json_file:
        json.dump(users, json_file)
        
def history_save():
    with open('database/history.json', 'w') as json_file:
        json.dump(history, json_file)





