# poluymorphism, encapsulation, inheritance, abstraction

#polymorphism - same method name but different implementation
# composition - has a relationship : ex : verhicle (car, truck, ..) has a engine (getOn() , getOff()) ,  car.getengine().getOn()
# inheritance - is a relationship : ex : dog is a animal

class Animal:
    def __init__(self, weight, color, age, anime_type):
        self.__weight = weight  # __weight is a private variable - encapsulation
        self.color = color      # color is a public variable
        self.age = age
        self.anime_type = anime_type
    
    
    # encapsulation of weight variable
    # Getter method
    def get_weight(self):
        return self.__weight
    # setter method
    def set_weight(self, weight):
        self.__weight = weight

    # abstraction
    def eat(self):
        print("Eating...")
    def sleep(self):
        print("Sleeping...")
    def bark(self):
        print("No !")


# inheritance - Dog class inherits Animal class
class Dog(Animal): 
    # all animal attributes are inherited
    # all animal methods are inherited
    def __init__(self, weight, color, age, anime_type, breed, name): # self is a reference to the object
        super().__init__(weight, color, age, anime_type) # calling the constructor of parent class
        self.breed = breed 
        self.name = name

    def bark(self):
        print("Woof! Woof!")

    # overriding the eat method of Animal class
    def eat(self):
        print("Dog is eating...")


class Cat(Animal):
    def __init__(self, weight, color, age, anime_type, breed, name):
        super().__init__(weight, color, age, anime_type)
        self.breed = breed
        self.name = name

    def bark(self):
        print("Meo !")


dog = Dog(10, "brown", 2, "mammal", "labrador", "Tommy")
print(dog.color)
print(dog.get_weight())
print(dog.eat())

# polymorphism - cat is Animal object
cat = Animal(5, "white", 1, "mammal")
print(cat.color)



zoo = []
cat2 = Cat(5, "white", 1, "mammal", "persian", "Kitty")
zoo.append(cat)
zoo.append(cat2)
zoo.append(dog)

for animal in zoo:
    animal.bark()


