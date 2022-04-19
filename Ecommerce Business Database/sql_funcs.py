#!/usr/bin/env python3

from mysql.connector import connect

hostname = "localhost"
user_name = "root"
pwd = "roottoor"


def execute_and_commit(query):
    # step1: create connection object
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        # step2: create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # step3: execute the statement
            mysql_cursor.execute(query)
            # step4: commit the changes
            mysql_connection_object.commit()

# checks if record primary key already exists
def check_if_pk_exists(table, pk):
    key = None
    if table == "customers": key = "customer"
    elif table == "orders" : key = "order"
    else: key = table
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        with mysql_connection_object.cursor() as mysql_cursor:
            query = f"""select * from ecommerce_project.{table}
                        where {key}_id = {pk};"""
            mysql_cursor.execute(query)
            for row in mysql_cursor:
                if row[0] != None:
                    print("primary key already exists")
                    return True
                else: 
                    return False


# get functions


def get_order(order_id) -> tuple:
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        with mysql_connection_object.cursor() as mysql_cursor:
            query = f"""select * from ecommerce_project.orders
                        where order_id = {order_id};"""
            mysql_cursor.execute(query)
            for row in mysql_cursor:
                if row[0] == None:
                    print("customer don't exist")
                else: 
                    return tuple(row)

def get_customer(customer_id) -> tuple:
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        with mysql_connection_object.cursor() as mysql_cursor:
            query = f"""select * from ecommerce_project.customers
                        where customer_id = {customer_id};"""
            mysql_cursor.execute(query)
            for row in mysql_cursor:
                if row[0] == None:
                    print("customer don't exist")
                else: 
                    return tuple(row)

def get_invoice(invoice_id) -> tuple:
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        with mysql_connection_object.cursor() as mysql_cursor:
            query = f"""select * from ecommerce_project.invoice
                        where invoice_id = {invoice_id};"""
            mysql_cursor.execute(query)
            for row in mysql_cursor:
                if row[0] == None:
                    print("customer don't exist")
                else: 
                    return tuple(row)


def get_all(table):
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        with mysql_connection_object.cursor() as mysql_cursor:
            get_record_list = f"""SELECT * from ecommerce_project.{table};"""
            mysql_cursor.execute(get_record_list)
            table =[]
            for row in mysql_cursor:
                table.append(row)
            return table
                


# add functions


def add_customer(customer_id, first_name, last_name, email_address, home_address, phone_number):
    if check_if_pk_exists("customers", customer_id) == True: return None
    add_record = f"""INSERT INTO ecommerce_project.customers 
                     (customer_id, first_name, last_name, email_address, home_address, phone_number) values
                     ("{customer_id}", "{first_name}", "{last_name}", "{email_address}", "{home_address}", "{phone_number}");"""
    execute_and_commit(add_record)

def add_vendor(vendor_id, vendor_name, vendor_email, vendor_number):
    if check_if_pk_exists("vendor", vendor_id) == True: return None
    add_record = f"""INSERT INTO ecommerce_project.vendor 
                     (vendor_id, vendor_name, vendor_email, vendor_number) values
                     ("{vendor_id}", "{vendor_name}", "{vendor_email}", "{vendor_number}");"""
    execute_and_commit(add_record)

def add_product(product_id, product_quantity, product_price, product_description, vendor_id):
    if check_if_pk_exists("product", product_id) == True: return None
    add_record = f"""INSERT INTO ecommerce_project.product 
                     (product_id, product_quantity, product_price, product_description, vendor_id) values
                     ("{product_id}", "{product_quantity}", "{product_price}", "{product_description}", "{vendor_id}");"""
    execute_and_commit(add_record)

def add_order(order_id, order_date, customer_id, order_status, product_id, quantity):
    if check_if_pk_exists("orders", order_id) == True: return None
    add_record = f"""INSERT INTO ecommerce_project.orders 
                     (order_id, order_date, customer_id, order_status, product_id, quantity) values
                     ("{order_id}", "{order_date}", "{customer_id}", "{order_status}", "{product_id}", "{quantity}");"""
    execute_and_commit(add_record)

def add_invoice(invoice_id, order_id, shipment_date, shipping_address):
    if check_if_pk_exists("invoice", invoice_id) == True: return None
    add_record = f"""INSERT INTO ecommerce_project.invoice 
                     (invoice_id, order_id, shipment_date, shipping_address) values
                     ("{invoice_id}", "{order_id}", "{shipment_date}", "{shipping_address}");"""
    execute_and_commit(add_record)


# Place order
# adds order and invoice
def place_order(order_id, order_date, customer_id, product_id, quantity):
    customer = get_customer(customer_id)
    add_order(order_id, order_date, customer_id, "about to be shipped", product_id, quantity)
    add_invoice(order_id, order_id, order_date, customer[4])


## remove functions


def remove_vendor_record(vendor_id):
    delete_product_record = f"DELETE FROM ecommerce_project.product WHERE vendor_id = {vendor_id};"
    delete_vendor_record = f"DELETE FROM ecommerce_project.vendor WHERE vendor_id = {vendor_id};"
    execute_and_commit(delete_product_record)
    execute_and_commit(delete_vendor_record)

def remove_product_record(product_id):
    delete_product_record = f"DELETE FROM ecommerce_project.product WHERE product_id = {product_id};"
    remove_order_from_product_id(product_id)
    execute_and_commit(delete_product_record)

def remove_customer_record(customer_id):  
    remove_order_from_customer_id(customer_id) 
    delete_customer_record = f"DELETE FROM ecommerce_project.customers WHERE customer_id = {customer_id};"
    execute_and_commit(delete_customer_record)

def remove_invoice_record(invoice_id):
    delete_invoice_record = f"DELETE FROM ecommerce_project.invoice WHERE invoice_id = {invoice_id};"
    execute_and_commit(delete_invoice_record)

def remove_order_record(order_id):
    delete_invoice_record = f"DELETE FROM ecommerce_project.invoice WHERE order_id = {order_id};"
    delete_order_record = f"DELETE FROM ecommerce_project.orders WHERE order_id = {order_id};"
    execute_and_commit(delete_invoice_record)
    execute_and_commit(delete_order_record)

def remove_order_from_customer_id(customer_id): 
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        with mysql_connection_object.cursor() as mysql_cursor:
            query = f"""select o.order_id from ecommerce_project.customers c 
                        inner join ecommerce_project.orders o 
                        on c.customer_id = o.customer_id
                        where o.customer_id = {customer_id};"""
            mysql_cursor.execute(query)
            for row in mysql_cursor:
                remove_order_record(row[0])

def remove_order_from_product_id(product_id): 
    with connect(host=hostname, user=user_name, password=pwd) as mysql_connection_object:
        with mysql_connection_object.cursor() as mysql_cursor:
            query = f"""select o.order_id from ecommerce_project.product p 
                        inner join ecommerce_project.orders o 
                        on p.product_id = o.product_id
                        where o.product_id = {product_id};"""
            mysql_cursor.execute(query)
            for row in mysql_cursor:
                remove_order_record(row[0])


# Update function


def update_customer(id_number, new_email):
    update_customername = f'UPDATE ecommerce_project.customers SET email_address = "{new_email}" WHERE customer_id = "{id_number}"'
    execute_and_commit(update_customername)

