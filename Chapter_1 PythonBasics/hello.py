# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?') # ask user for their name

myName = input()
print('It is good to meet you, ' + myName)

print('The length of your name is:')
print(len(myName))

print('What is your age') # ask user for their age
myAge = input()
print('you will be ' + str(int(myAge) + 1) + ' in a year.')

spam = int(input())

print(spam)