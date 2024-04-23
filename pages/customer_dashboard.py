
import support.support as support
import customer.balance as balance
import customer.account as account
import customer.shopping_cart as cart
import customer.shopping_list as shop
import customer.purchase_history as history
import control.customer.customer_option as option



def customer_dashboard_menu(users):
    while True:
        option.customer_dashboard_option()
        user_input_choice = support.user_input_choice()
        
        if user_input_choice == "1":
            support.clean_screen()
            account.account_info(users)
            
        elif user_input_choice == "2":
            support.clean_screen()
            balance.balance_info(users)

        elif user_input_choice == "3":
            support.clean_screen()
            shop.shopping_list(users)

        elif user_input_choice == "4":
            support.clean_screen()
            cart.shopping_cart(users)
                
        elif user_input_choice == "5":
            support.clean_screen()
            history.purchase_history(users)
            
        elif user_input_choice == "0":
            support.clean_screen()
            break

        else:
            support.error_message()



    