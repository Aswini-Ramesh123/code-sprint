SELECT * FROM new_schema.`employee info`;
use new_schema;
rename table `employee info` to employee_info;

#Task 1
select * from employee_info 
where Gender ='male' and Age <30 and  EverBenched = 'No' limit 5;

#Task 2
select avg(Age) as Avg_Emp from employee_info
where LeaveOrNot =1;

#TAsk 3
select Education,count(*) from employee_info where ExperienceInCurrentDomain>1 
group by Education;

#Task 4
select City,count(*) as Emp_Count ,dense_rank() over (order by count(*) desc) as Emp_Rank
from employee_info
group by City;

#Task 5
select City,
count(case when gender ='Male' then 'Male' end) as Male_Count,
count(case when gender ='Female' then 'Female' end) as Female_Count
from employee_info 
group by City;

#Task 6
select JoiningYear ,count(*) as no_of_emp,avg(ExperienceInCurrentDomain) as avg_exp from employee_info
group by JoiningYear;

#Task 7
select * from employee_info where City='Bangalore' 
and EverBenched = 'No' and PaymentTier=3
limit 5;

#Task 8
select count(case when LeaveOrNot=1 then 1 end)* 100 /count(*) as emp_count
from employee_info where EverBenched = 'Yes';

#TAsk 9
select Age,City,
case
when ExperienceInCurrentDomain <1 then 'Junior'
when ExperienceInCurrentDomain >=1 and ExperienceInCurrentDomain <3 then 'Mid'
else 'Senior'
end as Experience_Level
from employee_info
limit 10;

#Task 10
select EverBenched,LeaveOrNot,count(*) as no_of_emp from employee_info
group by EverBenched,LeaveOrNot;

#Task 11
select City,min(Age) as  youngest_employee 
from employee_info 
group by City;

#Task 12
select City,avg(Age) from employee_info
group by City
having avg(Age)> 30;

#TAsk 13
Select Age,City,
avg(Age) over (partition by City) as avg_age_in_city
from employee_info;

#Task 14
select City,Age,
case 
when Age<25 then 'Young'
when Age>=25 and Age<=35 then 'Adult'
when Age>35 then 'Senior'
end as Age_Group
from employee_info;

#Task 15
select * from employee_info where (ExperienceInCurrentDomain <2 and PaymentTier=3) or 
(Age > 30 and City='Pune');

#Task 16
select e.* from employee_info e
join(
select City,avg(PaymentTier) as avg_tier 
from employee_info
group by City) as c
on e.City = c.City
where e.PaymentTier > c.avg_tier;

#Task 17
select * from employee_info
where ExperienceInCurrentDomain is null or Education is null
or trim(ExperienceInCurrentDomain)='' or trim(Education)='';

select * from employee_info limit 100;

#Task 18
SET @top_n := CEIL((SELECT COUNT(*) * 0.20 FROM employee_info));
select Age, City
from (
SELECT Age, City, 
RANK() OVER (ORDER BY Age DESC) AS AgeRank
FROM employee_info
) AS ranked_employees
WHERE AgeRank <= @top_n;

#TAsk 19
select EverBenched,LeaveOrNot,count(*) as emp_count
from employee_info
group by EverBenched,LeaveOrNot;

#Task 20
select City,PaymentTier,count(*) from employee_info
group by City,PaymentTier;

#Task 21
select gender,count(*) as high_attrition_rate 
from employee_info
where LeaveOrNot=1
group by gender;

#Task 22
select Age,ExperienceInCurrentDomain from employee_info
where Age >30;

#Task 23
select joiningYear,count(*) as emp_count,
round(count(*)*100/(select count(*) from employee_info where LeaveOrNot = 0) ,2) as percent_of_Emp
from employee_info
where LeaveOrNot = 0
group by joiningYear;

#TAsk 24
select City,avg(ExperienceInCurrentDomain) as high_avg_experience from employee_info
where EverBenched='No'
group by City
order by high_avg_experience desc limit 1;

#Task 25
select ExperienceInCurrentDomain,
case when EverBenched = 'Yes' and ExperienceInCurrentDomain<3 then 'Yes'
else 'No'
end as LikelyToLeave
from employee_info limit 50;




