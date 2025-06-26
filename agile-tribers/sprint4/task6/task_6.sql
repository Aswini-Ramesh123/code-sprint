use sprint;
CREATE TABLE Library (
  book_id INT PRIMARY KEY,
  title VARCHAR(100),
  author VARCHAR(100),
  genre VARCHAR(50),
  price INT,
  publish_year INT,
  copies INT
);

INSERT INTO Library (book_id, title, author, genre, price, publish_year, copies) VALUES
(1, 'The Silent Patient', 'Alex Michaelides', 'Thriller', 350, 2019, 5),
(2, 'Becoming', 'Michelle Obama', 'Biography', 500, 2018, 2),
(3, 'Atomic Habits', 'James Clear', 'Self-help', 400, 2018, 4),
(4, 'The Alchemist', 'Paulo Coelho', 'Fiction', 300, 1988, 6),
(5, 'It Ends With Us', 'Colleen Hoover', 'Romance', 275, 2016, 3),
(6, 'Rich Dad Poor Dad', 'Robert Kiyosaki', 'Finance', 450, 2000, 1),
(7, 'The Power of Habit', 'Charles Duhigg', 'Self-help', 380, 2012, 5),
(8, 'The Psychology of Money', 'Morgan Housel', 'Finance', 450, 2020, 4),
(9, 'Verity', 'Colleen Hoover', 'Thriller', 350, 2018, 2),
(10, 'Outliers', 'Malcolm Gladwell', 'Self-help', 360, 2008, 3);

#Task 1
select * from Library where price =(
select max(price) from Library);

#Task 2
select * from Library where publish_year <(
select avg(publish_year) from Library);

#TAsk 3
select * from Library where copies >(
select copies from Library where title='Becoming');

#Task 4
select * from Library where genre =(
select genre from Library where title='Atomic Habits');

#Task 5
select * from Library where copies <(
select min(copies) from Library where genre='Self-help');

#Task 6
select * from Library where price in (
select price from Library 
group by price 
having count(*) > 1);

#Task 7
select * from Library where publish_year =(
select  min(publish_year) from Library);

#Task 8
select * from Library where author in(
select author from Library 
group by author
having count(*) >1);

#Task 9
select * from Library where price >(
select avg(price) from Library);

#Task 10
select * from Library where publish_year =(
select publish_year from Library where title = 'The Power of Habit');




