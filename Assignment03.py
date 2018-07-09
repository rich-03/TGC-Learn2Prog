a = 1
b = 2
c = 2
d = "One"
e = "Two"
f = "Three"
g = "one"

a > b #False
a == b #False
a != b #True
b == c #True
d < e #True
e < f #True
d < g #False
g < e #True
not (a == b) #True
b < c or b > c #False
(a+1) == b and not b < c #True
((a <= b) and (b <= c)) or ((a >= b) and (b >= c)) #False
total_cost = 100.00
days = 3
cost_per_day = total_cost / days
if cost_per_day > 40:
    print("Too expensive")
elif cost_per_day > 30:
    print("Reasonable cost")
elif cost_per_day > 20:
    print("Excellent cost")
else:
    print("Incredible bargain")

age = 67
income = 10000
if (age > 70):
    if (income < 15000):
        print("Eligible for benefits")
    else:
        if (income < 20000):
            print("Eligible for reduced benefits")
        else:
            print("Not eligible for benefits")
else:
    if (income < 20000):
        print("Eligible for reduced benefits")
    else:
        print("Not eligible for benefits")

age = 67
income = 10000
if (age > 70):
    if (income < 15000):
        print("Eligible for benefits")
    elif (income < 20000):
        print("Eligible for reduced benefits")
    else:
        print("Not eligible for benefits")
elif (income < 20000):
    print("Eligible for reduced benefits")
else:
    print("Not eligible for benefits")

if user_guess < 100:
    print("Too low")
elif (user_guess > 100):
    print("Too high")
else:
    print("Exactly right")

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