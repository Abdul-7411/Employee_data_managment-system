##EMOPLYEE DATA MANAGMENT SYSTEM
print("\nEMPLOYEE DATA MANAGMENT")

def Add_employee():#function for adding the employee's
    with open("employee.txt",'a') as f:
        employee_id = input("Employee Id :").strip()
        name = input("Employee name :").strip()
        email = input("Employee Email :").strip()
        profession = input("Employee profession :").strip()
        emp_level = input("Employee level :").strip()
        data = f"Employee Id :{employee_id} | Name :{name} | Email :{email} | Profession :{profession} | Level :{emp_level}\n"
        f.writelines(f"{data.strip()}\n")
        
def Search_employee():#function for searching emoployee
    with open("employee.txt",'r') as f1:
        emp_details = f1.readlines()
    user = input("Employee Id :").strip()
    found = False
    for detail in emp_details:
        if user in detail:
            print(f"Data found :{detail.strip()}\n")
            found = True
    if not found:
        print("No data found\n")

def Remove_employee():#function for removing employee
    with open("employee.txt",'r') as f2:
        emps = f2.readlines()
    user = input("Employee Id :").strip()
    found = False
    new_emp = []
    for emp in emps:
        if user in emp:
            print(f"{emp.strip()}")
            found = True
        else:
            new_emp.append(emp)
    with open("employee.txt",'w') as f3:
        updated = f3.writelines(new_emp)
    
    if found:
        print("Employee remove successfully\n")
    else:
        print('No data found\n')
        
def Show_all():#function for seeing all the data in file
    with open("employee.txt",'r') as f4:
        show_all = f4.read()
        if show_all:
            print("\nEmployee Data")
            print(f"{show_all}")
        else:
            print("No data found!\n")
            
def Remove_all():#function for removing all the data from the file
    updated_data = []
    with open("employee.txt",'w') as f5:
        data = f5.writelines(updated_data)
             
while True:#from here is all the code exicute
    print("1.Add Employee\n2.Search Employee\n3.Remove employee\n4.Show all\n5.Remove all\n6.Exit")
    user_input = input("Choose options :").strip()
    
    if user_input == '1':
        Add_employee()
    elif user_input == '2':
        Search_employee()
    elif user_input == '3':
        Remove_employee()
    elif user_input == '4':
        Show_all()
    elif user_input == '5':
        Remove_all()
    elif user_input == '6':
        break