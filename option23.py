# preparing program option for Sprint week project 2022-06-21
# Author : Devin Augot & Jacob Thomas

import datetime
from datetime import date

def fizzbuzz():
    while True:
        for Numbers in range(1, 101):
            if Numbers % 5 == 0 and Numbers % 8 == 0:
                print("FizzBuzz")
            if Numbers % 5 == 0:
                print("Fizz")
            elif Numbers % 8 == 0:
                print("Buzz")

            else:
                print(Numbers)

        else:
            break

    print()
    Anykey = input("Press any key to continue.")
    print()


# option 3 - Cool stuff with strings and dates


def FindLen(EmpName):

    # Function to count the number of letters in the Employees name
    counter = 0
    while EmpName[counter:]:
        counter += 1
    return counter


def Age(birthdate):

    # Function to Calculate employees age
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def cool_string_dates():
    while True:
        CurDate = datetime.datetime.now()
        CurYear = 2022
        EmployeeID = []


        while True:
            EmpName = input("Enter the employees name: ")
            if EmpName == "":
                print("Error. Employees name cannot be empty. Please Re-Enter.")
            else:
                break
        EmployeeID.append(EmpName[0])

        while True:
            LastName = input("Enter the employees last name: ")
            if LastName == "":
                print("Error Employees last name cannot be empty. Please Re-Enter.")
            else:
                break
        EmployeeID.append(LastName[0])

        while True:
            PhoneNum = input("Enter the employees Phone number (9999999999): ")

            if len(PhoneNum) != 10:
                print("Error. Phone number must be 10 digits in length. Please Re-Enter. ")
            else:
                break
        EmployeeID.append(PhoneNum[8:10])

        while True:
            EmpStart = input("Enter the employees start date as (YYYY-MM-DD): ")
            if EmpStart[4] != "-":
                print("Error. Employee Start Year and Month must be separated with a - .")
            elif EmpStart[7] != "-":
                print("Error. Employee Start Month and Day must be separated with a - .")
            elif EmpStart[0:3].isalpha() is True:
                print("Error. Employee Start Year must be 4 digits. Please Re-Enter. ")
            elif EmpStart[5:6].isalpha() is True:
                print("Error. Employee Start date day must be 2 digits. Please Re-Enter. ")
            elif EmpStart[8:9].isalpha() is True:
                print("Error. Employee Start date year must be 2 digits. Please Re-Enter. ")
            else:
                break
        EmployeeID.append(EmpStart[2:4])

        while True:
            EmpBirth = input("Enter the employees Birth date as (YYYY-MM-DD): ")

            if EmpBirth[4] != "-":
                print("Error. Employee Birth Year and Month must be separated with a - .")
            elif EmpBirth[7] != "-":
                print("Error. Employee Start Day and Year must be separated with a - .")
            elif int(EmpBirth[6:7]) < 1 or int(EmpBirth[6:7]) > 12:
                print("Error. Month must be entered between 01 and 12. Please Re-Enter")
            else:
                break
        EmployeeID.append(EmpBirth[2:4])

        # Print Statements

        print()
        print(f"Employees name is {FindLen(EmpName)} letters in length!. ")
        print(f"Employees last name is {FindLen(LastName)} letters in length!. ")
        EmployeeBirthYearDsp = datetime.datetime.strptime(EmpBirth, "%Y-%m-%d")
        print(f"Employees age is: {Age(EmployeeBirthYearDsp)}")
        print(f"The Employees Company ID is: {EmployeeID[0]}{EmployeeID[1]}-{EmployeeID[2]}{EmployeeID[3]}{EmployeeID[4]}")
        print()

    # Employee company ID is Based on First Letter of first and last name,
    # last 2 digits of phone number and last 2 digits birth date.

        ReturnToMain = input("Would you like to exit to main menu Y/N?") # Needs work
        if ReturnToMain.upper() == "N":
            continue
        elif ReturnToMain.upper() == "Y":
            print()
            return ReturnToMain
        else:
            print("Invalid input. Try again.")

