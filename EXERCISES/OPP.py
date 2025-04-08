class Animal:       #Create a class called Animal
    def __init__(self, name, species):      #Attributes: name and species
        self.name = name
        self.species = species
        self._age = 0       #adds a private attribute: _age
    def get_age(self):      #to access the _age attribute
        return self._age
        
    def set_age(self, age):     #to modify the _age attribute
        if age >= self._age:    #adds a validation to ensure the age is not negative
            self._age = age
        else:
            print("Your cannot have negative age!.")

    def make_sound(self):       #Method with a generic animal sound
        return "Animal sound"
    
    def get_attribute(self):
        return f"{self.name} {self.species}".title()
    
class Dog(Animal):      #Create a subclass Dog
    def __init__(self, name, species, breed):
        Animal.__init__(self, name, species)
        self.breed = breed      #adds a unique attribute: breed

    def make_sound(self):       #Will override the make_sound() method
        return "Woof!"
    
    def get_dog_attribute(self):
        return self.get_attribute() + "" + self.breed
    
class Cat(Animal):      #Create a subclass Dog
    def __init__(self, name, species, favorite_toy):
        Animal.__init__(self, name, species)
        self.favorite_toy = favorite_toy        #adds a unique attribute: favorite_toy

    def make_sound(self):       #Will override the make_sound() method
        return "Meow!" 
    
    def get_cat_attribute(self):
        return self.get_attribute() + "" + self.favorite_toy

class Cow(Animal):
    def make_sound(self):       
        return "Moo!" 

class Sheep(Animal):
    def make_sound(self):       
        return "~Mee!"
    
class Snake(Animal):
    def make_sound(self):       
        return "Hiss!"

class Owl(Animal):
    def make_sound(self):       
        return "Hoot!"
    
Animal_list = [     #Create a list of Animal Objects
    Dog("June", "Dog", "Askal"),
    Cat("Gwyn", "Cat", "Toy mices"),
    Cow("Mima", "Cow"), Sheep("Jul", "Sheep"), Snake("Zitch", "Snake"), Owl("Ott", "Owl")
]

for animal in Animal_list:      #iterate through the list and calls the make_sound() method
    print(animal.make_sound())

june = Dog("June", "Dog", "Askal")      #instance of Dog class
gwyn = Cat("Gwyn", "Cat", "Toy miceS")  #instance of Cat class

#Demonstration of getter and setter methods for _age attribute
june.set_age(6900)
print(f'June age is {june.get_age()}')
print(june.get_dog_attribute())

gwyn.set_age(50)
print(f'Gwyn age is {gwyn.get_age()}')
print(gwyn.get_cat_attribute())