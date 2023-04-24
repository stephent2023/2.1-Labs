import re
import time

print('''
1. Ages list
2. Vowel count
3. Time calculator
''')
task = int(input("Please select a task number: "))

### 1. Ages list
if task == 1:
    ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

    #Print length of list
    print(len(ages))

    #Print ages one by one
    for i in range (0, len(ages)):
        print(ages[i])

    #Add one to every age
    for j in range (0, len(ages)):
        ages[j]+=1
    print(ages)

    #Remove items outside of 16 to 65
    new_list = [item for item in ages if 15 < item < 66]
    ages = new_list
    print(ages)

    #Count items lover than 26
    count = 0
    for k in range (0, len(ages)):
        if ages[k]<26:
            count += 1
    print(count)

    #Sort the list
    ages.sort()
    print(ages)

### 2. Vowel count
elif task == 2:
    string = input("Please input a string: ")
    vowelcount = 0
    for i in range (1, len(string)):
        if string[i] in ["a", "e", "i", "o", "u"]:
            vowelcount += 1
    print("Vowel count =",vowelcount)

### 3. Time calculator
elif task == 3:
    #Format definition DD:HH:MM
    format = re.compile('.{2}:.{2}:.{2}')
    #While loop to hold the user in the program
    while True:
        print("""
=============== Select a mode: ===============
1-	Add 2 times   
2-	Find the difference between 2 times  
3-	Convert to Hours  
4-	Convert to Minutes  
5-	Convert Minutes to Time  
6-	Convert Hours to Time
7-	Exit    
==============================================
        """)
        selection = int(input(": "))

        #Date adder
        if selection == 1:
            date1 = input("Please enter the first date (DD:HH:MM): ")
            date2 = input("Please input the second date (DD:HH:MM): ")
            #Check for format
            if (format.match(date1)) and (format.match(date2)):
                #Split date into lists
                date1split = date1.split(":")
                date2split = date2.split(":")
                #Add date lists
                newdate = [int(date1split[0])+int(date2split[0]),int(date1split[1])+int(date2split[1]),int(date1split[2])+int(date2split[2])]
                #Check hours and minutes fall into 24 hours and 60 minutes
                if newdate[2]>59:
                    newdate[1]+=(newdate[2]//60)
                    newdate[2]=newdate[2]%60
                if newdate[1]>23:
                    newdate[0]+=(newdate[1]//24)
                    newdate[1]=newdate[1]%24
                #Print
                print("The added date =",newdate[0],":",newdate[1],":",newdate[2])
                time.sleep(3)
            else:
                print("Invalid format!!")

        #Date subtractor
        elif selection == 2:
            date1 = input("Please enter the first date (DD:HH:MM): ")
            date2 = input("Please input the second date (DD:HH:MM): ")

            #Check format
            if (format.match(date1)) and (format.match(date2)):
                #Split date to lists
                date1split = date1.split(":")
                date2split = date2.split(":")

                #Convert dates into minutes
                date1mins = (int(date1split[0])*1440)+(int(date1split[1])*60)+(int(date1split[2]))
                date2mins = (int(date2split[0])*1440)+(int(date2split[1])*60)+(int(date2split[2]))

                #Get difference in minutes
                minutes = int(abs(date1mins-date2mins))
                print(minutes)

                #Format minutes into days and hours
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
                #Print
                print("Difference = ",days,":",hours,":",minutes)
                time.sleep(3)
            else:
                print("Invalid format!!")

        #Convert to hours
        elif selection == 3:
            date = input("Please input a date (DD:HH:MM): ")
            #Check format
            if format.match(date):
                #Split date into list
                datesplit = date.split(":")
                #Calculate days into hours and minutes into decimal
                hours = (int(datesplit[0])*24)+(int(datesplit[1]))+(int(datesplit[2])/60)
                #Print
                print(hours,"hours")
                time.sleep(3)
            else:
                print("Invalid format")

        #Convert to minutes
        elif selection == 4:
            date = input("Please input a date (DD:HH:MM): ")
            #Check format
            if format.match(date):
                #Split date into list
                datesplit = date.split(":")
                #Convert days and hours into minutes
                mins = (int(datesplit[0])*1440)+(int(datesplit[1])*60)+(int(datesplit[2]))
                #Print
                print(mins,"mins")
                time.sleep(3)
            else:
                print("Invalid format!!")

        #Convert minutes into days and hours
        elif selection == 5:
            minutes = int(input("Please input a number of minutes: "))
            #Count number of days and hours in minutes
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
            #Print
            print("This is",days,":",hours,":",minutes)
            time.sleep(3)

        #Convert hours into days
        elif selection == 6:
            hours = int(input("Please input a number of hours: "))
            #Count number of days in hours
            if hours > 23:
                days = hours//24
                hours = hours - (24*(hours//24))
            else:
                days = 0
            #Print
            print("This is ",days,":",hours,": 00")
            time.sleep(3)

        elif selection == 7:
            print("Thankyou!!")
            break

else:
    print("Invalid task selection.")
