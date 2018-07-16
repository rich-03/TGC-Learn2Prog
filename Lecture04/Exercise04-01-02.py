# Ask the user for an amount already saved
print("We are able to determine how long it will take to make up all of your savings.")
balance = float(input("Enter the amount that will be saved: "))  # type: str
if balance < 0:   # type: str
    print("You have a stable balance.")
    balance = 0
    payment = 1
else:
    payment = float(input("Enter the amount that you will save each period: "))  # type: float
    if payment == 0:
        payment = float(input("Invalid Input. Enter a non-zero value:"))
        if payment == 0:
            print("Invalid Input, we will put in 1 payment automatically for this period.")
            payment = 1
# Calculate depository amount
num_remaining_payments = int(balance / payment)  # type: float
# Present info to user
print("You need to make", num_remaining_payments, "more deposits.")
