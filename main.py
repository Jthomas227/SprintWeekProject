# NL Chocolate company Program
# Authors: Jacob Thomas & Devin Augot
# Date completed: 06/24/2022

import option1
import option4
import option23

while True:
    while True:
        # Main Menu
        print()
        print("Nl Chocolate Company")
        print("Travel Claims Processing System")
        print()
        print("1. Enter an Employee Travel Claim.")
        print("2. Fun Interview Question.")
        print("3. Cool Stuff with Strings and Dates.")
        print("4. Graph Monthly Claim Totals.")
        print("5. Quit Program.")
        print()

        # User input for choice
        while True:
            try:
                choice = int(input("Enter choice (1-5): "))
            except:
                print("Invalid input. Try again.")
            else:
                if choice < 1 or choice > 5:
                    print("Invalid input. Try again")
                elif choice == 1:
                    option1.get_travel_claim()
                    break
                elif choice == 2:
                    option23.fizzbuzz()
                    break
                elif choice == 3:
                    option23.cool_string_dates()
                    break
                elif choice == 4:
                    option4.get_month_rev_chart()
                    break
                else:
                    exit()



