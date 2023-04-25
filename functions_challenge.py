### Function challenges
import math

###1
def passwordchecker(password):
    comppasswords = ["password","password123","123456","qwerty"]
    if password in comppasswords:
        print(f"Use a safer password '{password}' is compromised.")
    else:
        print("Password is safe.")

###2
def simplecalc(num1, num2):
    sum = num1+num2
    sub = num1-num2
    multiple = num1*num2
    print(f"Sum = {sum}, Sub = {sub}, Multiple = {multiple}")

###3
def highest(*numbers):
    return max(numbers)

###4
def evenorodd(number):
    if number%2 == 1:
        print("Odd!")
    elif number%2 == 0:
        print("Even!")
    else:
        print("Error")

###5
def uppercaser(stringput):
    return stringput.upper()

###6
def circlearea(radius):
    return round(math.pi*(radius**2),2)

###7
def celtofar(temp):
    return round((temp*1.8)+32,2)

print('''
1. Password checker
2. Simple calc
3. Highest number
4. Even or odd
5. Uppercaser
6. Circle area
7. Celcius to Fahrenheit
''')
task = int(input("Please select a task number: "))

if task == 1:
    userpass = input("Enter your password: ")
    passwordchecker(userpass)

elif task == 2:
    input1 = int(input("First num = "))
    input2 = int(input("Second num = "))
    simplecalc(input1, input2)

elif task ==3:
    input1 = int(input("First num = "))
    input2 = int(input("Second num = "))
    input3 = int(input("Third num = "))
    print("The highest number is",highest(input1,input2,input3))

elif task ==4:
    oddinput = int(input("Please enter a number: "))
    evenorodd(oddinput)

elif task == 5:
    stringupper = input("Enter a string: ")
    print(uppercaser(stringupper))

elif task == 6:
    radiusinput = float(input("Please enter a radius: "))
    print("Area =", circlearea(radiusinput))

elif task == 7:
    tempinput = float(input("Please enter a temp in Celcius: "))
    print("This is equivalent to",celtofar(tempinput),"Fahrenheit")

else:
    print("Invalid task selection")
