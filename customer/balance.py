import support.support as support
import control.customer.customer_option as option
import control.customer.customer_control as control

def balance_info(users):
    while True :
        option.balance_info_option()
        balance = support.get_balance_info(users)
        user_input_choice = support.user_input_choice()
        
        if user_input_choice == "0":
            break
    
        elif user_input_choice == '1':
            support.clean_screen()
            support.success_message('Your balance is : ', balance['balance'])
        
        elif user_input_choice == '2':
            topup_amount = support.user_input_choice("Enter amount of top up : ")
            result, message = control.amount_verification(topup_amount)
            
            if result == True  :
                support.clean_screen()
                support.add_balance(balance, topup_amount)
                support.success_message(message)
            
            elif result == False  :
                support.error_message(message)
                support.clean_screen()
                
            else :
                support.error_message(message)
                support.clean_screen()
                        
        else :
            support.error_message()
            support.clean_screen()
            
