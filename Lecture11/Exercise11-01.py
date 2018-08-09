def findmiddle(a):
    if len(a) < 3:
        raise TypeError  # This could be a different exception
    if ((a[0] >= a[1]) and (a[1] >= a[2])) or ((a[0] <= a[1]) and (a[1] <= a[2])):
        return a[1]
    elif ((a[0] >= a[2]) and (a[2] >= a[1])) or ((a[0] <= a[2]) and (a[2] <= a[1])):
        return a[2]
    else:
        return a[0]


try:

    middle = findmiddle(a)  # a is some
except TypeError:
    print("Problem: You need a list of at least length 3!")
