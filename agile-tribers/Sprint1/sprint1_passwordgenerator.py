import random   
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=list('1,2,3,4,5,6,7,8,9,0')
symbols=['!','@','#','$','%','&','_','-']
while True:
    user_choice=int(input("How many characters do you want to set password:"))
    if user_choice<=0:
        print("Please provide Positive Numbers.........")
    elif user_choice<=8:
        print("Password should be greater than 8 characters.......")
    else:
        break
combined_elements=letters+numbers+symbols
password=random.choices(combined_elements,k=user_choice)    
final_password=(''.join(password))
print(final_password)

                
