#program 1
num=-1
if num >0:
    print(f"{num} is Positive Number")
else:
    print(f"{num} is Negative Number")

#program 2
num=11
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#program 3
base=5
power=2
print(base**power)

#program 4
num1=10
num2=10
if num1>num2:
    print("Num1 is Greater")
elif num1==num2:
    print("Num1 and Num2 are Equal")
else:
    print("Num2 is greater")

#program 5
year=2024
if year%4==0:
    print(f"{year} is Leap Year")
else:
    print(f"{year} is Not Leap Year")

#program 6
mark=82
if mark>=90 and mark<=100:
    print("Grade:A")
elif mark>=80 and mark<=89:
    print("Grade:B")
elif mark>=70 and mark<=79:
    print("Grade:C")
elif mark>=60 and mark<=69:
    print("Grade:D")
else:
    print("Grade:F")

#program 7
age=21
if age<16:
    print("You can't drive")
elif age>=16 and age<=17:
    print("You can drive not vote")
elif age>=18 and age<=24:
    print("You can vote but not rent acar")
else:
    print("You can do pretty much anything")

#proram 8
i=1
while i<=100:
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
    i=i+1

#program 9
year=int(input("Enter the Year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is Leap Year")
        else:
            print(f"{year} is Not Leap Year")
    else:
        print(f"{year} is Leap Year")
else:
    print(f"{year} is Not Leap Year")
















            
        
