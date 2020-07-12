class Dog():
    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self, number):
        print(f"WOOF! My name is {self.name} and the number is {number}")


my_dog = Dog("Lab", "Sammy", False)
my_dog2 = Dog(breed="Poodle", name="Phillis", spots=False)
print(my_dog.species)
print(my_dog2.species)
my_dog.bark(5)
my_dog2.bark(10)


class Circle():
    pi = 3.13

    def __init__(self, radius=1):
        self.radius = radius
        self.area = Circle.pi * (radius ** 2)

    def get_circumference(self):
        return 2 * Circle.pi * self.radius


my_circle = Circle()
print(my_circle.pi)
print(my_circle.get_circumference())
print(my_circle.area)
