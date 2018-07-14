import random
import sys
import os


#Lesson 10 - Objects/classes
print("\n"*10)

class Animal:
	__name = ""  #underscores make the attribute private
	__height = 0 #to changes these values you need to use a funcition
	__weight = 0 #in the class
	__sound = 0
	
	#constructor
	def __init__(self, name, height, weight, sound):
		self.__name = name
		self.__height = height
		self.__weight = weight
		self.__sound = sound
		
	#setters
	
	def set_name(self, name): #self lets class to refer to itself
		self.__name = name
	def set_height(self, height):
		self.__height =height
	def set_weight(self, weight):
		self.__weight= weight
	def set_sound(self, sound):
		self.__sound = sound
		
	#getters
	def get_name(self):
		return self.__name 
	def get_height(self):
		return self.__height
	def get_weight(self):
		return self.__weight
	def get_sound(self):
		return self.__sound
	
	def get_type(self):
		print("Animal")
		
	def toString(self):
		return "{} is {} cm tall {} kilograms and say {}".format(self.__name,
		self.__height,
		self.__weight,
		self.__sound)
		
		
	
cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())	

#inheritance - making another class with a class and inheriting all it's attributes

class Dog(Animal):
	__owner = ""
	
	def __init__(self, name, height, weight, sound, owner):
		self.__owner = owner
		super().__init__(self, name,height, weight, sound) 
		
		
	def set_owner(self,owner):
		self.__owner = owner
		
	def get_owner(self):
		return self.__owner
		
	def get_type(self):
		print("Dog")
		
	def toString(self):
		return "{} is {} cm tall {} kilograms and say {} and his owner is {}".format(self.__name,
		self.__height,
		self.__weight,
		self.__sound,
		self.__owner)
		
		
	def multiple_sounds(self, how_many=None):
		if how_many is None:
			print(self.get_sounds())
		else: 
			print(self.get_sound()*how_many)
		
charlie = Dog("Charlie", 25, 20, "woof", "Emmanuel")

print(charlie.toString())
		

