### Lab 2
print('''
1. Age category
2. Calculator
3. Mark finder
4. Pythagoras
''')
task = int(input("Please select a task number: "))

### 1. Age category
if task == 1:
    age = int(input("Please enter your age: "))
    if age >= 18:
        print("You are in Category A")
    elif age >= 16:
        print("You are in Category B")
    else:
        print("You are in Category C")

### 2. 2. Calculator
elif task == 2:
    num1 = int(input("Please enter your first number:"))
    num2 = int(input("Please enter your second number: "))

    print("Add          +\nSubtract     -\nMultiply     *\nDivide       /\n")
    operator = input("Please enter an operator: ")
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    else:
        print("Please select a valid option.")

### 3. Mark finder
elif task == 3:
    mark = int(input("What mark did you get? "))
    level = int(input("What level are you in? (1 or 2): "))

    if level == 1:
        if  70 < mark <= 100:
            print("Distinction")
        elif 60 < mark <=70:
            print("Merit")
        elif 49 < mark <=60:
            print("Pass")
        elif 0 <= mark <50:
            print("Fail")
        else:
            ("Please input a mark from 0 to 100")
    elif level == 2:
        if  65 < mark <= 100:
            print("Distinction")
        elif 50 < mark <=65:
            print("Merit")
        elif 39 < mark <=50:
            print("Pass")
        elif 0 <= mark <40:
            print("Fail")
        else:
            ("Please input a mark from 0 to 100")

### 4. Pythagoras
elif task == 4:
    print('''Pythagoras calculator
    1.	Find the length of A given B and C  
    2.	Find the length of B given A and C 
    3.	Find the length of C given A and B 
    ''')
    selection = int(input("Pick an option: "))

    if selection == 1:
        B = int(input("Please input size of side B: "))
        C = int(input("Please input size of side C: "))
        print("Side A = ",(C**2-B**2)**0.5)
    elif selection == 2:
        A = int(input("Please input size of side A: "))
        C = int(input("Please input size of side C: "))
        print("Side B = ",(C**2-A**2)**0.5)
    elif selection == 3:
        A = int(input("Please input size of side A: "))
        B = int(input("Please input size of side B: "))
        print("Side B = "(A**2+B**2)**0.5)
    else:
        print("Invalid selection")

###
else:
    ("Invalid task selection")
