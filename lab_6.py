#Lab 6

def getIncomeTax(salary):
    if salary > 150000:
        tax = (salary-150000)*0.45
        tax += 115500*0.4
        tax += 34500*0.2
    elif salary > 34500:
        tax = (salary-34500)*0.4
        tax += 34500*0.2
    elif salary > 0:
        tax= salary*0.2
    else:
        return "error"
    return tax

salaryinput = int(input("Please enter your salary: "))

print("Your tax is: ",getIncomeTax(salaryinput))
