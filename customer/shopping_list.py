
import math
import config.config as cf
import support.support as support
import pages.customer_dashboard as dashboard
import control.general.general_control as control
import control.customer.customer_option as option
import control.customer.customer_control as customer

products = cf.products
page = 0
def shopping_list(users):
    global products
    global page
    while True :
        purchase = False
        current_page = (page // 5) + 1
        total_page = math.ceil(len(products) / 5)
        control.show_product_list(products, page, total_page)
        option.shopping_menu_option( page, current_page, total_page)
        user_input_choice = support.user_input_choice()

        if user_input_choice == "1":
            page = 0
            support.clean_screen()
            products = control.products_filter(params='price',order=False)
            
        elif user_input_choice == "2":
            page = 0
            support.clean_screen()
            products = control.products_filter(params='price',order=True)
            
        elif user_input_choice == "3":
            
            while True:
                categories = control.list_categories()
                control.show_categories(categories)
                user_input_choice = support.user_input_choice('Enter category number or 0 to cancel ')
                isdigits, value = support.input_check(user_input_choice)
                
                if isdigits and value <= len(categories) and value > 0 :
                    page = 0
                    category = categories[value - 1]
                    products = control.products_filter(category = category)
                    break
                
                elif isdigits and value > len(categories)  :
                    support.error_message("Category number is out of list")
                    support.clean_screen()
                    
                elif isdigits and value == 0 :
                    break

                else :
                    support.error_message()
         
        elif user_input_choice == "4":
            
            while True:
                user_input_choice = support.user_input_choice('Enter name of product you want to search :')
                products = control.products_filter(product_name = user_input_choice)
                
                if len(products) == 0:
                    support.clean_screen()
                    support.success_message('No result for : ',user_input_choice)
                    products = cf.products
                    
                else :
                    page = 0
                    support.clean_screen()
                    support.success_message('Showing Result for : ', user_input_choice)
                    break
                
        elif user_input_choice == "5":
            page = 0
            support.clean_screen()
            products = control.products_filter(params='sold',order=True)
            support.success_message('Showing result for most sold product')
        
        elif user_input_choice == "6":
            
            while purchase != True :
                support.clean_screen()
                control.show_product_list(products, page, total_page)
                user_input_choice = support.user_input_choice('Enter product number to buy or 0 to cancel : ')
                isdigits, product_number = support.input_check(user_input_choice)
                
                if isdigits and product_number <= len(products) and product_number > 0 :
                    selected_product = products[product_number-1]
                    product_stock = selected_product['stock']
                    while True :
                        user_input_choice = support.user_input_choice('Enter product quantity : ')
                        isdigits, product_qty = support.input_check(user_input_choice)

                        if isdigits and product_qty <= product_stock and product_qty > 0 :
                            support.clean_screen()
                            user_cart = customer.get_user_cart(users)  
                            customer.add_to_cart(user_cart,selected_product, users, product_qty)
                            control.update_product_qty(selected_product, product_qty)
                            support.success_message('Product is added to Cart')
                            purchase = True
                            break
                            
                        elif isdigits and product_qty > product_stock :
                            support.clean_screen()
                            support.error_message('Product is out stock')
                            break
                            
                        else :
                            support.error_message()
                            
                elif isdigits and product_number > len(products) :
                    support.clean_screen()
                    support.error_message('Product Number is out of list')
                
                elif isdigits and product_number == 0 :
                    support.clean_screen()
                    break
                
                else :
                    support.error_message()
        
        elif user_input_choice == "7" and current_page  < total_page :
            support.clean_screen()
            page += 5
          
        elif user_input_choice == "8" and current_page  > 1 :
            support.clean_screen()
            page -= 5
         
        elif user_input_choice == "0" :
            support.loading_animation()
            dashboard.customer_dashboard_menu(users)
        
        else:
            support.error_message()

