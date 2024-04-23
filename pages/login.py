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
            support.error_message(message)
        
        elif result == "2" :
            support.error_message(message)

        elif result == "3":
            # support.loading_animation()
            customer.customer_dashboard_menu(message)

        elif result == "4":
            # support.loading_animation()
            admin.admin_dashboard_menu(message)

        else :
            support.error_message()

