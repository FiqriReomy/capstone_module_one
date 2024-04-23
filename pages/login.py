import support.support as support
import pages.admin_dashboard as admin
import pages.customer_dashboard as customer

def login_menu():
    while True :
        username, password = support.login_menu_input()
        result, message  = support.user_role_check(username,password)
       
        if result == False and message == False:
            break
        
        elif result == "1":
            support.clean_screen()
            support.error_message(message)
        
        elif result == "2" :
            support.clean_screen()
            support.error_message(message)

        elif result == "3":
            support.clean_screen()
            customer.customer_dashboard_menu(message)

        elif result == "4":
            support.clean_screen()
            admin.admin_dashboard_menu(message)

        else :
            support.error_message()

