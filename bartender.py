milkshakes = {
    "Strawberry": 5,
    "Banana": 4,
    "Caramel": 6
}

budget = int(input("Please input your budget: "))

while True:
    print(milkshakes)
    print("------------------------------")
    choice = input("What would you like? ")
    if choice == "q":
        print("Goodbye!!")
        break
    elif choice == "1":
        if budget >= milkshakes["Strawberry"]:
            print("Here you go!")
            budget -= milkshakes["Strawberry"]
            print("You have",budget,"left.")
        else:
            print("Get outta here!")
            break
    elif choice == "2":
        if budget >= milkshakes["Banana"]:
            print("Here you go!")
            budget -= milkshakes["Banana"]
            print("You have",budget,"left.")
        else:
            print("Get outta here!")
            break
    elif choice == "3":
        if budget >= milkshakes["Caramel"]:
            print("Here you go!")
            budget -= milkshakes["Caramel"]
            print("You have",budget,"left.")
        else:
            print("Get outta here!")
            break
    else:
        print("Huh?")
