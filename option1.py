# option 1

import datetime as dt

# Constants
DAILY_RATE = 85.00
MILE_RATE_OWN = 0.17
MILE_RATE_RENT = 65.00
HST_RATE = 0.15

def get_travel_claim():
        # Input
    while True:
        while True:
            emp_num = input("Enter employee number: ")
            if emp_num == "":
                print("Invalid input. Try again.")
            elif len(emp_num) != 5:
                print("Invalid input. Employee number must be 5 characters long. Try again.")
            else:
                break

        while True:
            emp_f_name = input("Enter employee first name: ").title()
            if emp_f_name == "":
                print("Invalid input. Try again.")
            else:
                break

        while True:
            emp_l_name = input("Enter employee last name: ").title()
            if emp_l_name == "":
                print("Invalid input. Try again.")
            else:
                break

        while True:
            loc_trip = input("Enter location of trip: ").title()
            if loc_trip == "":
                print("Invalid input. Try again.")
            else:
                break

        while True:
            try:
                start_date = input("Enter Start date of trip (mm/dd/yyyy): ")
                start_date_obj = dt.datetime.strptime(start_date, "%m/%d/%Y")
            except:
                print("Invalid format. Format must be (mm/dd/yy). Try again.")
            else:
                break


        while True: # Doesn't break out of loop
            try:
                end_date = input("Enter End date of trip (mm/dd/yyyy): ")
                end_date_obj = dt.datetime.strptime(end_date, "%m/%d/%Y")
                if end_date_obj > start_date_obj + dt.timedelta(days=7):
                    print("Invalid input. End date of trip must be within 7 days of start date. Try again.")
            except:
                    print("Invalid format. Format must be (mm/dd/yyyy). Try again.")
            else:
                break

        while True:
            try:
                num_days = int(input("Enter Number of days: "))
            except:
                    print("Invalid input. Try again.")
            else:
                if num_days < 1 or num_days > 7:
                    print("Invalid input. Try again.")
                else:
                    break

        while True:
            car_type = input("Was the car used your own or rented (O/R): ").upper()
            if car_type == "":
                print("Invalid input. Try again.")
            elif car_type == "O":
                while True: # Doesn't break out of loop
                    try:
                        total_km = int(input("Enter total amount of KM: ")) # only used when employee used their own car cannot exceed 2000
                    except:
                        if total_km < 1 or total_km > 2000:
                            print("Invalid input. Total Km's cannot be less than 1 or greater than 2000. Try again.")
                    else:
                        break
            elif car_type == "R":
                total_km = 0
                break
            else:
                print("Invalid input. Input must be 'O' or 'R'. Try again.")

        while True:
            claim_type = input("Enter the Claim type (S/E): ").upper()
            if claim_type == "S":
                break
            elif claim_type == "E":
                break
            else:
                print("Invalid input. Input must be 'S' or 'E'. Try again.")



        emp_name = emp_f_name + " " + emp_l_name
        per_diem = num_days * DAILY_RATE

        if car_type == "O":
            mil_amt = total_km * MILE_RATE_OWN
        elif car_type == "R":
            mil_pay = num_days * MILE_RATE_RENT

        bonus = 0

        if num_days > 3:
            bonus += 100

        if total_km > 1000 and car_type == "O":
            mil_amt = (MILE_RATE_OWN + .04) * total_km

        if total_km == 0 and car_type == "R":
            mil_amt = 0

        if claim_type == "E":
            per_diem = num_days * (DAILY_RATE + 45.00)

        claim_amt = per_diem + mil_amt + mil_pay + bonus

        hst = per_diem * HST_RATE

        claim_total = claim_amt + hst

        # Output
        print()
        print("Nl Chocolate Company Claim Processed")
        print("------------------------------------")
        print(f"Employee number {emp_num}")
        print(f"Employee name {emp_name}")
        print(f"Trip location {loc_trip}")
        print(f"Start Date {start_date}")
        print(f"End Date {end_date}")
        print(f"Number of days {num_days}")
        print(f"Car used {car_type}")
        print(f"Claim type {claim_type}")
        print(f"claim amount {claim_amt}")
        if mil_amt > 0:
            print(f"Mileage amount: {mil_amt}")
        if mil_pay > 0:
            print(f"Pay for rental car {mil_pay}")
        print(f"Hst {hst}")
        print("------------------------------------")
        print(f"Claim total {claim_total}")
        print()

        while True:
            cont = input("Would you like to Process another claim? (Y/N): ").upper()
            if cont == "Y":
                break
            elif cont == "N":
                exit()
            else:
                print("Invalid input. Try again.")
