
import math
import config.config as cf
import support.support as support
import control.admin.admin_option as adm_option
import control.admin.admin_statement as statement
import control.general.general_control as control
import control.customer.customer_option as option
import control.customer.customer_control as customer


products = cf.products
def shopping_list(users):
    global products
    page = 0
    while True :
        total_page = math.ceil(len(products) / 5)
        control.show_product_list(products, page, total_page)
        option.shopping_list_option()
        user_input_choice = support.user_input_choice()

        if user_input_choice == "0":
            break

        elif user_input_choice == "1":
            total_page = math.ceil(len(products) / 5)
            purchase = True
            while purchase :
                support.clean_screen()
                control.show_product_list(products, page, total_page)
                user_input_choice = support.user_input_choice('Enter product number to buy or 0 to cancel : ')
                isdigits, product_number = support.input_check(user_input_choice)
                
                if isdigits and product_number <= len(products) and product_number > 0 :
                    selected_product = cf.products[product_number-1]
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
                            purchase = False
                            break
                            
                        elif isdigits and product_qty > product_stock :
                            support.clean_screen()
                            support.error_message('Product is out stock')
                            purchase = False
                            break
                            
                        else :
                            support.error_message()
                            purchase = False
                            break
                            
                elif isdigits and product_number > len(products) :
                    support.clean_screen()
                    support.error_message('Product Number is out of list')
                    purchase = False
                    break
                
                elif isdigits and product_number == 0 :
                    support.clean_screen()
                    purchase = False
                    break
                
                else :
                    support.error_message()
                    purchase = False
                    break
           

        elif user_input_choice == "2":
            first_condition = True
            while first_condition :
                support.clean_screen()
                adm_option.sort_by_option()
                user_input_choice = support.user_input_choice()
                
                if user_input_choice == '0':
                    support.clean_screen()
                    break
                
                elif user_input_choice =='1':
                    sort_product = control.products_filter(params='stock', order=False)
                    statement.pagination_product('stock', sort_product)
                
                elif user_input_choice == '2':
                    sort_product = control.products_filter(params='price', order=False)
                    page = 0
                    statement.pagination_product('price', sort_product)
                else :
                    support.error_message()
                    
        elif user_input_choice == "3":
            while True :
                support.clean_screen()
                adm_option.filter_search_option()
                user_input_choice = support.user_input_choice()
                    
                if user_input_choice == '0':
                    support.clean_screen()
                    break
                    
                elif user_input_choice =='1':
                    product_name = support.user_input_choice("Enter product name : ")
                    filter_product = control.products_filter(product_name=product_name)
                    if len(filter_product) == 0 :
                        support.error_message(f" '{product_name}' is not exist ")
                    else :
                        statement.pagination_product(sort_type='name', sort_product=filter_product ,product_name=product_name)
                    
                elif user_input_choice == '2':
                    min_price = support.user_input_choice("Enter product min price : ")
                    max_price = support.user_input_choice("Enter product max price : ")
                    filter_product = control.products_filter(min_price=int(min_price), max_price=int(max_price))
                    statement.pagination_product(sort_type='name', sort_product=filter_product ,product_name=product_name)
                       
        elif user_input_choice == '4':
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
 
        else :
            support.error_message() 