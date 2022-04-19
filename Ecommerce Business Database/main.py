from sql_funcs import *


def add_customer_from_user_input():
    customer_id = input("Enter the customer id (PK) unique:  ")
    first_name = input("Enter the customers first name:  ")
    last_name = input("Enter the customers last name:  ")
    customer_email = input("Enter the customer email:  ")
    customer_address = input("Enter the customer address:  ")
    phone = input("Enter the customer phone number:  ")
    status = add_customer(customer_id, first_name, last_name, customer_email, customer_address, phone)
    if status == 0:
        print(f'{first_name} {last_name},{customer_email},{customer_address} and {phone} added to the DB with CustomerId = {customer_id}')
    input('Hit Enter to Continue\n\n')


def add_product_from_user_input():
    product_id = input("Enter product id:  ")
    vendor_id = input("Enter vendor id:  ")
    product_quantity = input("Enter product quantity:  ")
    product_price = input("Enter product price:  ")
    product_description = input("Enter product description:  ")
    add_product(product_id, vendor_id, product_quantity, product_price, product_description)


def add_vendor_from_user_input():
    vendor_id = input("Enter vendor id:  ")
    vendor_name = input("Enter vendor name:  ")
    vendor_email = input("Enter vendor email:  ")
    vendor_number = input("Enter vendor number:  ")
    add_vendor(vendor_id, vendor_name, vendor_email, vendor_number)


def add_order_from_user_input():
    order_id = input("Enter order id:  ")
    print("Enter order date:  ")
    order_date = get_date()
    customer_id = input("Enter customer id:  ")
    order_status = input("Enter order status:  ")
    product_id = input("Enter product_id:  ")
    quantity = input("Enter quantity of product:  ")
    add_order(order_id, order_date, customer_id, order_status, product_id, quantity)


def add_invoice_from_user_input():
    invoice_id = input("Enter invoice id:  ")
    order_id = input("Enter order id:  ")
    print("Enter shipment date:  ")
    shipment_date = get_date()
    shipping_address = input("Enter shipping address:  ")
    add_invoice(invoice_id, order_id, shipment_date, shipping_address)


def place_order_from_user_input():
    invoice_id = input("Enter invoice id:  ")
    print("Enter shipment date:  ")
    shipment_date = get_date()
    customer_id = input("Enter customer id:  ")
    product_id = input("Enter product id:  ")
    quantity = input("Enter quantity of product:  ")
    place_order(invoice_id, shipment_date, customer_id, product_id, quantity)
    display_invoice(invoice_id)


def remove_customer_from_user_input():
    customer_id = input("Enter the customer id: ")
    remove_customer_record(customer_id)


def remove_product_from_user_input():
    product_id = input("Enter the product id: ")
    remove_product_record(product_id)

def remove_vendor_from_user_input():
    vendor_id = input("Enter the vendor id: ")
    remove_vendor_record(vendor_id)


def remove_order_from_user_input():
    order_id = input("Enter the order id: ")
    remove_order_record(order_id)


def remove_invoice_from_user_input():
    invoice_id = input("Enter invoice id: ")
    remove_invoice_record(invoice_id)

def update_customer_from_user_input():
    current_customer_name = input("Enter the current customer id:  ")
    new_customer_name = input("Enter the new customer email:  ")
    update_customer(current_customer_name, new_customer_name)
    print(f'Customer email was updated to {new_customer_name}')

def list_records_in_table():
    table_name = input("Enter the table name:  ")
    record_list = get_all(table_name)
    for record in record_list:       
        print(record)

def display_invoice(invoice_id):
    invoice = get_invoice(invoice_id)
    order = get_order(invoice[1])
    print("Invoice")
    print("===========================")
    print("Invoice ID:", invoice[0])
    print("Order ID:", invoice[1])
    print("Shipment Date:", invoice[2])
    print("Shipping Address:", invoice[3])
    print("Customer ID:", order[2])
    print("Product ID:", order[4])
    print("Quantity:", order[5])
    print("===========================")

   

def display_main_menu():
    print("MENU: ")
    print("1.  Add Record")
    print("2.  Remove Record")
    print("3.  List Records")
    print("4.  Update Customer email")
    print("5.  Place Order")
    print("6.  Quit")

def display_add_menu():
    print("ADD MENU: ")
    print("1.  Add Customer")
    print("2.  Add Product")
    print("3.  Add Vendor")
    print("4.  Add Orders")
    print("5.  Add Invoice")
    print("6.  return to main menu")

def display_remove_menu():
    print("REMOVE MENU: ")
    print("1.  Remove Customer")
    print("2.  Remove Product")
    print("3.  Remove Vendor")
    print("4.  Remove Order")
    print("5.  Remove Invoice")
    print("6.  return to main menu")

def get_date() -> str:
    year = input("\tYear: ")
    month = input("\tMonth: ")
    day = input("\tDay: ")
    return f"{year}-{month}-{day}"


def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice:  ")
        if choice == '1':
            display_add_menu()
            choice = input("Enter your choice:  ")
            if choice == "1":
                add_customer_from_user_input()
            elif choice == "2":
                add_product_from_user_input()
            elif choice == "3":
                add_vendor_from_user_input()
            elif choice == "4":
                add_order_from_user_input()
            elif choice == "5":
                add_invoice_from_user_input()
            else: continue
        elif choice == "2":
            display_remove_menu()
            choice = input("Enter your choice:  ")
            if choice == "1":
                remove_customer_from_user_input()
            elif choice == "2":
                remove_product_from_user_input()
            elif choice == "3":
                remove_vendor_from_user_input()
            elif choice == "4":
                remove_order_from_user_input()
            elif choice == "5":
                remove_invoice_from_user_input()
            else: continue
        elif choice == "3":
            list_records_in_table()
        elif choice == "4":
            update_customer_from_user_input()
        elif choice == "5":
            place_order_from_user_input()
        elif choice == "6":
            break
        else:
            print("Invalid Choice.  Try Again.")


if __name__ == '__main__':
    main()