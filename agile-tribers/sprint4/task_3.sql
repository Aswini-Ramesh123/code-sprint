show databases;
use sprint;
create table employee(employee_id int,first_name varchar(50),last_name varchar(50),department varchar(50),salary  int,hire_date date);
insert into employee values(1,'Alice','Smith','Engineering',	75000,'2018-03-01'),
(2,'Bob','Jones','HR',58000	,'2019-07-15'),
(3,'Charlie','Brown','Engineering',62000,'2020-01-10'),
(4,'David','Wilson','Sales',49000,'2017-05-21'),
(5,'Eva','Taylor','HR','54000','2021-11-30'),
(6,'Frank','Anderson','Engineering',88000,'2016-09-05'),
(7,'Grace','Thomas','Marketing',45000,'2022-02-14'),
(8,'Hannah','Jackson','Sales',67000,'2015-08-08'),
(9,'Ian','White','Engineering',59000,'2019-12-23'),
(10,'Jane','Harris','HR',61000,'2020-06-18'),
(11,'Kyle','Martin','Marketing',53000,'2018-10-09'),
(12,'Lara','Thompson','Engineering',72000,'2017-01-27'),
(13,'Mike','Garcia','Sales',48000,'2021-04-11'),
(14,'Nina','Martinez','HR',55000,'2022-07-06'),
(15,'Oscar','Robinson','Marketing',66000,'2019-02-28');
drop table employee;
#Task 1
select department
from employee
group by(department)
having avg(salary) > 60000;
#Task 2
select department
from employee 
group by department
having avg(salary) > 55000 and count(*)>2;
#Task 3
select department
from employee
group by department
having sum(salary) > 50000;
#Task 4
select * from employee where salary > 45000;
#Task 5
select department 
from employee 
group by department
having count(*) >=3 and avg(salary) < 65000;
#Task 6
select * from employee 
order by first_name asc;
#Task 7
select * from employee
order by hire_date desc;
#Task 8
select employee_id,first_name,last_name,salary
from employee order by salary asc;
#Task 9
select department,sum(salary) as total_salary
from employee
group by department;
#Task 10
select department,avg(salary) as avg_salary
from employee
group by department;
#TAsk 11
select department,count(department) as department_count
from employee
group by department;
#Task 12
select department,max(salary) as highest_salary 
from employee
group by department;
#Task 13
select year(hire_date),sum(salary)
from employee
group by year(hire_date);