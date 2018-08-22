import random
import sys
import os


#Lesson 10 - Objects/classes
print("\n"*10)

class Animal:
	name = ""  #underscores make the attribute private
	height = 0 #to changes these values you need to use a funcition
	weight = 0 #in the class
	sound = 0
	
	#constructor
	def __init__(self, name, height, weight, sound):
		self.name = name
		self.height = height
		self.weight = weight
		self.sound = sound
		
	#setters
	
	def set_name(self, name): #self lets class to refer to itself
		self.name = name
	def set_height(self, height):
		self.height =height
	def set_weight(self, weight):
		self.weight= weight
	def set_sound(self, sound):
		self.sound = sound
		
	#getters
	def get_name(self):
		return self.name 
	def get_height(self):
		return self.height
	def get_weight(self):
		return self.weight
	def get_sound(self):
		return self.sound
	
	def get_type(self):
		print("Animal")
		
	def toString(self):
		return "{} is {} cm tall {} kilograms and say {}".format(self.name,
		self.height,
		self.weight,
		self.sound)
		
		
	
cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())	

#inheritance - making another class with a class and inheriting all it's attributes
class Dog(Animal):
    def __init__(self, name, height, weight, sound, owner):
        super(Dog, self).__init__(name, height, weight, sound) 
        
        self.ownerName = owner
        
    def set_owner(self, owner):
        self.ownerName = owner
        
    def get_owner(self):
        return self.ownerName
        
    def get_type(self):
        print("Dog")
    
    def toString(self):
        return "{} is {} cm tall {} kilograms and says {} and his owner is {}".format(self.name, self.height,self.weight,self.sound, self.ownerName)
    
charlie = Dog('charlie', 20, 30, 'woof', 'Emmanuel')

print(charlie.toString())
