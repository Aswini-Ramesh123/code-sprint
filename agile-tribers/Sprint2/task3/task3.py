#program 1
try:
    def safe_divide(a,b):
        return a/b
    res=safe_divide(10,0)
    print(res)
except ZeroDivisionError:
    print("can't divisible by zero")

#program 2
try:
    num=int(input("Enter Number:"))
    string=input("Enter String:")
    convert=int(string)
    divide=num/convert
    print(divide)
except ValueError:
    print("can't change a string into number")
except ZeroDivisionError:
    print("can't divisible by zero")

#program 3
def read_files():
    try:
        f=open("data.txt","r")
        content=f.read()
        print(content)
    except FileNotFoundError:
        print("File is not found")
    except IOError:
        print("IO error")
    finally:
        f.close()
        print("File closed")
read_files()

#program 4
class AgeError(Exception):
    pass
try:
    age=int(input("Enter Age:"))
    if age<18:
        raise AgeError("You must be atleast 18 years old")
except AgeError as e:
    print("caught:",e)

#program 5
try:
    num1=int(input("Enter Number 1:"))
    num2=int(input("Enter Number 2:"))
    divide=num1/num2
except ZeroDivisionError:
    print("Cant divisible by zero")
except ValueError:
    print("Invalid input")
else:
    print("Operation successful")

#program 6
def validate_password(password):
        letters=any(char.isalpha() for char in password)
        numbers=any(char.isdigit() for char in password)
        if len(password)<8:
            raise ValueError("Password must be atleast 8 characters")
        if not(letters and numbers):
            raise ValueError("Password doesn't contain both letters and numbers")   
try:      
    validate_password("1234as")
except ValueError as e:
    print(e)
try:
    validate_password("asdfghjk")
except ValueError as e:
    print(e)
try:
    validate_password("abcdef678")
except ValueError as e:
    print(e)

#program 7
import logging
logging.basicConfig(filename="error_log.txt",level=logging.ERROR,force=True)
try:
    num1=10
    num2=0
    divide=num1/num2
    print(divide)
except ZeroDivisionError as e:
    logging.error(f"Error Occur:{e}")

#program 8
def outer_function():
    try:
        def inner_function():
            num=10/0
            print(num)
        inner_function()
    except ZeroDivisionError as e:
        print(f"Error occur:{e}")      
outer_function()

#program 9
def read_file(filename):
    try:
        with open(filename,"r") as f:
            content=f.read()
            print(content)
    except FileNotFoundError:
        print("File is not found")
filename=input("Enter filename:")
read_file(filename)

#program 10
try:
    num=int(input("Enter a Number:"))
    print("No error occurs")
except Exception:
    print("Invalid input")

#program 11
name=input("Enter name:")
age=int(input("Enter age:"))
print(f"Hello {name},you are {age} years old!")

#program 12
def float_number(num):
    print(f"Floating number with 2 decimal points:{num:.2f}")
float_number(67.5678)

#program 13
items=[
    ("Apples","20rs"),
    ("Mangoes","30rs"),
    ("Cherries","45rs"),
    ("Grapes","78rs"),
    ("Oranges","10rs")]
print("Items".ljust(10) + "Price".rjust(10))
print("-" *20)
print()
for item,price in items:
    print(item.ljust(10) + price.rjust(10))
#program 14
person={
    "name":"John",
    "age":30,
    "city":"New York"
    }
print("{name} is {age} years old and lives in {city}".format(**person))

#program 15
def number(num):
    print("{:,}".format(num))
number(1000000)

#program 16
def validate_password(password):
        letters=any(char.isalpha() for char in password)
        numbers=any(char.isdigit() for char in password)
        if len(password)<8:
            raise ValueError(f"Error: The Password {password} is too short.It must be atleast 8 characters long")
try:      
    validate_password("123")
except ValueError as e:
    print(e)

#program 17
from datetime import datetime
date_time=datetime.now()
print(date_time.strftime("Today is %B %d,%Y, and the time is %I:%m %p"))

#program 18
name="John"
age=30
email="john@gmail.com"
print(f'''name={name},
age={age},
email={email}'''

#program 19
with open("students.txt","w") as f:
    f.write("Chol\n")
    f.write("Kim\n")
    f.write("Jhope\n")
with open("students.txt","r") as f:
    content=f.read()
    print(content)

#program 20
def read_and_append(filename,text):
    with open(filename,"a") as f:
        f.write(text)
    with open(filename,"r") as f:
        content=f.read()
        print(content)
read_and_append("students.txt","Hello,im a new student Jimin")
























        
