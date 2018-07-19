def sumList(mylist):
    for i in range(1, len(mylist)):
        mylist[i] += mylist[i - 1]
    return mylist[len(mylist) - 1]


testlist1 = [1, 2, 3, 4, 5]
testlist2 = [6, 7, 8, 9, 10]
print(sumList(testlist1))
print(sumList(testlist2))
print(testlist1)
