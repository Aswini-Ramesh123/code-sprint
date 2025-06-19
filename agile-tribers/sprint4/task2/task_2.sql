show databases;
use sprint;
#Task1
create table employee(employee_id int,first_name varchar(50),last_name varchar(50),department varchar(20),salary decimal(8,2),hire_date date);
insert into employee values(1,'alice','smith','engineering',75000,'2018-03-01'),
(2,'bob','jones','hr',58000,'2019-07-15'),
(3,'charlie','brown','engineering',62000,'2020-01-10'),
(4,'david','wilson','sales',49000,'2017-05-21'),
(5,'eva','taylor','hr',54000,'2021-11-30'),
(6,'frank','anderson','engineering',88000,'2016-09-05'),
(7,'grace','thomson','marketing',45000,'2022-02-14'),
(8,'hannah','jackson','sales',67000,'2015-08-08'),
(9,'ian','white','engineering',59000,'2019-12-23'),
(10,'jane','harris','hr',61000,'2020-06-18'),
(11,'kyle','martin','marketing',53000,'2018-10-09'),
(12,'lara','thompson','engineering',72000,'2017-01-27'),
(13,'mike','garcia','sales',48000,'2021-04-11'),
(14,'nina','martinez','hr',550000,'2022-07-06'),
(15,'oscar','robinson','marketing',66000,'2019-02-28');
select sum(salary) total_salary_over_60000 from employee where salary >60000;
select avg(salary) avg_salary_all from employee;
select count(*) count_salary_under_55000 from employee where salary < 55000;
select max(salary) highest_saary from employee;
select min(salary) lowest_salary from employee;
select sum(salary) total_salary_hr from employee where department='hr';
select avg(salary) avg_salary_engineering from employee where department ='engineering';
select count(salary) count_salary_50000_to_70000 from employee where salary between 50000 and 70000;
select sum(salary) sum_salary_under_60000 from employee where salary <60000;
select avg(salary) avg_salary_over_60000 from employee where salary > 60000;
select * from employee;
drop table books;
create table books(book_id int,author varchar(50),title varchar(50),genre varchar(20),publish_year int,available_copies int);
INSERT INTO books VALUES
(001, 'alex', 'silent patient', 'Thirller', 2009, 5),
(002, 'Harper Lee', 'To Kill a Mockingbird', 'Thirller', 1960, 5),
(003, 'F. Scott Fitzgerald', 'The Great Gatsby', 'historical', 1925, 5),
(004, 'Jane Austen', 'Pride and Prejudice', 'fantacy', 2013, 1),
(005, 'J.D. Salinger', 'The Catcher in the Rye', 'adventure', 1951, 3),
(006, 'Paulo Coelho', 'The Alchemist', 'fantacy', 1848, 7),
(007, 'Dan Brown', 'The Da Vinci Code', 'fantacy', 2003, 4),
(008, 'J.K.Rowling', 'Harry Potter and the Philosophers Stone', 'adventure', 1997, 5),
(009, 'J.R.R.Tolkien', 'The Hobbit', 'fantacy', 1937, 3),
(010, 'Khaled Hosseini', 'The Kite Runner', 'Thirller', 2003, 2);
select * from books where publish_year between 1900 and 1950;
select * from books where available_copies between 4 and 7;
select * from books where publish_year between 1800 and 1900;
select * from books where book_id between 5 and 10;
select * from books where publish_year between 1850 and 1950 and available_copies >=5;
select * from books where title like 'the%';
select * from books where author like '%tolkien%';
select * from books where genre='fiction';
insert into books values(011,'leo tolstoy','war and peace','historical',1869,2);
select * from books where title like '%war%';
select * from books where author like '%tolstoy%';
select title as book_title,available_copies as copies from books ;
select * from books as B where available_copies >=5;
select title,author,publish_year as year_publish from books;
select title as book_title,author as book_author,available_copies as copies_in_stock from books;
select available_copies as stock,title,author from books where available_copies >4;
select * from books where book_id between 001 and 005;
select * from books order by publish_year desc limit 3;
select * from books where available_copies > 3 limit 7;
select * from books order by author limit 10;
select * from books where genre ='fantacy' limit 4;


