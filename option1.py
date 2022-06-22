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
        # Employee number
        while True:
            emp_num = input("Enter employee number: ")
            if emp_num == "":
                print("Invalid input. Try again.")
            elif len(emp_num) != 5:
                print("Invalid input. Employee number must be 5 characters long. Try again.")
            else:
                break
        # Employee first name
        while True:
            emp_f_name = input("Enter employee first name: ").title()
            if emp_f_name == "":
                print("Invalid input. Try again.")
            else:
                break

        # Employee second name
        while True:
            emp_l_name = input("Enter employee last name: ").title()
            if emp_l_name == "":
                print("Invalid input. Try again.")
            else:
                break

        # Location of trip
        while True:
            loc_trip = input("Enter location of trip: ").title()
            if loc_trip == "":
                print("Invalid input. Try again.")
            else:
                break

        # Start date of trip
        while True:
            try:
                start_date = input("Enter Start date of trip (mm/dd/yyyy): ")
                start_date_obj = dt.datetime.strptime(start_date, "%m/%d/%Y")
            except:
                print("Invalid format. Format must be (mm/dd/yy). Try again.")
            else:
                break

        # End date of trip
        while True:
            try:
                end_date = input("Enter End date of trip (mm/dd/yyyy): ")
                end_date_obj = dt.datetime.strptime(end_date, "%m/%d/%Y")
            except:
                print("Invalid format. Format must be (mm/dd/yyyy). Try again.")
            else:
                if end_date_obj > start_date_obj + dt.timedelta(days=7):
                    print("Invalid input. End date of trip must be within 7 days of start date. Try again.")
                else:
                    break

        # Number of days of trip
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

        # Car type
        while True:
            car_type = input("Was the car used your own or rented (O/R): ").upper()
            if car_type == "":
                print("Invalid input. Try again.")
            elif car_type == "O":
                while True:
                    while True:
                        try:
                            total_km = int(input("Enter total amount of KM: "))
                        except:
                            print("Invalid input. Try again.")
                        else:
                            if total_km < 1 or total_km > 2000:
                                print("Invalid input. Total Km's cannot be less than 1 or greater than 2000. Try again.")
                            else:
                                break
                    break
                break
            elif car_type == "R":
                total_km = 0
                break
            else:
                print("Invalid input. Input must be 'O' or 'R'. Try again.")

        # Claim type
        while True:
            claim_type = input("Enter the Claim type (S/E): ").upper()
            if claim_type == "S":
                break
            elif claim_type == "E":
                break
            else:
                print("Invalid input. Input must be 'S' or 'E'. Try again.")

        # Calculations
        emp_name = emp_f_name + " " + emp_l_name
        per_diem = num_days * DAILY_RATE

        mil_amt = 0
        mil_pay = 0

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

        # Formatting
        hst_dsp = "${:.2f}".format(hst)
        claim_amt_dsp = "${:.2f}".format(claim_amt)
        mil_amt_dsp = "${:.2f}".format(mil_amt)
        mil_pay_dsp = "${:.2f}".format(mil_pay)
        claim_total_dsp = "${:.2f}".format(claim_total)

        # Output
        print()
        print("Nl Chocolate Company Claim Processed")
        print("------------------------------------")
        print(f"Employee number: {emp_num:>19s}")
        print(f"Employee name: {emp_name:>21s}")
        print(f"Trip location: {loc_trip:>21s}")
        print(f"Start Date: {start_date:>24s}")
        print(f"End Date: {end_date:>26s}")
        print(f"Number of days: {num_days:>20d}")
        print(f"Car used: {car_type:>26s}")
        print(f"Claim type: {claim_type:>24s}")
        print(f"claim amount: {claim_amt_dsp:>22s}")
        if mil_amt > 0:
            print(f"Mileage amount: {mil_amt_dsp:>20s}")
        if mil_pay > 0:
            print(f"Pay for rental car: {mil_pay_dsp:>16s}")
        print(f"Hst: {hst_dsp:>31s}")
        print("------------------------------------")
        print(f"Claim total: {claim_total_dsp:>23s}")
        print()

        # end program and return to main menu or input another claim
        while True:
            cont = input("Would you like to Process another claim? (Y/N): ").upper()
            if cont == "Y":
                break
            elif cont == "N":
                return
            else:
                print("Invalid input. Try again.")
