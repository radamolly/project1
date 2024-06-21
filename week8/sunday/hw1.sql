show databases;
create database company;
use company;
create table employees(
	id int auto_increment primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(100) not null,
    hire_date date not null
);

insert into employees (first_name, last_name, email, hire_date) values ("John", "Doe", "john.doe@example.com", '2023-01-15');
insert into employees (first_name, last_name, email, hire_date) values ("Jane", "Smith", "jane.smith@example.com", '2023-02-20');

select id, first_name, last_name, email, hire_date from employees;

UPDATE employees
SET email = 'john.doe@company.com' 
where first_name = 'John' AND last_name = 'Doe';

DELETE FROM employees
WHERE first_name = 'Jane' AND last_name = 'Smith';