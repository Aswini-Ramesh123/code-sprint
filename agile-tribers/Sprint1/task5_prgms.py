#program 1
for i in range(1,11):
    print(i)

#program 2
for i in range(1,21):
    if i%2==0:
        print(i)

#program 3
for i in range(1,21):
    if i%2!=0:
        print(i)

#program 4
num=int(input("Enter Number:"))
fact=1
for i in range(1,num+1):
    fact=i*fact
print(fact)

#program 5
num=int(input("Enter Number:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print("The sum is:",sum)

#program 6
list1=[1,2,3,4,5]
sum=0
for i in list1:
    sum=sum+i
    avg=sum/5
print("Average is:",avg)

#program 7
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

#program 8
for i in range(1,6):
    print(i)

#program 9
for i in range(1,11):
    print(i)

#program 10
list1=[10,20,30,40,10]
if list1[0]==list1[-1]:
    print("True")
else:
    print("False")

#program 11
list1=[10,67,20,78,98,55,89,33,90]
for i in list1:
    if i%5==0:
        print(i)

#program 12
vowel=['a','e','i','o','u']
character=input("Enter character:")
if character in vowel:
    print(f"{character} is vowel")
else:
    print(f"{character} is consonant")

#program 13
even_count=0
odd_count=0
for i in range(10,56):
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Even count:",even_count)
print("Odd count:",odd_count)

#program 14
for i in range(1,26):
    if i%5==0:
        pass
    else:
        print(i)

#program 15
list1=[1,2,3,4,5]
fact=1
for i in list1:
    fact=fact*i
    print(fact)
    
#program 16
num1=10
num2=200
product=num1*num2
if product >500:
    sum=num1+num2
    print("Sum is:",sum)
else:
    print("Product is:",product)

#program 17
a=44
b=55
if a>b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")

#program 18
a=98
b=78
c=450
if a>b and a>c:
    print(f"{a} is greater")
elif b>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")

#program 19
x=[23,4,-6,23,-9,21,3,-45,-8]
pos_list=[]
neg_list=[]
for i in x:
    if i>0:
        pos_list.append(i)
    else:
        neg_list.append(i)
print("Positive Number:",pos_list)
print("Negative Number:",neg_list)
    
    


















































    
    
