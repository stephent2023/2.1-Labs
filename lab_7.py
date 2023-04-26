class Student:
    def __init__(self, name, age, currclass):
        self.name = name
        self.age = age
        self.currclass = currclass
    def getage(self):
        print("My age is",self.age)
    def scoreaverage(self, score1, score2, score3):
        print("Average =",(score1+score2+score3)/3)

class Bird:
    def __init__(self, name, species, can_fly):
        self.name = name
        self.species = species
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly == True:
            print(f"{self.name} is flying!")
        else:
            print(f"{self.name} can't fly! :(")

    def __str__(self):
        return f"{self.name} ({self.species}, {self.can_fly})"

class Owl(Bird):
    def __init__(self, name, can_fly, species):
        super().__init__(name, species, can_fly)

    def hoot(self):
        print(f"{self.name}: Hoot!")


class Dodo(Bird):
    def __init__(self, name, can_fly, species):
        super().__init__(name, species, can_fly)

student1 = Student("Johnny", 19, "maths")
student2 = Student("Jeff", 25, "english")
student1.getage()
student1.scoreaverage(4,5,6)

owl1 = Owl("Joe", True, "Barn")
owl1.hoot()

dodo1 = Dodo("Billy", False, "Dodo")
dodo1.fly()
