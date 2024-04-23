import support.support as support
import control.admin.admin_option as option
import config.config as cf
import math
import control.admin.admin_control as control
import control.general.general_control as general
import control.general.general_option as general_option

def product_list():
    while True :
        option.product_list_option()
        user_input_choice = support.user_input_choice()

        if user_input_choice == "0":
            break
            
        elif user_input_choice == "1":
            product_name = support.user_input_choice("Input new product name : ")
            result, message =  control.exist_product_name(product_name)
            
            if result == None :
                support.error_message(message)
                
            
            elif not result :
                support.error_message(message)
            
            elif result  :
                category = support.user_input_choice("Input product category : ")
                price = support.user_input_choice("Input product price : ")
                result1, product_price = support.input_check(price)
                
                print(product_price)
                if result1 and product_price != 0 : 
                    stock = support.user_input_choice("Input product stock : ")    
                    result2, product_qty = support.input_check(stock)
                    
                    if result2 and product_qty != 0 :
                        control.create_and_update(product_name, category, product_qty,  stock)
                        support.success_message(message )
                        
                    elif not result2:
                        support.error_message("Invalid stock input") 

                elif not result1 :
                    support.error_message("Invalid price input") 
                    
        elif user_input_choice == "2":
            products = cf.products
            page = 0
            total_page = math.ceil(len(products) / 5)
            general.show_product_list(products, page, total_page)
            product_number = support.user_input_choice("Input product number  : ") 
            result, product_index = support.input_check(product_number)
            product_id = products[product_index-1]['product_id']
            product = control.get_product_by_id(product_id)

            if result and len(product) == 0  :
                support.error_message('Product number is not on the list')
                
            elif result and len(product) != 0 :
                category = support.user_input_choice("Input new product category : ")
                price = support.user_input_choice("Input new product price : ")
                result1, product_price = support.input_check(price)

                if result1 and product_price != 0 : 
                    stock = support.user_input_choice("Input new product stock : ")    
                    result2, product_qty = support.input_check(stock)
                    
                    if result2 and product_qty != 0 :
                        control.create_and_update(product['name'], product['category'],product['price'], product['stock'], product['product_id'] )
                        support.success_message('Product update is success')
                        
                    elif not result2:
                        support.error_message("Invalid stock input") 

                elif not result1 :
                    support.error_message("Invalid price input")  
                
            else :
                support.error_message()
                
                
        elif user_input_choice == "3":
            products = cf.products
            page = 0
            total_page = math.ceil(len(products) / 5)
            general.show_product_list(products, page, total_page)
            product_number = support.user_input_choice("Input product number  : ") 
            result, product_index = support.input_check(product_number)
            
            if result and product_index <= len(products) and product_index != 0:
                product_id = products[product_index-1]['product_id']
                command = support.user_input_choice("Are you sure want to delete ? Press 1.Yes or 0.No : ") 
                status = support.user_confirmation(command)

                if status == True:
                    cf.products.pop(product_index - 1)
                    cf.products_save()
                    support.success_message('Product is deleted')  
                    
                elif status == False :
                    support.clean_screen()
                    
                else :
                    support.error_message()
                    
            elif result and product_index > len(products) or product_index == 0 :
                support.error_message('Product number is not on the list')
            
            else  :
                support.error_message()

            
        elif user_input_choice == "4":
            while True :
                general_option.product_list_sort_option()
                user_input_choice = support.user_input_choice()
                
                if user_input_choice == '0':
                    support.clean_screen()
                    break
                
                elif user_input_choice == '1':
                    product_sorted = general.products_filter(params='stock')
                    general.show_product_list(product_sorted, 1, 5)
                    
                elif user_input_choice == '2':
                    print('price')
                    
                else :
                    support.clean_screen()
                    support.error_message()
                    
            
        elif user_input_choice == "5":
            print('FILTER PRODUCT')
            
        else :
            support.error_message() 




