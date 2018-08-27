def dosomething(lst):
    if len(lst) == 0:
        return 1
    else:
        return lst[0]*dosomething(lst[1:])
