import support.support as support
import control.customer.customer_control as control
import control.customer.customer_option as cart_menu

checkout_cart = list()

def shopping_cart(users):
    global checkout_cart
    while True:
        user_cart = control.get_user_cart(users)
      
        if len(user_cart) == 0 :
            support.clean_screen()
            support.error_message('Your cart is empty') 
            break
        else :
            control.show_cart(user_cart)
            cart_menu.cart_menu_option()
            user_input_choice = support.user_input_choice()
            isdigits, value = support.input_check(user_input_choice)
            
            if isdigits and value == 1:
                checkout = True
                while checkout:
                    support.clean_screen()
                    control.show_cart(user_cart)
                    user_input_choice = support.user_input_choice('Select product number or 0 cancel :')
                    isdigits, value = support.input_check(user_input_choice)
                
                    if isdigits and value <= len(user_cart) and value != 0 :

                        previous_cart = len(checkout_cart)
                        checkout_cart = control.checkout_check(checkout_cart, user_cart, value)
                        if len(checkout_cart) == previous_cart:
                            support.error_message('Number already selected as a checkout item')  
                    
                        else :
                            while True :
                                support.clean_screen()  
                                total_amount = control.show_checkout(checkout_cart)
                                user_input_choice = support.user_input_choice('Press (1) to proceed or (0) to checkout cart :')
                                if user_input_choice == '0' :
                                    break
                            
                                elif user_input_choice == '1':
                                    balance = support.get_balance_info(users)
                                
                                    if balance['balance'] <= total_amount :
                                        support.error_message('Insufficient Funds !!! Top up your balance')
                                        checkout_cart = list()
                                        checkout = False
                                        break
                                    
                                    else :
                                        balance['balance'] -= total_amount
                                        control.remove_checkout_item(checkout_cart[0])
                                        control.update_product_sold(checkout_cart)
                                        support.add_balance(balance, total_amount, 'remove')
                                        control.update_purchase_history(checkout_cart)
                                        support.success_message("Purchase is success, Your Balance :", balance['balance'])
                                        checkout = False
                                        break
                                else :
                                    support.error_message()
                                    
                    elif isdigits and value == 0 :
                        checkout_cart = list()
                        checkout = False
                        break
                        
                    elif isdigits and value > len(user_cart) :
                        support.error_message("The number is out of list")
                    
                    else :
                        support.error_message()
                        
            elif isdigits and value == 2:
                while True :
                    user_input_choice = support.user_input_choice('Select product number you want remove from cart or 0 to cancel:')
                    isdigits, value = support.input_check(user_input_choice)
                    
                    if isdigits and value == 0:
                        support.clean_screen()
                        break
                    
                    elif isdigits and value > 0 and value <= len(user_cart): 
                        selected_item = user_cart[value-1]
                        control.remove_checkout_item(selected_item)
                        control.update_product_quantity(selected_item, users[0]['user_id'])
                        select_product = user_cart[value - 1]
                        control.update_user_cart(select_product,user_cart, 0, 'remove')
                        support.success_message("Item is deleted from cart")
                        support.clean_screen()
                        checkout = False
                        break
                        
                    elif isdigits and value > len(user_cart):
                        support.error_message('Item is out of list')

                    else :
                        support.error_message()
                    
                
            elif isdigits and value == 0 :
                support.clean_screen()
                break
                
            else :
                support.error_message()
