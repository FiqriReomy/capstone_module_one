import math
import config.config as cf
import support.support as support
import control.admin.admin_option as option
import control.admin.admin_control as control
import control.general.general_control as general
import control.admin.admin_statement as statement

def sales_record():
    products = cf.products
    while True :
        option.sales_record_option()
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

                if result1 and product_price != 0 : 
                    stock = support.user_input_choice("Input product stock : ")    
                    result2, product_stock = support.input_check(stock)
                    
                    if result2 and product_stock != 0 :
                        control.create_and_update(product_name, category, product_price, product_stock)
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
           
   
            if result and  product_index <= len(products) and product_index != 0 :
                product_id = products[product_index-1]['product_id']
                name = support.user_input_choice('Input new product name : ')
                category = support.user_input_choice("Input new product category : ")
                price = support.user_input_choice("Input new product price : ")
                result1, product_price = support.input_check(price)
                 
                if result1  : 
                    stock = support.user_input_choice("Input new product stock : ")    
                    result2, product_stock = support.input_check(stock)
                    
                    if result2 and product_stock != 0 :
                        control.create_and_update(name, category, product_price, product_stock, product_id )
                        support.success_message('Product update is success')
                        
                    else :
                        support.error_message("Invalid stock input") 
                        
                else :
                    support.error_message('invalid price input')
                    
            elif result and  product_index > len(products) :
                support.error_message('Product number is out of list')  
                   
            else :
                support.error_message()

        elif user_input_choice == "3":
            page = 0
            total_page = math.ceil(len(products) / 5)
            general.show_product_list(products, page, total_page)
            product_number = support.user_input_choice("Input product number  : ") 
            result, product_index = support.input_check(product_number)
            statement.pagination_product('stock', sort_product)
            
            if result and product_index <= len(products) and product_index != 0:
                product_id = products[product_index-1]['product_id']
                command = support.user_input_choice("Are you sure want to delete ? Press 1.Yes or 0.No : ") 
                status = support.user_confirmation(command)

                if status == True:
                    cf.products.pop(product_index - 1)
                    cf.products_save()
                    support.clean_screen()
                    support.success_message('Product is deleted')  
                    
                elif status == False :
                    support.clean_screen()
                    
                else :
                    support.clean_screen()
                    support.error_message()
                    
            elif result and product_index > len(products) or product_index == 0 :
                support.clean_screen()
                support.error_message('Product number is not on the list')
            
            else  :
                support.clean_screen()
                support.error_message()
            
        elif user_input_choice == "4":
            first_condition = True
            while first_condition :
                support.clean_screen()
                option.sort_by_option()
                user_input_choice = support.user_input_choice()
                
                if user_input_choice == '0':
                    support.clean_screen()
                    break
                
                elif user_input_choice =='1':
                    sort_product = general.products_filter(params='stock', order=False)
                    statement.pagination_product('stock', sort_product)
                
                elif user_input_choice == '2':
                    sort_product = general.products_filter(params='price', order=False)
                    page = 0
                    statement.pagination_product('price', sort_product)
                else :
                    support.error_message()
                    
        elif user_input_choice == "5":
            while True :
                support.clean_screen()
                option.filter_search_option()
                user_input_choice = support.user_input_choice()
                    
                if user_input_choice == '0':
                    support.clean_screen()
                    break
                    
                elif user_input_choice =='1':
                    product_name = support.user_input_choice("Enter product name : ")
                    filter_product = general.products_filter(product_name=product_name)
                    if len(filter_product) == 0 :
                        support.error_message(f" '{product_name}' is not exist ")
                    else :
                        statement.pagination_product(sort_type='name', sort_product=filter_product ,product_name=product_name)
                    
                elif user_input_choice == '2':
                    min_price = support.user_input_choice("Enter product min price : ")
                    max_price = support.user_input_choice("Enter product max price : ")
                    filter_product = general.products_filter(min_price=int(min_price), max_price=int(max_price))
                    statement.pagination_product(sort_type='name', sort_product=filter_product ,product_name=product_name)
                       
                else :
                        support.error_message()         
        else :
            support.error_message() 