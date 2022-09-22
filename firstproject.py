#!/usr/bin/env python3


#convert string to list
def Convert(string):
    li = list(string.split(" "))
    return li


print("Welcome to Zodiac Predictor")
#Prompt user to enter a name, and store the input in user_name variable and convert to lowercase

user_name = input("Please enter your name: ")
user_name = user_name.lower()

print(user_name)
#Prompt user to enter a date of birth in a specified format , and store the input in dob variable and convert to lowercase
dob = input("Enter date of birth (e.g October 1) : ")
dob = dob.lower()

#convert dob to a list
date_of_birth = Convert(dob)
#Convert the day in user to an integer and save in variable day
day =int(date_of_birth[-1])

#CHECK IF USER INPUT MEETS aQUARIUS CRITERIA
if ((32 > day > 19) and (date_of_birth[0] == "january")) or (  (19 > day > 0) and (date_of_birth[0] == "february")):
    print("Aquarius")

#CHECK IF USER INPUT MEETS PISCES CRITERIA
elif ((32 > day > 19) and (date_of_birth[0] == "february")) or (  (20 > day > 0) and (date_of_birth[0] == "march")):
    print("Pisces")
#CHECK IF USER INPUT MEETS PISCES CRITERIA
elif ((32 > day > 19) and (date_of_birth[0] == "february")) or (  (20 > day > 0) and (date_of_birth[0] == "march")):
    print("Aries")
else:
    print(day)


