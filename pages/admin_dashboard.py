import support.support as support
import admin.product_list as product
import control.admin.admin_option as option


def admin_dashboard_menu(users):
    while True:
        option.admin_dashboard_option()
        user_input_choice = support.user_input_choice()

        if user_input_choice == "1":
            support.clean_screen()
            product.product_list()

        elif user_input_choice == "0":
            support.clean_screen()
            break

        else:
            support.clean_screen()
            support.error_message()