import pages.login as login
import support.support as support
import control.general.general_option as option


while True :
    option.main_menu_option()
    user_input_choice = support.user_input_choice()

    if user_input_choice == "0":
        support.clean_screen()
        support.success_message("Thank you for using our application")
        break

    elif user_input_choice == "1":
        support.clean_screen()
        login.login_menu()
        
    else :
        support.error_message()
            

