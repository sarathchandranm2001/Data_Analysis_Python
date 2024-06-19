def calculate_electricity_bill(units):
    if units <= 0:
        return "Invalid input. Units cannot be zero or negative."

    total_bill = 0

    if units <= 200:
        total_bill = units * 0.50
    elif units <= 400:
        total_bill = 200 * 0.50 + (units - 200) * 0.65
    elif units <= 600:
        total_bill = 200 * 0.50 + 200 * 0.65 + (units - 400) * 0.80
    else:
        total_bill = 200 * 0.50 + 200 * 0.65 + 200 * 0.80 + (units - 600) * 1.00

    
    if total_bill > 400:
        surcharge = total_bill * 0.15
        total_bill += surcharge


    if total_bill < 100:
        total_bill = 100

    return total_bill


units_consumed = int(input("Enter the units consumed: "))
bill_amount = calculate_electricity_bill(units_consumed)
print(f"Electricity bill amount: Rs. {bill_amount:.2f}")
