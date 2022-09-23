#!/usr/bin/env python3

import matplotlib.pyplot as plt

import crayons
# fnction to convert string to list

def Convert(string):
    li = list(string.split(" "))
    return li


def main():

    exit = 1

    print(f"{crayons.red('come here with me')}")

    while (exit == 1):

        zodiac_sign = ""

        print(
            f"{crayons.green('== == == == == ==Welcome to Zodiac Predictor == == == == == ==')}")
        # Prompt user to enter a name, and store the input in user_name variable and convert to lowercase

        user_name = input("Please enter your name: ")
        user_name = user_name.capitalize()

        # Prompt user to enter a date of birth in a specified format , and store the input in dob variable and convert to lowercase
        dob = input("Enter month and day of birth (e.g October 1) : ")
        dob = dob.lower()

        # convert dob to a list
        date_of_birth = Convert(dob)
        # Convert the day in uer inout (date of birth) to an integer and save in variable day
        day = int(date_of_birth[-1])

        # if( len(date_of_birth) < 1 or len(date_of_birth[0] < 4)):

        #     print("enter a valid date: ")

        # CHECK IF USER INPUT MEETS aQUARIUS CRITERIA
        if ((32 > day > 19) and (date_of_birth[0] == "january")) or ((19 > day > 0) and (date_of_birth[0] == "february")):
            zodiac_sign = "Aquarius"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")

            print(f"{crayons.green('Aquarius Traits')}")


        elif ((30 > day > 18) and (date_of_birth[0] == "february")) or ((21 > day > 0) and (date_of_birth[0] == "march")):
            zodiac_sign = "Pisces"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")

            print(f"{crayons.green('Pisces Traits')}")


        elif ((32 > day > 20) and (date_of_birth[0] == "march")) or ((20 > day > 0) and (date_of_birth[0] == "april")):

            zodiac_sign = "Aries"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")

            print(f"{crayons.green('Aries Traits')}")


        elif ((31 > day > 19) and (date_of_birth[0] == "april")) or ((21 > day > 0) and (date_of_birth[0] == "may")):

            zodiac_sign = "Taurus"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")

            print(f"{crayons.green('Taurus Traits')}")

        elif ((32 > day > 20) and (date_of_birth[0] == "may")) or ((21 > day > 0) and (date_of_birth[0] == "june")):

            zodiac_sign = "Pisces"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(f"{crayons.green('Pisces Traits')}")

        elif ((31 > day > 20) and (date_of_birth[0] == "june")) or ((23 > day > 0) and (date_of_birth[0] == "july")):

            zodiac_sign = "Cancer"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(f"{crayons.green('Cancer Traits')}")
        # CHECK IF USER INPUT MEETS LEO CRITERIA

        elif ((32 > day > 22) and (date_of_birth[0] == "july")) or ((18 > day > 0) and (date_of_birth[0] == "august")):

            zodiac_sign = "Leo"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(f"{crayons.green('Leo Traits')}")

        # CHECK IF USER INPUT MEETS VIRGO CRITERIA
        elif ((32 > day > 22) and (date_of_birth[0] == "august")) or ((23 > day > 0) and (date_of_birth[0] == "september")):
            zodiac_sign = "Virgo"

            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(f"{crayons.green('Virgo Traits')}")

        # CHECK IF USER INPUT MEETS LIBRA CRITERIA
        elif ((31 > day > 22) and (date_of_birth[0] == "september")) or ((23 > day > 0) and (date_of_birth[0] == "october")):
            zodiac_sign = "Libra"

            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(f"{crayons.green('Libra Traits')}")

        # CHECK IF USER INPUT MEETS SCORPIO CRITERIA
        elif ((32 > day > 22) and (date_of_birth[0] == "october")) or ((22 > day > 0) and (date_of_birth[0] == "november")):
            zodiac_sign = "Scorpio"

            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(f"{crayons.green('Scorpio Traits')}")

        # CHECK IF USER INPUT MEETS SAGITTARIUS CRITERIA
        elif ((31 > day > 21) and (date_of_birth[0] == "november")) or ((22 > day > 0) and (date_of_birth[0] == "december")):
            zodiac_sign = "Saggitarius"

            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")

            print(f"{crayons.green('Sagittarius Traits')}")

            print(
                f"{crayons.blue('Strengths: Generous, idealistic, great sense of humors')}")

        # CHECK IF USER INPUT MEETS SAGITTARIUS CRITERIA
        elif ((32 > day > 21) and (date_of_birth[0] == "december")) or ((20 > day > 0) and (date_of_birth[0] == "january")):
            zodiac_sign = "Capricorn"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
        else:
            print("Enter a valid date: ")

        print("Enter 1 to continue using Zodiac Predictor or 0 to exit: ")

        new = input()
        exit = int(new)

    print(f"Have a nice day {user_name}.")

main()




