use sprint;
create table orders(orderid int,customer varchar(20),country varchar(20),order_date date,amount decimal(10,2),order_status varchar(20));
INSERT INTO Orders (orderid, customer, country, order_date, amount, order_status) VALUES
(1, 'Alice Johnson', 'USA', '2024-12-01', 250.00, 'Shipped'),
(2, 'Bob Smith', 'UK', '2024-12-03', 120.50, 'Pending'),
(3, 'Charlie Lee', 'Canada', '2024-12-04', 89.99, 'Cancelled'),
(4, 'Diana Prince', 'USA', '2024-12-05', 300.00, 'Delivered'),
(5, 'Ethan Brown', 'Australia', '2024-12-06', 45.75, 'Shipped'),
(6, 'Fiona Davis', 'India', '2024-12-07', 600.00, 'Processing'),
(7, 'George Wilson', 'Germany', '2024-12-08', 155.00, 'Delivered'),
(8, 'Hannah Moore', 'France', '2024-12-09', 78.40, 'Pending'),
(9, 'Ian Taylor', 'USA', '2024-12-10', 200.00, 'Shipped'),
(10, 'Julia Martin', 'UK', '2024-12-11', 130.25, 'Cancelled'),
(11, 'Kevin Walker', 'Canada', '2024-12-12', 499.99, 'Delivered'),
(12, 'Laura Scott', 'India', '2024-12-13', 90.00, 'Processing'),
(13, 'Michael Young', 'Australia', '2024-12-14', 105.80, 'Shipped'),
(14, 'Nancy Hall', 'Germany', '2024-12-15', 62.00, 'Delivered'),
(15, 'Oliver King', 'USA', '2024-12-16', 315.45, 'Pending');

#Task 1
select *,
row_number() over (order by order_date) as row_num
from orders;

#TAsk 2
select * ,rank() over (partition by country order by amount desc) as rank_in_country
from orders;

#TAsk 3
select * ,dense_rank() over (partition by country order by amount desc) as rank_in_country
from orders;

#Task 4
select *,
ntile(4) over (partition by country order by amount rows between unbounded preceding and unbounded following) as bucket
from orders;

#Task 5
select *,
lead(amount) over (partition by country) as next_amount
from orders;

#Task 6
select *,
lag(amount) over (partition by country) as previous_amount
from orders;

#Task 7
select country,amount as first_amount from(
	select *,row_number() over (partition by country order by order_date) as row_num
from orders )as sub
where row_num=1;

#Task 8
select * from orders where year(order_date)= 2023;

#Task 9
select country,total_amount from(
	select *,sum(amount) over (partition by country) as total_amount,
	row_number() over (partition by country) as row_num from orders) as sub
    where row_num=1;

#Task 10
select country,avg_amount from
(select *,avg(amount) over (partition by country) as avg_amount,
row_number() over (partition by country) as row_num from orders)as sub
where row_num=1;

#Task 11
select country,total_orders from(
select *,count(country) over (partition by country) as total_orders,
row_number() over (partition by country order by order_date) as row_num from orders) as sub
where row_num=1;

#TAsk 12
select *,row_number() over (partition by country order by order_date) as row_num
from orders;

#Task 13
select *,cume_dist() over (partition by country order by amount) as cumilative
from orders;

#Task 14
select *,percent_rank() over (partition by country order by amount) as percetile_rank from orders;

#Task 15
select *,amount - lag(amount) over (partition by country order by order_date)
as diff_with_previous from orders;

#Task 16
select *,sum(amount) over (partition by country order by order_date) as running_total
from orders;

#Task 17
select * from
(select *,rank() over (partition by country order by order_date) as tot_country
from orders)as sub
where tot_country <=3;

#Task 18
select * from orders where amount > 100 and order_status = 'shipped';

#Task 19
select customer,count(customer) over (partition by customer) as total_order
from orders;

#Task 20
select *,dense_rank() over(partition by country,order_status order by amount)as rank_country_status
from orders;

select * from orders;
