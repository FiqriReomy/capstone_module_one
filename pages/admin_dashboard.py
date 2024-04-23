import support.support as support
import admin.sales_record as record
import admin.product_list as product
import admin.customer_list as customer
import control.admin.admin_option as option


def admin_dashboard_menu(users):
    while True:
        option.admin_dashboard_option()
        user_input_choice = support.user_input_choice()

        if user_input_choice == "1":
            # support.loading_animation()
            product.product_list()

        elif user_input_choice == "2":
            # support.loading_animation()
            customer.customer_list()

        elif user_input_choice == "3":
            # support.loading_animation()
            record.sales_record()

        elif user_input_choice == "0":
            # support.loading_animation()
            break

        else:
            support.error_message()