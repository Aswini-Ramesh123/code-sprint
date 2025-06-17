create database sprint;
show databases;
use sprint;
#Task 1
create table students(student_id int,
student_Name varchar(50),
grade char(10),
age varchar(3));
#Task2
alter table students add email varchar(50);
#Task_3
alter table students drop column grade;
#Task4
alter table students modify age varchar(3);
#Task 5
rename table students to studentdetails;
#Task 6
delete from studentdetails;
#Task7
create table Employees(Empid int,EmpName varchar(50),EmpSalary int);
#Task8
alter table Employees add Department varchar(40);
#Task9
drop table Employees;
#Task10
create table Products(product_id int,productName varchar(20),Price int);
#Task11
create table books(book_id int,author varchar(50),title varchar(50),publish_year int);
insert into books values (001,'alex','silent patient',1999);
#Task12 & 13
insert into books values(002,'Harper Lee','To Kill a Mockingbird',1960),
(003,'F. Scott Fitzgerald','The Great Gatsby',1925),
(004,'Jane Austen','Pride and Prejudice',1813),
(005,'J.D. Salinger','The Catcher in the Rye',1951),
(005,'Paulo Coelho','The Alchemist',1988),
(006,'Dan Brown','The Da Vinci Code',2003),
(007,'J.K.Rowling','Harry Potter and the Philosophers Stone',1997),
(008,'J.R.R.Tolkien','The Hobbit',1937),
(009,'Khaled Hosseini','The Kite Runner',2003),
(010,'Yuval Noah Harari','Sapiens: A Brief History of Humankind',2011);
select * from books;
#Task 14
select title, author from books;
#Task 15
select * from books;
#Task 16
delete from books where book_id=002;
#Task 17
create table Employees(employe_id int primary key,first_name varchar(50),last_name varchar(50),age int,department varchar(50),salary decimal(10,2));
#TAsk 18
insert into Employees values(1,'john','doe',30,'Hr',50000);
#Task 19 & 20
insert into Employees values(2,'jane','smith',25,'Finance',60000),
(3,'Alice','johnson',28,'IT',70000);
select * from Employees;
#TAsk 21
update Employees set salary=66000 where employe_id=2;
#Task 22
delete from employees where employe_id=3;
#Task 23
insert into Employees values(3,'michel','tayler',35,'sales',75000),
(4,'Emilys','Davis',40,'Marketing',80000);









