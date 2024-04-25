import support.support as support
import control.customer.customer_option as option
import control.customer.customer_control as control

def account_info(users):
    while True :
        option.account_info_option()
        user_input_choice = support.user_input_choice()
        
        if user_input_choice == "0":
            break
    
        elif user_input_choice == '1':
            support.clean_screen()
            support.success_message('Your username :', users[0]['username'])
        
        elif user_input_choice == '2':
            oldpassword = support.user_input_choice("Input your old password or 0 to cancel: ")
            result, message = support.user_role_check(users[0]['username'], oldpassword )
            
            if result == "2" and oldpassword == "0":
                support.clean_screen()
            
            elif result == "2":
                support.error_message(message)
            
            else :
                while True :
                    newpassword = support.user_input_choice("Input your new password : ")
                    command = support.user_input_choice("Are you sure ? 1. Proceed or 0. Re-input")
                    
                    if command == "1" and len(newpassword) >= 8:
                        message = control.update_account_info(users[0], newpassword)
                        support.success_message(message)
                        break
                    
                    if command == "1" and len(newpassword) < 8:
                        support.error_message('Password must be more than 8 characters')
                        break
                    
                    elif command == '0' :
                        support.clean_screen()
                        
                    else :
                        support.error_message()
        else :
            support.error_message()
                        

                             
            
