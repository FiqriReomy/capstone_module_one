import math
import config.config as cf
import support.support as support
import control.admin.admin_option as option
import control.general.general_control as general

def pagination_product(sort_type='name', sort_product=cf.products, product_name=None):
    # support.clean_screen()
    sort_product
    page = 0
    while True :
            current_page = (page // 5) + 1
            total_page = math.ceil(len(sort_product) / 5)
            general.show_product_list(sort_product, page, total_page)
            option.pagination_option(page, current_page, total_page)
            user_input_choice = support.user_input_choice()

            if user_input_choice == '0':
                break
            
            elif user_input_choice == "1":
                page = 0
                support.clean_screen()
            
            elif user_input_choice == "2":
                page = math.ceil(len(sort_product)) - 1
                support.clean_screen()
                        
            elif user_input_choice == "3":
                sort_product = general.products_filter(params=sort_type, order=False,product_name=product_name)
                support.clean_screen()
                        
            elif user_input_choice == "4":
                sort_product = general.products_filter(params=sort_type, order=True, product_name=product_name)
                support.clean_screen()
                               
            elif user_input_choice == "5" and current_page < total_page :
                page += 5
                support.clean_screen()
                            
            elif user_input_choice == "6" and current_page  > 1 :
                page -= 5
                support.clean_screen()
                            
            else :
                support.clean_screen()
                support.error_message()
                        
                        
                    