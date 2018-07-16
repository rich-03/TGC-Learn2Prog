age = 67
income = 10000
if age > 70 & income < 15000:
    print("False")
if age > 70:
    if income < 15000:
        print("Eligible for benefits")
    elif income < 20000:
        print("Eligible for reduced benefits")
    else:
        print("Not eligible for benefits")
elif income < 20000:
    print("Eligible for reduced benefits")
else:
    print("Not eligible for benefits")
