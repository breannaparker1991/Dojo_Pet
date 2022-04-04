class Pet:
  def __init__(self, name , tricks):
    self.name = name
    self.tricks = tricks
    self.energy = 100
    self.health = 100
    
  def sleep(self):
    if self.energy < 75:
      self.energy += 25
    else:
      Pet.noise(self)
      return self
  
  def eat(self):
    if self.health < 80:
      self.energy += 5
      self.health += 10
    else:
      Pet.noise(self)
    return self
  
  def play(self):
    self.health -= 5
    self.energy -= 5
    Pet.noise(self)
    return self
  
  def noise(self):
    self.energy -= 1
    print(self.sound)
    return self
  
  def  stats(self):
    print(f"Energy: {self.energy}, Health: {self.health}")
    
class Dog(Pet):
  def __init__(self, name, tricks, breed):
      super().__init__(name, tricks)
      self.breed = breed
      self.sound = "Bark"
      
class Cat(Pet):
  def __init__(self, name, tricks, color):
      super().__init__(name, tricks)
      self.color = color
      self.sound = "Meow"

class Ninja():
  def __init__(self, first_name , last_name , pet ):
    self.first_name = first_name  
    self.last_name = last_name
    self.treats = 3 	
    self.pet_food = 5
    self.pet = pet
    
  def walk(self):
    self.pet.play()
    return self
  
  def feed(self):
    if self.pet_food > 0:
      self.pet.eat()
      self.pet_food -= 1
    else:
      print("Buy More Pet Food!")
    return self
  
  def bathe(self):
    self.pet.noise()
    if self.treats > 0:
      self.treats -= 1
    else:
      print ("Buy More Treats!")
    return self
  
  def Check_on_pet (self):
    self.pet.stats()

Snickers = Dog("Snickers", "sit", "maltese")
Ripley = Cat("ripley", "stare", "black" )
Bree = Ninja("Bree", "Parker", Snickers & Ripley)


Bree.bathe(Snickers).walk(Snickers).feed(Snickers)
Bree.Check_on_pet(Snickers)
print(Snickers.breed)
print(Ripley.color)
Bree.bathe(Ripley).walk(Ripley).feed(Ripley)
Bree.Check_on_pet(Ripley)