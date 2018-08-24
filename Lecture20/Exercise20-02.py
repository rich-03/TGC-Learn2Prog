def swap():
    pass


def one_bubble_pass(lst):
    returnval = False
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            swap()
            returnval = True
    return returnval
