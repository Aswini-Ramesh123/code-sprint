use sprint;
create table student(s_id int primary key,
s_name varchar(50),
s_age int,
class varchar(10));
create table mark(mark_id int primary key,
s_id int,
constraint fk foreign key(s_id) references student(s_id),
sub varchar(10),
marks int);
INSERT INTO student VALUES
(1, 'Alice', 14, '8A'),                
(2, 'Bob', 15, '9B'),                   
(3, 'Charlie', 13, '7A'),               
(4, 'David', 14, '8B'),                 
(5, 'Eva', 15, '9A');  
INSERT INTO mark VALUES
(1, 1, 'Math', 85),                   
(2, 2, 'Science', 78),               
(3, 3, 'English', 90),                 
(4, 4, 'History', 88),                 
(5, 5, 'Geography', 92); 
drop table mark;
#Task 1 inner join
select s.s_name,m.sub,m.marks
from student as s
inner join mark as m
on s.s_id=m.s_id;

#Task 2
select s.s_name from student as s
inner join mark as m
on s.s_id=m.s_id;

#TAsk 3
select s.s_name,m.sub,m.marks from student as s
inner join mark as m
on s.s_id=m.s_id
where m.sub = 'math';

#Task 4
select s.s_name,m.sub,m.marks from student as s
inner join mark as m
on s.s_id=m.s_id and m.marks>85;

#Task 5
select s.s_name,m.sub from student as s
inner join mark as m
on s.s_id=m.s_id 
order by s.s_name;

#Task 6 Left join
select s.s_name,m.sub,m.marks from student as s
left join mark as m
on s.s_id=m.s_id; 

#TAsk 7
select s.s_name,m.sub,m.marks from student as s
left join mark as m
on s.s_id=m.s_id; 

#TAsk 8
select s.s_name,m.sub,m.marks from student as s
left join mark as m
on s.s_id=m.s_id; 

#TAsk 9
select s.s_name,m.sub,m.marks
from student as s
left join mark as m
on s.s_id=m.s_id 
where s.s_age > 14;

#Task 10 right join
select s.s_name,m.marks from student as s
right join mark as m
on s.s_id=m.s_id;

#Task 11
select s.s_name,m.sub
from student as s
right join mark as m
on s.s_id=m.s_id;

#Task 12
select s.s_name,m.sub
from student as s
right join mark as m
on s.s_id=m.s_id;

#Task 13
select s.s_name,m.sub,m.marks
from student as s 
inner join mark as m
on s.s_id = m.s_id
where m.sub ='English';

#Task 14
select m.mark_id,m.sub,m.marks,s.s_name
from student as s 
right join mark as m
on s.s_id = m.s_id;

#Task 15 full join
select s.s_name,m.marks
from student as s
left join mark as m
on s.s_id = m.s_id
union
select s.s_name,m.marks
from student as s
right join mark as m
on s.s_id = m.s_id;

#Task 16
select s.s_name,m.sub,m.marks
from student as s
left join mark as m
on s.s_id = m.s_id
union
select s.s_name,m.sub,m.marks
from student as s
right join mark as m
on s.s_id = m.s_id;

#Task 17
select s.s_name,m.sub,m.marks
from student as s
left join mark as m
on s.s_id = m.s_id
union
select s.s_name,m.sub,m.marks
from student as s
right join mark as m
on s.s_id = m.s_id;

drop table student;
drop table mark;
alter table mark drop foreign key fk;
select * from student;
select * from mark;
delete from mark where s_id =6;
delete from student where s_id =6;