#program 1

def fn(n):
    return n**3
cube=fn(5)
print("Cube value is :",cube)

#program 2
while True:
    num=int(input("Enter a Number:"))
    if num<0:
        break
    else:
        print("Cube of the Number is:",num**3)

#program 3
num=20
for i in range(1,num+1):
    if i%2!=0:
        continue
    else:
        print(i)

#program 4
total=0
while True:
    num=int(input("Enter the Number:"))
    if num<0:
        continue
    elif num==0:
        break
    else:
        total=total+num
print("Sum is:",total)

#program 5
def fn1():
    n=5
    res=n**2
    print("Square is:",res)
fn1()

#program 6
count=0
def fun():
    global count
    count+=1    
fun()
fun()
print(count)

#program 7
x=10
def fns():
    def fn1():
        y=20
        print("Y is:",y)
    fn1()
    print("X is:",x)
fns()   
#program 8
fruits=("apple","banana","cherry")
print("Second Element is:",fruits[1])
list_fruits=list(fruits)
list_fruits[1]="orange"
result=tuple(list_fruits)
print(result)


#program 9
set1={1,2,3,4,5}
set2={4,5,6,7,8}
a=set1&set2
print("Intersection is:",a)
b=set1|set2
print("Union is:",b)
c=set1-set2
print("Difference is:",c)
set1.add(6)
print("After adding")
print("Set1 is:",set1)
set2.discard(8)
print("After removing")
print("Set2 is:",set2)
num=int(input("Enter a Number:"))
if num in set1:
    print("Yes,The number in set1")
else:
    print("No,The number not in set1")


#program 10
a=(1,2,3,4,5,6)
print("Third Element is:",a[2])
b=set(a)
b.add(7)
print(b)

#program 11
a=[1,2,3,1,4,2,5]
b={1,2,3}
val1=set(a)
print("Unique Elements of original list:",val1)
c=val1&b
print("Intersection of a and b is:",c)
d=val1|b
print("Union of a and b is:",d)



#program 12
num_list=[10,20,30,40,50]
num_list.append(60)
modify=tuple(num_list)
print("Tuple is:",modify)
convert_set=set(modify)
print("Set is:",convert_set)


        
        
