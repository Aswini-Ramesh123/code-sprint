#Program 1
num1=int(input("Number1:"))
num2=int(input("Number2:"))
product=num1*num2
if product > 500:
    print("Sum is:",num1+num2)
else:
    print("Product is:",product)

#program 2
a=12
b=20
c=9
if a>b and a>c:
    print("A is Greater")
elif b>c and b>a:
    print("B is Greater")
else:
    print("C is Greater")

#program 3
list1 = [1, 2, 2, 3, 4, 1]
list2 = []
if list1:
    if list1[0] not in list2:
        list2.append(list1[0])
    if list1[1] not in list2:
        list2.append(list1[1])
    if list1[2] not in list2:
        list2.append(list1[2])
    if list1[3] not in list2:
        list2.append(list1[3])
    if list1[4] not in list2:
        list2.append(list1[4])
    if list1[5] not in list2:
        list2.append(list1[5])
print(list2) 

#program 4
nums=[3,2,2,3]
num=nums.copy()
original_length=len(nums)
value=3
if value in num:
    num.remove(value)
    if len(num) <= original_length:
        num.append('_')  
if value in num:
    num.remove(value)
    if len(num) <= original_length:
        num.append('_')       
print(num)

#program 5

nums=[1,2,3,1]
a,b,c,d=nums
if(a==b)or(a==c)or(a==d)or(b==c)or(b==d)or(c==d):
    print("True")
else:
    print("False")

#program 8
num1 = [1, 2, 2, 1]
num2 = [2, 2]
new_list = []
for i in num1:
    if i in num2 and i not in new_list:
        new_list.append(i)
print(new_list)

#program 6
num=int(input("Num:")) #38
b=str(num)   #'38'
digit=[int(b[0]),int(b[1])]   #[3,8]
add=digit[0]+digit[1]
if add >=10:  #11>=10
    b=str(add) #'11'
    digit=[int(b[0]),int(b[1])]
    add=digit[0]+digit[1]
print(add)

#program 7
arr=[1,0,2,3,0,4,5,0]
arr1=arr.copy() 
length=len(arr) 
i=0
if arr[1]==0:
    arr1.insert(2,0)
    if len(arr1)>length:
        arr1.pop()
if arr[4]==0:
    arr1.insert(5,0)
    if len(arr1)>length:
        arr1.pop()
print(arr1)





            
            
            
        

















