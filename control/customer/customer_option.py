import math
import config.config as cf
import support.support as support

def shopping_menu_option( page,current_page, total_page):
        if page == 0 and total_page > 1 :
                print("""
1. Sort By Lowest Price     6. Add Product To Cart
2. Sort By Highest Price    7. Next Page
3. Sort By Category         8. ---------
4. Search Product By Name 
5. Sort By Most Sell        0. Main Menu
""")
        elif page == 0 and total_page == 1:
                print("""
1. Sort By Lowest Price     6. Add Product To Cart
2. Sort By Highest Price    7. ---------
3. Sort By Category         8. ---------
4. Search Product By Name  
5. Sort By Most Sell        0. Main Menu
""")
        elif current_page < total_page : 
                print("""
1. Sort By Lowest Price     6. Add Product To Cart
2. Sort By Highest Price    7. Next Page
3. Sort By Category         8. Previous Page
4. Search Product By Name   
5. Sort By Most Sell        0. Main Menu
""")
        else :
                print("""
1. Sort By Lowest Price     6. Add Product To Cart
2. Sort By Highest Price    7. ---------
3. Sort By Category         8. Previous Page
4. Search Product By Name  
5. Sort By Most Sell        0. Main Menu
""")
                
def customer_dashboard_option():
    print("""
-- WELCOME TO EASY SHOP --
    0. Log out
    1. Account Info
    2. Balance Info
    3. Shopping List
    4. Shopping Cart
    5. Shopping History
""")


def account_and_balance_option(balance, users):
    print(f"""
HELLO : {users[0]['username']}
YOUR BALANCE IS   : {support.currency_format(balance['balance'])}
1. TOP UP
2. EDIT ACCOUNT INFO * COMING SOON !!
0. MAIN MENU  
""")


def cart_menu_option():
    print("""
1. Checkout cart            0. Back to Main Menu 
2. Delete Cart              
""")

def purchase_history_option():
    print("""
0. Back to main menu   
          """)
    
def balance_info_option():
    print("""
0. Main Menu
1. Balance info
2. Top Up
""")
    
def account_info_option():
    print("""
0. Main Menu
1. Account Info
2. Edit Password
""")
    
    
def shopping_list_option():
    print("""
0. Main Menu
1. Add product to Cart
2. Sort Product
3. Filter Product
""")
    