#Class Players

class Players:
    def __init__(self,player):
        self.name = player
        self.armour = 30
        self.weapon = "blaster"
        self.health = 100

    def add_health(self,x):
        self.health += x

    def select_weapon(self,w):
        self.weapon = w

player = Players("Alexsandr")
print(player.name)
print(player.armour)
print(player.weapon)
print(player.health)

player.add_health(25)
print(player.health)

player2 = Players("Mouse")
player2.select_weapon("Gun")
print(player2.name,player2.health,player2.weapon,player2.armour)



#Class Dog

class Dog:
    def __init__(self, name, age):
        
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy", 3)
my_dog2 = Dog("Bonia",5)
my_dog.name = "Rex"

print(my_dog.name)  # Вывод: Buddy
print(my_dog2.name)  # Вывод: Buddy

print(my_dog.bark())  # Вывод: Buddy says woof!  
print(my_dog2.bark())  # Вывод: Buddy says woof!  




#Class Animal.
#Class animal has Dog,Cat,Bird.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} sing"

animals = [Dog("Buddy"), Cat("Whiskers"),Bird("Lemon")]
for animal in animals:
    print(animal.speak())




#Class Vehicle.
#Classe Vehicle has Car


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Вызов конструктора родителя
        self.doors = doors
    def info(self):
        return f"{super().info()} with {self.doors} doors"
    
class Plane(Vehicle):
    def __init__(self, make, model,long,height):
        super().__init__(make, model)  # Вызов конструктора родителя
        self.long = long
        self.height = height

    def info(self):
        return f"{super().info()} with {self.height} height, {self.long} long"
#Использование нового класса
#Создаем объект класса Car:

my_car = Car("Toyota", "Corolla", 4)
print(my_car.info())  # Вывод: Toyota Corolla with 4 doors

my_plane = Plane("Il", "-2",20,10)
print(my_plane.info())  # Вывод: Toyota Corolla with 4 doors





#Class player for game

class Player:
    def __init__(self,player): 
        self.name = player
        self.armour = 200
        self.health = 1000
        self.weapon = "pump-action shotgun"

    
    def add_health(self,x):
        self.health += x

    def select_weapon(self,w):
        self.weapon = w


#player.add_health(25)
#print(player.health)

player = Player("Bob")
player.select_weapon("Katana")

player2 = Player("Jim")
player2.select_weapon("Gun")

player3 = Player("Sarash")
player3.select_weapon("Bluster")

player4 = Player("Car3476")
player4.select_weapon("Minigun")

#print(player2.name,player2.health,player2.weapon,player2.armour)
#print(player3.name,player3.health,player3.weapon,player3.armour)

print("Name:",player.name)
print("Armour:",player.armour)
print("Health:",player.health)
print("Weapon:",player.weapon)

print("Name:",player2.name)
print("Armour:",player2.armour)
print("Health:",player2.health)
print("Weapon:",player2.weapon)

print("Name:",player3.name)
print("Armour:",player3.armour)
print("Health:",player3.health)
print("Weapon:",player3.weapon)

print("Name:",player4.name)
print("Armour:",player4.armour)
print("Health:",player4.health)
print("Weapon:",player4.weapon)


