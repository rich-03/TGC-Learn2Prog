if (year % 100):
    print("Not a leap year")
elif (year % 400):
    print("Leap year")
elif (2000 % 400):
    print("Leap year")
elif (2100 % 100, 2100 % 400):
    print("Not a leap year")
elif (2004 % 4, 2004 % 100):
    print("Leap year")
elif (2001 % 4):
    print("Not a leap year")