import os
import time
import locale
import config.config as cf
locale.setlocale(locale.LC_ALL, '')


def user_input_choice(message='ENTER OPTION NUMBER : '):
    user_input_choice = input(message.upper())
    return user_input_choice

def message_timer(value):
    time.sleep(value)
    
def success_message(message="UPDATE IS SUCCESS!!", variable=""):
    # os.system("cls")
    print(message.upper(), variable)
    time.sleep(1)
    # os.system("cls")
    
def user_confirmation(command):
    if command == '1' :
        return True
    elif command == '0':
        return False
    else :
        return None

def error_message(message="INVALID NUMBER !! PLEASE ENTER THE RIGHT VALUES !!"):
    # os.system("cls")
    print(message.upper())
    time.sleep(1)
    # os.system("cls")


def currency_format(amount):
    formatted_number = locale.format_string("%.0f", amount, grouping=True)
    return "IDR " + formatted_number

def input_check(params):

    if params.isdigit():
        value = int(params)
        return True, value
    
    else : 
        return False, params
    
def login_menu_input(): 
    print("ENTER YOUR USERNAME AND PASSWORD OR ENTER 0 TO EXIT")
    username_input = input("USERNAME : ")
    if username_input == '0':
        return False, False
    else :
        password_input = input('PASSWORD : ')
        return username_input, password_input
   
def clean_screen():
    os.system('cls') 

def loading_animation():
    os.system('cls')
    print("REDIRECTING . ")
    time.sleep(0.15)
    os.system('cls')
    print("REDIRECTING .. ")
    time.sleep(0.15)
    os.system('cls')
    print("REDIRECTING ...")
    time.sleep(0.15)
    os.system('cls')
    print("REDIRECTING ....")
    time.sleep(0.15)
    os.system('cls')
    print("REDIRECTING .....")
    time.sleep(0.15)
    os.system('cls')
    print("REDIRECTING . ")
    time.sleep(0.15)
    os.system('cls')
    print("REDIRECTING .. ")
    time.sleep(0.15)
    os.system('cls')
    print("REDIRECTING ...")
    time.sleep(0.15)
    os.system('cls')
    print("REDIRECTING ....")
    time.sleep(0.15)
    os.system('cls')
    print("REDIRECTING .....")
    time.sleep(0.15)
    os.system('cls')
    
    

def user_role_check(username, password):
    user_info = list(filter(lambda x:x['username'] == username, cf.users))
    
    if username == False and password == False :
        return False, False
    
    elif len(user_info) ==  0:
        return "1", 'Username is not exist !!!'
    
    elif user_info[0]['password'] != password:
        return "2", 'Password is wrong !!!'
    
    elif user_info[0]['role'] == 'customer':
        return "3", user_info
    
    else:
        return "4", user_info
    
    
def get_user_info(username):
    users = list(filter(lambda x:x['username'] == username, cf.users))
    return users


def get_balance_info(user_id):
    balance = list(filter(lambda x:x['user_id'] == user_id[0]['user_id'], cf.balance))
    return balance[0]

def get_cart_info(user_id):
    cart = list(filter(lambda x:x['user_id'] == user_id, cf.cart))
    return cart


def add_balance(balance,amount):
    for i in cf.balance:
        if i['balance_id'] == balance['balance_id']:
            i['balance'] += int(amount)
            balance['balance'] = i['balance']
            cf.balance_save()
    return balance
    
    
def debug(value):
    print('ERROR CHECKING SUCCESS :', value)
