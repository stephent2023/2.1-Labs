print('''
1. Ages list
2. Variable count
3. Time calculator
''')
task = int(input("Please select a task number: "))

### 1. Ages list
if task == 1:
    ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
    for i in range (0, len(ages)):
        print(ages[i])

    for j in range (0, len(ages)):
        ages[j]+=1
    print(ages)

    new_list = [item for item in ages if 15 < item < 66]
    ages = new_list
    print(ages)

    count = 0
    for k in range (0, len(ages)):
        if ages[k]<26:
            count += 1
    print(count)

    ages.sort()
    print(ages)

### 2. Variable count
elif task == 2:
    string = input("Please input a string: ")
    vowelcount = 0
    for i in range (1, len(string)):
        if string[i] in ["a", "e", "i", "o", "u"]:
            vowelcount += 1
    print("Vowel count =",vowelcount)

### 3. Time calculator
elif task == 3:
    print("""Select a mode:
    1-	Add 2 times   
    2-	Find the difference between 2 times  
    3-	Convert to Hours  
    4-	Convert to Minutes  
    5-	Convert Minutes to Time  
    6-	Convert Hours to Time
    7-	Exit  
    """)
    selection = int(input(": "))

    if selection == 1:
        date1 = input("Please enter the first date (DD:HH:MM): ")
        date2 = input("Please input the second date (DD:HH:MM): ")
        date1split = date1.split(":")
        date2split = date2.split(":")
        newdate = [int(date1split[0])+int(date2split[0]),int(date1split[1])+int(date2split[1]),int(date1split[2])+int(date2split[2])]
        if newdate[2]>59:
            newdate[1]+=(newdate[2]//60)
            newdate[2]=newdate[2]%60
        if newdate[1]>23:
            newdate[0]+=(newdate[1]//24)
            newdate[1]=newdate[1]%24
        print("The added date =",newdate[0],":",newdate[1],":",newdate[2])

    elif selection == 2:
        date1 = input("Please enter the first date (DD:HH:MM): ")
        date2 = input("Please input the second date (DD:HH:MM): ")
        date1split = date1.split(":")
        date2split = date2.split(":")

        date1mins = (int(date1split[0])*1440)+(int(date1split[1])*60)+(int(date1split[2]))
        date2mins = (int(date2split[0])*1440)+(int(date2split[1])*60)+(int(date2split[2]))

        minutes = int(abs(date1mins-date2mins))
        print(minutes)

        if minutes > 1439:
            days = minutes//1440
            minutes = minutes - (1440*(minutes//1440))
        else:
            days = 0
        if minutes > 59:
            hours = minutes//60
            minutes = minutes - (60*(minutes//60))
        else:
            hours = 0
        print("Difference = ",days,":",hours,":",minutes)


    elif selection == 3:
        date = input("Please input a date (DD:HH:MM): ")
        datesplit = date.split(":")
        hours = (int(datesplit[0])*24)+(int(datesplit[1]))+(int(datesplit[2])/60)
        print(hours,"hours")

    elif selection == 4:
        date = input("Please input a date (DD:HH:MM): ")
        datesplit = date.split(":")
        mins = (int(datesplit[0])*1440)+(int(datesplit[1])*60)+(int(datesplit[2]))
        print(mins,"mins")

    elif selection == 5:
        minutes = int(input("Please input a number of minutes: "))
        if minutes > 1439:
            days = minutes//1440
            minutes = minutes - (1440*(minutes//1440))
        else:
            days = 0
        if minutes > 59:
            hours = minutes//60
            minutes = minutes - (60*(minutes//60))
        else:
            minutes = 0
        print("This is",days,":",hours,":",minutes)

    elif selection == 6:
        hours = int(input("Please input a number of hours: "))
        if hours > 23:
            days = hours//24
            hours = hours - (24*(hours//24))
        else:
            days = 0
        print("This is ",days,":",hours,": 00")
else:
    print("Invalid task selection.")
