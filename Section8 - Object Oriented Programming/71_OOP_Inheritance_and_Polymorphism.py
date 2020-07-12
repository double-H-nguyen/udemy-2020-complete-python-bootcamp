# INHERITANCE
# Base class


class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


# Dog class will inherit Animal class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog")

    def eat(self):
        print("I a dog and am eating")

    def bark(self):
        print("WOOF!")


my_animal = Animal()
print()
my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()
print()

# POLYMORPHISM


class Doggy():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Kitty():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


def pet_speak(pet):
    print(pet.speak())


niko = Doggy("Niko")
felix = Kitty("Felix")
pet_speak(niko)
pet_speak(felix)
print()


# ABSTRACT CLASS
class Mammal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            "Subclass must implement this abstract method")


class Doge(Mammal):
    def speak(self):
        return self.name + " says woof!"


class Kidoge(Mammal):
    def speak(self):
        return self.name + " says meow!"


my_doge = Doge("Henry")
my_kidoge = Kidoge("Michelle")
print(my_doge.speak())
print(my_kidoge.speak())
print()
