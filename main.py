# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# declaring variable is very simple you can directly declare variable without any data types
#
# firstName = "Hammad"
# myAge = 25
# print("Hello hammad welcome to python world")
# print(myAge)
#
# # you can take input from terminal using input.
# name = input("What is your name ? ")
#
# print("hello " + name + " good morning")

# type conversion

# yearOfBirth = input("what is your birth year? ")
# # calculate your age
#
# age = 2023 - int(yearOfBirth)  # there are more conversion type like str(), bool(), float() etc
#
# print(age)

# stringLearn = 'Learn methods of string'
#
# ind = stringLearn.index('e')  # there are many methods like js replace, find, toUpperCase etc.
#
# print(ind)
#
# # in keyword check if that particular string is present or not
# print('methods' in stringLearn)
#
# if ind > 7:
#     print('your index is greater than 7')
#     print("this block will also printed because it in same alignment")
# elif ind < 7:
#     print('your index is less than 7')
# else:
#     print("this is else block")
#
# print("this will always printed because its not in scope of if : in python colons means curly braces")

# while loop
#
# num = 2
#
# while num < 6:
#     print(num)
#     num+=1

# List

# names = ["hammad", "zaid", "shadan", "kashfi"]
#
# print(names[0])
# print(names[1])
# print(names[-2])
# print(names[-1])
#
# # range [0:3]
#
# print(names[0:3])
#
# # array methods
#
# names.append(65)   # similar to push
# names.insert(0, "first word")    # it takes index on which u want to updated the element
#
# print(names)
#
# print(64 in names)  #check if exists in array
#
# print(len(names))  #same as length
#
# # for loops
#
# for item in names:
#     print(item)
#

# nums = range(0,12)  #it will print a certain range of num where we can also pass tird argumrnt for difference
#
# for num in nums:
#     print(num)

# Tupples

# numbers = (1, 2, 3, 4) # tupples can not be mutated
# functions

def add (n1, n2) :
    return n1 + n2
number = add(2, 9)
print(number)

def greet (name):
    print(f"hello {name}")

greet("zaid")



