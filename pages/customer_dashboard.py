import customer.balance as balance
import support.support as support
import customer.account as account
import customer.shopping_list as shop
import customer.shopping_cart as cart
import customer.purchase_history as history
import control.customer.customer_option as option



def customer_dashboard_menu(users):
    while True:
        option.customer_dashboard_option()
        user_input_choice = support.user_input_choice()
        
        if user_input_choice == "1":
            # support.loading_animation()
            account.account_info(users)
            
        elif user_input_choice == "2":
            # support.loading_animation()
            balance.balance_info(users)

        elif user_input_choice == "3":
            # support.loading_animation()
            shop.shopping_list(users)

        elif user_input_choice == "4":
            # support.loading_animation()
            cart.shopping_cart(users)
                
        elif user_input_choice == "5":
            # support.loading_animation()
            history.purchase_history(users)
            
        elif user_input_choice == "0":
            # support.loading_animation()
            break

        else:
            support.error_message()



    