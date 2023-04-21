print('''
1. Squares
2. Factorial
3. Investment calc
4. Number guess
5. Vowel counter
6. Mark average
''')
task = int(input("Please select a task number: "))

if task == 1:
    square = 0
    num = 0
    while square<2000:
        print(square)
        num=num+1
        square = num**2

elif task == 2:
    factorialnum = int(input("Please enter anumber to claculate the factorial of: "))
    factorial = factorialnum
    while factorialnum>1:
        factorialnum = factorialnum-1
        factorial = factorial*factorialnum
    print(factorial)

elif task == 3:
    investment = int(input("Please input value of initial investment: "))
    interestrate = int(input("Please intput the yearly interest rate: "))
    targetvalue = int(input("Please input the investment target: "))
    time = 0
    while investment < targetvalue:
        time=time+1
        investment = investment*(1+(interestrate/100))
        #print(investment)
    print("It will take "+str(time)+" to reach "+str(targetvalue))

elif task == 4:
    lowerbound = 400
    upperbound = 1000
    numtry = 3
    success=False
    while (numtry != 0) and (success == False):
        #print(numtry)
        guess = int(input("Please type a number between "+str(lowerbound)+" and "+str(upperbound)+": "))
        if 400 < guess < 1000:
            print("Congrats!!!")
            success = True
        else:
            print("Wrong!!!")
            numtry = numtry - 1

elif task == 5:
    word = input("Please enter a word: ")
    vowelnum = 0
    for i in range(len(word)):
        if (word[i] == ("a") or (word[i] == ("e")) or (word[i] == ("i")) or (word[i] == ("o")) or (word[i] == ("u"))):
            vowelnum = vowelnum+1
    print(vowelnum)

elif task == 6:
    valid = False
    while valid == False:
        english = int(input("Please input your mark in English: "))
        if 0 <= english <= 100:
            valid = True
        else:
            print("Please enter a mark from 0 to 100.")
    valid = False
    while valid == False:
        maths = int(input("Please input your mark in Maths: "))
        if 0 <= maths <= 100:
            valid = True
        else:
            print("Please enter a mark from 0 to 100.")
    valid = False
    while valid == False:
        ict = int(input("Please input your mark in ICT: "))
        if 0 <= ict <= 100:
            valid = True
        else:
            print("Please enter a mark from 0 to 100.")

    average = (english+maths+ict)/3

    if average >= 65:
        print("Pass with an average of "+str(average))
    else:
        print("Fail with an average of "+str(average))

            

else:
    print("Invalid task selection")