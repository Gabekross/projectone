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
elif ((30 > day > 18) and (date_of_birth[0] == "february")) or (  (21 > day > 0) and (date_of_birth[0] == "march")):
    print("Pisces")
#CHECK IF USER INPUT MEETS PISCES CRITERIA
elif ((32 > day > 20) and (date_of_birth[0] == "march")) or (  (18 > day > 0) and (date_of_birth[0] == "march")):
    print("Aries")

#CHECK IF USER INPUT MEETS TAURUS CRITERIA
elif ((31 > day > 19) and (date_of_birth[0] == "april")) or (  (18 > day > 0) and (date_of_birth[0] == "march")):
    print("Taurus")

#CHECK IF USER INPUT MEETS TAURUS CRITERIA
elif ((32 > day > 20) and (date_of_birth[0] == "may")) or (  (18 > day > 0) and (date_of_birth[0] == "march")):
    print("Gemini")


#CHECK IF USER INPUT MEETS Cancer CRITERIA
elif ((31 > day > 20) and (date_of_birth[0] == "june")) or (  (18 > day > 0) and (date_of_birth[0] == "march")):
    print("Cancer")
#CHECK IF USER INPUT MEETS LEO CRITERIA

elif ((32 > day > 22) and (date_of_birth[0] == "july")) or (  (18 > day > 0) and (date_of_birth[0] == "march")):
    print("Leo")

#CHECK IF USER INPUT MEETS VIRGO CRITERIA
elif ((32 > day > 22) and (date_of_birth[0] == "august")) or (  (18 > day > 0) and (date_of_birth[0] == "march")):
    print("Virgo")

#CHECK IF USER INPUT MEETS LIBRA CRITERIA
elif ((31 > day > 22) and (date_of_birth[0] == "september")) or (  (18 > day > 0) and (date_of_birth[0] == "march")):
    print("Libra")


#CHECK IF USER INPUT MEETS SCORPIO CRITERIA
elif ((32 > day > 22) and (date_of_birth[0] == "october")) or (  (18 > day > 0) and (date_of_birth[0] == "march")):
    print("Scorpio")

#CHECK IF USER INPUT MEETS SAGITTARIUS CRITERIA
elif ((31 > day > 21) and (date_of_birth[0] == "november")) or (  (18 > day > 0) and (date_of_birth[0] == "march")):
    print("Sagittariuis")

#CHECK IF USER INPUT MEETS SAGITTARIUS CRITERIA
elif ((32 > day > 21) and (date_of_birth[0] == "december")) or (  (18 > day > 0) and (date_of_birth[0] == "march")):
    print("capricorn")
else:
    print("Enter a valid date: ")




