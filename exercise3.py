''' Create a program that asks the user to enter their name and their age. Print out a message
addressed to them that tells them the year that they will turn 100 years old '''
name = input("enter your name")
age = int(input("enter your age"))

hundered_year=2021+(100-age)
print(name, 'you will turn 100 years in ' , hundered_year)
