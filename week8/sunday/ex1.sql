show databases;
create database rada_cafe;
use rada_cafe;
create table employee(
	id int auto_increment primary key,
    name varchar(100) not null,
    salary decimal(10,2) not null
);
create table product(
	id int auto_increment primary key,
    name varchar(100) not null,
    catagory_id int not null,
    cost decimal(10,2) not null
);
create table catagories(
	id int auto_increment primary key,
    name varchar(100) not null
);
create table sales(
	id int auto_increment primary key,
    product_id int not null,
    employee_id int not null,
    cost decimal(10,2) not null,
    total decimal(10,2) not null
);

insert into catagories (name) values ("Food");
insert into catagories (name) values ("Beverage");
insert into catagories (name) values ("Gift");

insert into employee (name, salary) values ("Somchai", 10000);
insert into employee (name, salary) values ("Meow",12000);


insert into product (name, cost, catagory_id) values ("waffle", 40, 03);
insert into product (name, cost, catagory_id) values ("lemonade", 25, 01);

insert into sales (employee_id, product_id, cost, total) values (1, 002, 25, 25);
insert into sales (employee_id, product_id, cost, total) values (2, 003, 85, 85);

update employee set name = "Sompong" where id = 1;

delete from employee where id = 3;

-- select id, name from catagories;
-- select id, name, salary from employee;
-- select id, name, cost, catagory_id from product;
-- select id, employee_id, product_id, cost, total from sales;

select product.id, product.name, product.cost, catagories.name as catagory_name from product join catagories on product.catagory_id = catagories.id;
-- select sales.id, employee.name as employee_name, product.name as product_name, sales.cost, sales.total from sales join employee on sales.employee_id = employee.id join product on sales.product_id = product.id;

select s.id, e.name as employee_name, p.name as product_name, s.cost, s.total from sales s join employee e on s.employee_id = e.id join product p on s.product_id = p.id;
