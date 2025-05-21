import locale
import ast
courses_available=("Python","Data Science","Web Development","Ai")
fees_details={"Python":25000,"Data Science":20000,"Web Development":40000,"Ai":45000}

#add student        

def add_student():
    student={}
    existing_id=set()
    try:
        with open("student_detail.txt","r")as f:
            lines=f.readlines()
            for line in lines:
                student_id, student_details = line.strip().split(":", 1)
                existing_id.add(student_id)
    except Exception as e:
        print("Error:",e)
                
    while True:
        s_id=input("Enter student ID:")
        try:
            if not s_id.isdigit():
                raise ValueError("Invalid input,Enter valid input.....")
            if s_id in existing_id:
                raise ValueError("Student Id Already Exists")
            break
        except ValueError as e:
            print("Error:",e)

    while True:
        s_name=input("Enter student name:")
        try:
            if not s_name.isalpha():
                raise ValueError("Invalid Input,Enter valid input.....")
            break
        except ValueError as e:
            print("Error:",e)

    while True:
        age=input("Enter student age:")
        try:
            if not age.isdigit():
                raise ValueError("Invalid Input,Enter valid input.....")
            break
        except ValueError as e:
            print("Error:",e)
    print("Courses we offer:")
    for i,items in enumerate(courses_available,1):
        print(f"{i}. {items}")

    while True:
        course=input("Enter course:").title()
        try:
            if course not in courses_available:
                raise ValueError("Choose the course we offered.....")
            break
        except ValueError as e:
            print("Error:",e)
    print("Fees Details:")
    for i,(key,value) in enumerate(fees_details.items(),1):
        print(f"{i}. {key}: {value}")

    while True:
        total_fees=input("Enter Fees: ₹")
        try:
            if not total_fees.isdigit():
                raise ValueError("Invalid Input,Enter valid input.....")
            total_fees=int(total_fees)
            if total_fees != fees_details[course]:
                raise ValueError("You Entered Wrong Fees Details.....")
            break
        except ValueError as e:
            print("Error:",e)

    while True:
        fees_paid=input("Paid fees amount: ₹")
        try:
            if fees_paid.isalpha():
                raise ValueError("Enter Fees Details in Number Format.....")
            fees_paid=int(fees_paid)
            if fees_paid<0:
                raise ValueError("Invalid Input,Enter Valid Input.....")
            if fees_paid >=total_fees:
                raise ValueError("You Entered Paid Fees Amount is Higher Than Fees Amount.....")
            break
        except ValueError as e:
            print("Error:",e)
    check_balance=total_fees-fees_paid
    locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
    amount = check_balance
    formatted_amount = locale.currency(amount, grouping=True, symbol=True)
    print("Balance amount is: ",formatted_amount)
    student[s_id]={
        "Name":s_name,
        "Age":age,
        "Course":course,
        "Total Fees":total_fees,
        "Paid Fees":fees_paid,
        "Balance":check_balance
    }
    with open("student_detail.txt","a") as f:
        for key, value in student.items():
            f.write(f"{key}: {value}\n")
    

#update student

def update_student():
    search_id=input("Enter id:").strip()
    updated_lines=[]
    updated=False
    try:
        with open("student_detail.txt", "r") as f:
            lines = f.readlines()

        for line in lines:
            if ':' not in line:
                continue
            student_id, student_data = line.strip().split(':', 1)
            student_id = student_id.strip()

            if student_id == search_id:
                student_dict = ast.literal_eval(student_data.strip())

                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Course")
                print("4. Update Total Fees")
                print("5. Update Paid Fees")

                update = int(input("Enter Choice U Want to Update: "))
                if update == 1:
                    student_dict["Name"] = input("Enter New Name: ")
                elif update == 2:
                    student_dict["Age"] = input("Enter New Age: ")
                elif update == 3:
                    student_dict["Course"] = input("Enter New Course: ")
                elif update == 4:
                    student_dict["Total Fees"] = int(input("Enter New Total Fees: "))
                    student_dict["Balance"] = student_dict["Total Fees"] - student_dict["Paid Fees"]
                elif update == 5:
                    student_dict["Paid Fees"] = int(input("Enter New Paid Fees: "))
                    student_dict["Balance"] = student_dict["Total Fees"] - student_dict["Paid Fees"]
                    
                    print(f" Balance Amount is: ₹" ,student_dict["Balance"])
                else:
                    print("Invalid choice.")

                updated_line = f"{student_id}: {student_dict}\n"
                updated_lines.append(updated_line)
                updated = True
            else:
                updated_lines.append(line)

        with open("student_detail.txt", "w") as f:
            f.writelines(updated_lines)

        if updated:
            print("Student record updated successfully.")
        else:
            print("Student Id not found.")

    except Exception as e:
        print("Error Occurred:", e)

# remove students

def remove_student():
    search_id = input("Enter ID you want to remove:").strip()
    updated_lines = []
    removed = False  
    try:
        with open("student_detail.txt", "r") as f:
            lines = f.readlines()

        for line in lines:
            student_id, student_details = line.strip().split(":", 1)

            if student_id == search_id:
                removed = True  
                continue
            else:
                updated_lines.append(line)

        with open("student_detail.txt", "w") as f:
            f.writelines(updated_lines)

        if removed:
            print("Student ID removed successfully.")
        else:
            print("Student ID not found.")

    except Exception as e:
        print("Error:", e)

# view Student
def view_student():
    try:
        found=False
        view_id=input("Enter Id You want to view:")
        with open("student_detail.txt","r") as f:
            lines=f.readlines()
            for line in lines:
                student_id, student_details = line.strip().split(":", 1)
                student_id = student_id.strip()
        
                if view_id==student_id:
                    found=True       
                    print(f"{student_id}: {student_details}")
            if found:
                print("Student Id is Found")
            else:
                raise FileNotFoundError("Student Id Not Found")
    except Exception as e:
        print("Error:",e)

#Fees Report
            
def fees_report():
    found=False
    try:
        with open("student_detail.txt","r") as f:
            lines=f.readlines()
        for line in lines:
            student_id, student_details = line.strip().split(":", 1)
            details = ast.literal_eval(student_details.strip())
            balance = int(details["Balance"])

            if balance>0:
                print(f"id: {student_id} | Name: {details['Name']} | Balance Due: ₹{balance}")
                found=True
        if not found:
            print("All Students have Cleared their Fees")
                    
    except Exception as e:
        print("Error:",e)
            
            

while True:    
    print("1. Add Student")
    print("2. Update Student")
    print("3. Remove Student")
    print("4. View Student")
    print("5. Fees Report")
    print("6. Exit")

    choice=int(input("Enter Choice:"))
    if choice==1:
        add_student()
    elif choice==2:
        update_student()
    elif choice==3:
        remove_student()
    elif choice==4:
        view_student()
    elif choice==5:
        fees_report()
    elif choice==6:
        break
    else:
        print("Invalid Choice")
    
































    

    
