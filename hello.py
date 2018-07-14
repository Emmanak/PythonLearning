import random
import sys
import os

#PRINT LESSON
print("Lesson 1 - Print statement")

name = "Emmanuel"

print("my name is" ,name)

grocery_list = ['peanutbutter', 'bananas','food', 'drink']

#print grocery_list

print ('I like to eat' ,grocery_list[1] ,'with' ,grocery_list[0])

print( grocery_list[0:3])

print(len(grocery_list))

qoute = "\"always remember you are unique"

multi_line_quote = '''just like
everyone else'''

print("%s %s %s" % ('I like the quote', qoute, multi_line_quote))

print("I don't like", end="")
print(" newline")
print("\n"*10)


print("Lesson 2 - Lists")
print(grocery_list)
grocery_list.append('Onion')
grocery_list.insert(1,'Pickle')
print(grocery_list)
print("\n"*10)


#lesson 3 - Tuples
print("Lesson 3 - tupples")

pi_tuple = (1,2,3,4,5,6)
print(pi_tuple)
new_tuple = list(pi_tuple)
print(new_tuple)
len(pi_tuple)


#lesson 4 - dictionaries
print("\n"*10)
print("Lesson 4 - Dictionaries")
super_villans = {'Fiddler' : 'Isaac Bowin', 'Captain Cold': 'Leonard Snart',  'Batman': 'Joker', 'Superman': 'Lex Luther'}
print(super_villans['Batman'])
print(super_villans.get('Superman'))
print(super_villans.keys())
print(super_villans.values())



#lesson 5 - Conditionals
print("\n")
print("I'm going to skip this lesson because it's similar. \n just note that conditional statements end with :")


#lesson 6 - Looping
print("\n"*10)
print("Lesson 6 - Looping")
for x in range(0,10):
	print(x, ' ', end="")
for y in grocery_list:
	print(y)
for z in [2,4,6,8,10]:
	print(z)
	
num_list = [[1,2,3,], [10,20,30], [100, 200, 300]]

for mat in range (0,3):
	for mat2 in range(0,3):
		print(num_list[mat][mat2])
		
#Lesson 7 - Functions
print("\n"*10)
print("Lesson 7- Functions")

def addNumber(fNum, lNum):
	sumNum=fNum + lNum
	return sumNum
	
string = addNumber(1,4)
print("1+4=",string)

#Lesson 8 - UserInputs
print("\n"*10)
print("What is your name?")

#name1 = sys.stdin.readline()
#print("Hello", name1)


#Lesson 9 - File I/O
print("\n"*10)

test_file = open("test", "wb") #wb is to write to the file
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("test file for python\nYou should be able to read this", 'UTF-8'))

test_file.close()

test_file = open("test", "r+") #read file
text_in_file = test_file.read()
print(text_in_file)

os.remove("test") #delete file

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
		

