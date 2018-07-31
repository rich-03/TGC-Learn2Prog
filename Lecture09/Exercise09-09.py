def findincrease(val1, val2):
    if val2 > val1:
        return val2 - val1
    else:
        return 0


salary1 = float(input("Enter previous salary"))
benefits1 = float(input("Enter previous benefits"))
bonus1 = float(input("Enter previous bonus"))
salary2 = float(input("Enter new salary"))
benefits2 = float(input("Enter new benefits"))
bonus2 = float(input("Enter new bonus"))
salaryincrease = findincrease(salary1, salary2)
benefitsincrease = findincrease(benefits1, benefits2)
bonusincrease = findincrease(bonus1, bonus2)
