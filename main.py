# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("This line will be printed.")
x = 1
if x == 1:
    # indented four spaces, no curly brackets but tabs work along with the std four spaces
    print("x is 1.")
    print("Goodbye, World!")
    print(x)
    myfloat = 7.0
    print(myfloat)
    myfloat = float(7)
    print(myfloat)
    mystring = 'hello'
    print(mystring)
    mystring = "hello"
    print(mystring)
    # examples of pythons type of variables, float, int, string

one = 1
two = 2
three = one + two
print(three)
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
#examples of combining things

#this is aloud
a, b = 3, 4 #odd way to define things
print(a,b)

#lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
#python calls arrays lists
# prints out 1,2,3
for x in mylist:
    print(x)
#you can use basic operators used in arthmatic in strings
helloworld = "hello" + " " + "world"
print(helloworld)
lotsofhellos = "hello" * 10 #repeating strings
print(lotsofhellos)
#same thing applies to lists too
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# This prints out "Hello, John!"
#python uses c-style printf formatting
name = "John"
print("Hello, %s!" % name)
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

#Basic String Operations
astring = "Hello world!"
print(len(astring))
#prints length of astring
astring = "Hello world!"
print(astring.index("o"))
#That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character.
print(astring.count("l"))
#This counts the number of l's in the string.
print(astring[3:7:2])
#This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax.
#The general form is [start:stop:step].
print(astring[::-1])
#with the above mentioned type of slice syntax you can easily reverse a string like this
print(astring.upper())
print(astring.lower())
#change case
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
#This is used to determine whether the string starts with something or ends with something, respectively.
afewwords = astring.split(" ")
#This splits the string into a bunch of strings grouped together in a list.

#Boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

#The "in" operator
if name in ["John", "Rick"]:

    print("Your name is either John or Rick.")
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

#The 'is' operator
#Unlike the double equals operator "==", the "is" operator does not match the values of the variables,
# but the instances themselves.
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#The "not" operator
print(not False) # Prints out True
print((not False) == (False)) # Prints out False

#loops
#for loop
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
#while loop
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

#"break" and "continue" statements
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

#you can use else in for/while loops
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

#functions
def my_function(arg1, arg2):
    print(arg1+arg2)
    return arg1
#call a function like this


my_function(1,2)

#Classes and Objects
#Objects are an encapsulation of variables and functions into a single entity.
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
#access like this:

myobjectx = MyClass()
myobjectx.variable

myobjectx.function()

#A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
# #Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.)
# #instead of using its index to address it.
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#to go through a dictionary, since there isn't an index, do this:
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#removing a value from a dictionary
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

#Modules and Packages
# import the draw module
import draw

#Importing module objects to the current namespace
from draw import draw_game

#Importing all objects from a module
from draw import *

