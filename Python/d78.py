# Single Inheritance 

# Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.


class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed

    def make_sound(self):
        print("Bark !")

d=Dog("Dog","Doggerman")
d.make_sound()

a=Animal("Dog","Dog")
a.make_sound()

