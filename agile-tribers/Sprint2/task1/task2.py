#program 1
person={
    'name':"Alice",
    'age':25,
    'city':"New York"
    }
person['email']="alice@example.com"
person['age']=26
person.pop('city')
print(person)

#program 2
fruits={
    'apple':10,
    'banana':5,
    'cherry':15
    }
print("Quality of banana:",fruits['banana'])
fruits['orange']=8
fruits['apple']=15
fruits.pop('cherry')
print(fruits)

#program 3
sentence=input("Enter the sentence:")
word=sentence.split()
new={}
for i in word:
    if i in new:
        new[i]+=1
    else:
        new[i] = 1
print(new)

#program 4
dict1={'apple':5,'banana':3,'orange':7}
dict2={'banana':2,'orange':3,'grape':4}
dict3=dict1|dict2
for key,value in dict1.items():
    if key in dict2:
        added_value=dict1[key]+dict2[key]
        dict3[key]=added_value
print(dict3)

#program 5
employees = { 
'E001': {'name': 'Alice', 'department': 'HR', 'salary': 50000}, 
'E002': {'name': 'Bob', 'department': 'IT', 'salary': 60000}, 
'E003': {'name': 'Charlie', 'department': 'Finance', 'salary': 55000} 
}    
def get_salary(employee_dict,emp_id):
    return employee_dict[emp_id]['salary']
res=get_salary(employees,'E002')
print("salary of Employee 2:",res)

def increase_salary(employee_dict,percentage):
    for emp_id in employee_dict:
        current_salary=employee_dict[emp_id]['salary']
        new_salary=current_salary*(percentage/100)
        employee_dict[emp_id]['salary']=current_salary+new_salary
increase_salary(employees,10)
print(employees)

#program 6
marks = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 90
    }
sort_elements=dict(sorted(marks.items(),key=lambda x:x[1],reverse=True))
print(sort_elements)

#program 7
for i in range(1,11):
    for j in range(1,11):
        value=i*j
        print(value,end=' ')
    print()

#program 8
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
transpose_matrix=[]
rows=len(matrix)
columns=len(matrix[0])
for i in range(rows):
    new_row=[]
    for j in range(columns):
        new_row.append(matrix[j][i])
    transpose_matrix.append(new_row)
for row in transpose_matrix:
    print(row)

#program 9
matrix=[
    [2,4,5],
    [7,9,11],
    [13,16,19]
    ]
count=0
for row in matrix:
    for column in row:
        divise_count=0
        for i in range(1,column+1):
            if column%i==0:
                divise_count+=1
        if divise_count==2:
            count+=1
print("Total prime numbers:",count)

#program 10
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
spiral = []
while matrix:
    spiral=spiral+matrix.pop(0)
    for row in matrix:
        if row:
            spiral.append(row.pop())
        if matrix:
            spiral=spiral+matrix.pop()[::-1]
print("Spiral order:", spiral)

        
        

#program 11
weight=int(input("Enter weight(kg):"))
height=float(input("Enter height(m):"))
bmi=weight/(height**2)
print("BMI:",bmi)
if bmi<18.5:
    print("Category: Under weight")
elif bmi>=18.5 and bmi<=24.9:
    print("Category: Normal weight")
elif bmi>=25 and bmi<=29.9:
    print("Category: Over weight")
else:
    print("Category: Obesity")

#program 12
user=int(input("Enter student score(0-100):"))
if user>=90 and user<=100:
    print("Grade: A")
    print("Status: Pass")
elif user>=80 and user<=89:
    print("Grade: B")
    print("Status: Pass")
elif user>=70 and user<=79:
    print("Grade: c")
    print("Status: Pass")
elif user>=60 and user<=69:
    print("Grade: D")
    print("Status: Fail")
else:
    print("Grade: F")
    print("Status: Fail")

#program 13
matrix=[
    ["madam","apple","racecar"],
    ["level","hello","civic"],
    ["world","deified","rotor"]
    ]
for row in matrix:
    for column in row:
        reverse_word=column[::-1]
        if column==reverse_word:
            print(f"{column} is a palindrome")
        else:
            print(f"{column} is not palindrome")
#program 14
for i in range(1,11):
    if i%2==0:
        for j in range(1,11):
            value=i*j
            print(value,end=' ')
        print()





















