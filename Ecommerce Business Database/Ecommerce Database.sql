drop database ecommerce_project;

CREATE database ecommerce_project;
use ecommerce_project;
 
 CREATE table customers(
 customer_id int NOT NULL primary key,
 first_name varchar(60) NOT NULL,
 last_name varchar(60) NOT NULL,
 email_address varchar(70),
 home_address varchar(90),
 phone_number varchar(40)
 );
 
 CREATE table vendor(
 vendor_id int NOT NULL primary key,
 vendor_name varchar(60),
 vendor_email varchar(60),
 vendor_number varchar(60)
 );
 
  CREATE table product(
 product_id int NOT NULL primary key,
 product_quantity int NOT NULL,
 product_price DECIMAL(5,2) NOT NULL,
 product_description VARCHAR(70),
 vendor_id int NOT NULL,
 foreign key (vendor_id) references vendor (vendor_id)
 );
 
 CREATE table orders(
order_id int NOT NULL primary key,
order_date date NOT NULL, /* yyyy-mm-dd */
customer_id int NOT NULL,
order_status varchar(60),
foreign key (customer_id) references customers (customer_id),
product_id int not null,
foreign key (product_id) references product (product_id),
quantity int not null
);

CREATE table invoice(
invoice_id int NOT NULL primary key,
order_id int NOT NULL,
shipment_date date NOT NULL, /* yyyy-mm-dd */
shipping_address VARCHAR(90),
foreign key (order_id) references orders (order_id)
);
