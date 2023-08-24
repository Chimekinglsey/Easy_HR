# #!/usr/bin/python3
# from user_models.user_company import Company
# from user_models.user_hr import HrUser
# from sqlalchemy.exc import IntegrityError
# from datetime import datetime
# import time

# print("Hello, Welcome to Easy_Hr")
# time.sleep(10)
# print("We will set up your account now")
# time.sleep(10)

# company_name = input("Enter company's name: ")
# company_headquarters = input("Enter company's headquaters location: ")
# company_strenght = int(input("Enter company's staff_strength: "))
# MyCompany = Company(company_name, company_headquarters, company_strenght)
# try:
#     MyCompany.save()
#     Company_id = MyCompany.id
#     print('Your Company account, {} has been successfully created'.format(MyCompany.name))
# except IntegrityError as e:
#    print("Oops, {} already exists").format(MyCompany.name)

# time.sleep(10)
# print("Let's create your user")
# time.sleep(10)

# hr_first_name = input("What is your first name?: ")
# hr_last_name = input("What is your last name?: ")
# hr_password = input("Provide a password: ")
# hr_email = input("What is your email address?: ")
# hr_phoneNo = input("Enter your phone number? ")

# MyUser = HrUser(Company_id, hr_first_name, hr_last_name, hr_password, hr_email, hr_phoneNo)
# try:
#     MyUser.save()
#     User_id = MyUser.id
#     print('{}, you have successfully created your account'.format(MyUser.first_name))
# except IntegrityError as e:
#    print("Oops User {} already exists").format(MyUser.first_name)

# print("Now lets create your company database")
# MyUser.create_company_database()

# print("Create a branch")
# branch_name = input("Enter branch name: ")
# branch_location = input("Enter branch location: ")
# try:
#     branch_id = MyUser.create_branch(branch_name, branch_location)
#     print('{} sucessfully created'.format(branch_name))
#     time.sleep()
# except IntegrityError as e:
#     print('{} already exists'.format(branch_name))


# print("Create a department")
# dept_name = input("Enter department name: ")
# try:
#     dept_id = MyUser.create_dept(branch_id, dept_name)
#     print('{} sucessfully created'.format(dept_name))
#     time.sleep(10)
# except IntegrityError as e:
#     print('{} already exists'.format(dept_name))

# print("Create a level")
# level_name = input("Enter level name: ")
# level_type = input("Enter a level type, Senior or Junior: ")
# try:
#     level_id = MyUser.create_level(level_name, level_type)
#     print('{} sucessfully created'.format(level_name))
# except IntegrityError as e:
#     print('{} already exists'.format(level_type))


# def get_date_of_birth():
#     while True:
#         dob_str = input("Enter employee date of birth (YYYY-MM-DD): ")
#         try:
#             dob = datetime.strptime(dob_str, "%Y-%m-%d")
#             return dob
#         except ValueError:
#             print("Invalid date format. Please use the format YYYY-MM-DD.")

# print("Store an employee details")
# emp_first_name = input("Enter Employee First name: ")
# emp_last_name = input("Enter Employee Last name: ")
# date_of_birth = get_date_of_birth()
# emp_email = input("Enter employee's email: ")
# salary = input("Enter employee's salary: ")
# emp_address = input("Enter employee's address: ")
# emp_phoneNo = input("Enter phone_number: ")
# try:
#     employee_id = MyUser.create_employees(branch_id, dept_id, level_id, emp_first_name, emp_last_name,
#                  date_of_birth, emp_email, salary, emp_address, emp_phoneNo)
#     print('{:s} {:s} sucessfully created'.format(emp_first_name, emp_last_name))
#     time.sleep(10)
# except IntegrityError as e:
#     print('{:s} with {:s} already exists'.format(emp_first_name, emp_email))


# print("Store an employee details")
# emp_first_name = input("Enter Employee First name: ")
# emp_last_name = input("Enter Employee Last name: ")
# date_of_birth = get_date_of_birth()
# emp_email = input("Enter employee's email: ")
# salary = int(input("Enter employee's salary: "))
# emp_address = input("Enter employee's address: ")
# emp_phoneNo = input("Enter phone_number: ")
# try:
#     employee_id = MyUser.create_employees(branch_id, dept_id, level_id, emp_first_name, emp_last_name,
#                  date_of_birth, emp_email, salary, emp_address, emp_phoneNo)
#     print('{:s} {:s} details sucessfully stored'.format(emp_first_name, emp_last_name))
#     time.sleep(10)
# except IntegrityError as e:
#     print('{:s} with {:s} already exists'.format(emp_first_name, emp_email))


# print('Store an {:s} {:s} Next of Kin details'.format(emp_first_name, emp_last_name))
# nok_first_name = input("Enter Next of Kin First name: ")
# nok_last_name = input("Enter Next of Kin Last name: ")
# nok_email = input("Enter Next of Kin's email: ")
# nok_address = input("Enter Next of Kin's address: ")
# nok_phoneNo = input("Enter Next of Kin's phone_number: ")
# try:
#     employee_id = MyUser.create_nok(employee_id, nok_first_name, nok_last_name, nok_email, nok_address, nok_phoneNo)
#     print('{:s} {:s} details sucessfully stored'.format(nok_first_name, nok_last_name))
#     time.sleep(10)
# except IntegrityError as e:
#     print('{:s} with {:s} already exists'.format(nok_first_name, nok_email))

#!/usr/bin/python3
from models.branch import Branch
from models.dept import Department
from models.levels import Level

newBranch= Branch("Alaba", "Surulere")
branch_id = newBranch
print(newBranch.id)

newDept = Department(newBranch.id, "Customer Service")
newDept.save
print(newDept.id)

newLevel = Level(newDept.id, "Manager", "Senior")
newLevel.save
print(newLevel.id)