import support.support as support
import control.customer.customer_control as control

def purchase_history(users) :
    
    user_history = control.get_user_history(users[0]['user_id'])
    
    while len(user_history) == 0:
        support.success_message('You dont have any purchase history !!')
        break
        
    while user_history :
        control.show_user_history(user_history)
        user_input_choice = support.user_input_choice('0. Back to Main Menu')
        
        if user_input_choice == '0':
            break
        
        else :
            support.error_message()
            
        
        
        
    