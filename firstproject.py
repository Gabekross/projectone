#!/usr/bin/env python3

"""A simple script to predict 
   a users zodiac sign | olugabriel80@gmail.com"""

#importing crayons library . This helps add colors to text ouput in terminal
import crayons
# fnction to convert string to list

"This function converts a string to a list"
def Convert(string):
    li = list(string.split(" "))
    return li


def main():


    #intial value for exit varible to be used in the while looop
    exit = 1

    #while loop to keep program running until user enters any other character to exit the program

    while (exit == 1):

        #create variable zodiac_sign and set it to an empty string
        zodiac_sign = ""

        print(
            f"{crayons.green('== == == == == ==Welcome to Zodiac Predictor == == == == == ==')}")
        # Prompt user to enter a name, and store the input in user_name variable and convert to lowercase
        user_name = input("Please enter your name: ")
        user_name = user_name.capitalize()

        # Prompt user to enter a date of birth in a specified format , and store the input in dob variable
        dob = input("Enter month and day of birth (e.g October 1) : ")

        print(
            f"{crayons.green('== == == == == ==== == == == == == == == == == == ==')}")
        #convert dob to lower case to ensure that dob variable used in the later part of script is in lower case
        dob = dob.lower()

        # Use convert fucntion to convert dob to a list and assign corresponsinf list to date_of_birth
        date_of_birth = Convert(dob)
        # Convert the day in user inout (date of birth) to an integer and save value in variable day
        day = int(date_of_birth[-1])


        # CHECK IF USER INPUT MEETS AQUARIUS CRITERIA
        if ((32 > day > 19) and (date_of_birth[0] == "january")) or ((19 > day > 0) and (date_of_birth[0] == "february")):
            zodiac_sign = "Aquarius"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")

            print(
                f"{crayons.green('Aquarius Traits: Visit https://www.zodiacsign.com/')}")

        # CHECK IF USER INPUT MEETS PSICES CRITERIA


        elif ((30 > day > 18) and (date_of_birth[0] == "february")) or ((21 > day > 0) and (date_of_birth[0] == "march")):
            zodiac_sign = "Pisces"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")

            print(f"{crayons.green('Pisces Traits : Visit https://www.zodiacsign.com/' )}")

        # CHECK IF USER INPUT MEETS ARIES CRITERIA


        elif ((32 > day > 20) and (date_of_birth[0] == "march")) or ((20 > day > 0) and (date_of_birth[0] == "april")):

            zodiac_sign = "Aries"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")

            print(
                f"{crayons.green('Aries Traits : Visit https://www.zodiacsign.com/')}")

        # CHECK IF USER INPUT MEETS taurus CRITERIA


        elif ((31 > day > 19) and (date_of_birth[0] == "april")) or ((21 > day > 0) and (date_of_birth[0] == "may")):

            zodiac_sign = "Taurus"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")

            print(
                f"{crayons.green('Taurus Traits : Visit https://www.zodiacsign.com/')}")

         # CHECK IF USER INPUT MEETS Gemini CRITERIA

        elif ((32 > day > 20) and (date_of_birth[0] == "may")) or ((21 > day > 0) and (date_of_birth[0] == "june")):

            zodiac_sign = "Gemini"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(
                f"{crayons.green('Gemini Traits : Visit https://www.zodiacsign.com/')}")

        elif ((31 > day > 20) and (date_of_birth[0] == "june")) or ((23 > day > 0) and (date_of_birth[0] == "july")):

            zodiac_sign = "Cancer"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(
                f"{crayons.green('Cancer Traits : Visit https://www.zodiacsign.com/')}")
        # CHECK IF USER INPUT MEETS LEO CRITERIA

        elif ((32 > day > 22) and (date_of_birth[0] == "july")) or ((18 > day > 0) and (date_of_birth[0] == "august")):

            zodiac_sign = "Leo"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(
                f"{crayons.green('Leo Traits : Visit https://www.zodiacsign.com/')}")

        # CHECK IF USER INPUT MEETS VIRGO CRITERIA
        elif ((32 > day > 22) and (date_of_birth[0] == "august")) or ((23 > day > 0) and (date_of_birth[0] == "september")):
            zodiac_sign = "Virgo"

            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(
                f"{crayons.green('Virgo Traits : Visit https://www.zodiacsign.com/')}")

        # CHECK IF USER INPUT MEETS LIBRA CRITERIA
        elif ((31 > day > 22) and (date_of_birth[0] == "september")) or ((23 > day > 0) and (date_of_birth[0] == "october")):
            zodiac_sign = "Libra"

            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(
                f"{crayons.green('Libra Traits : Visit https://www.zodiacsign.com/')}")

        # CHECK IF USER INPUT MEETS SCORPIO CRITERIA
        elif ((32 > day > 22) and (date_of_birth[0] == "october")) or ((22 > day > 0) and (date_of_birth[0] == "november")):
            zodiac_sign = "Scorpio"

            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")
            print(
                f"{crayons.green('Scorpio Traits : Visit https://www.zodiacsign.com/')}")

        # CHECK IF USER INPUT MEETS SAGITTARIUS CRITERIA
        elif ((31 > day > 21) and (date_of_birth[0] == "november")) or ((22 > day > 0) and (date_of_birth[0] == "december")):
            zodiac_sign = "Saggitarius"

            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")

            print(
                f"{crayons.green('Sagittarius Traits : Visit https://www.zodiacsign.com/')}")


        # CHECK IF USER INPUT MEETS SAGITTARIUS CRITERIA
        elif ((32 > day > 21) and (date_of_birth[0] == "december")) or ((20 > day > 0) and (date_of_birth[0] == "january")):
            zodiac_sign = "Capricorn"
            print(f"Hello {user_name}, your zodiac sign is {zodiac_sign}.")

            print(
                f"{crayons.green('Capricorn Traits : Visit https://www.zodiacsign.com/')}")

        # Ensure user enters a valid date

        else:
            print("Enter a valid date: ")

        # Prompt user to exit or continue using the program    

        print(" ")

        print("Enter 1 to continue using Zodiac Predictor or 0 to exit: ")

        #Accept input from user as regards user choice

        new = input()

        # Turn user input to an intger and use the value to update exit varibale used in the while loop
        exit = int(new)

    print(f"Have a nice day {user_name}.")


if __name__ == "__main__":
    main()



