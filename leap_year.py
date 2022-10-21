# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/21
# Takes the user input for a year and tells
# The user whether it is a leap year using
# Nested boolean expressions.


def main():

    # Title
    print("leap Years")

    # User inputs for the year
    year_input = input("Enter a year: ")

    # Try Catch statement to make sure the input is an integer
    try:
        year_integer = int(year_input)

    # Exception which tells the user to enter an integer
    except Exception:
        print("Please enter an integer! (ex: 2000)")

    else:
        # IF statement for if the year is divisible by 4
        if year_integer % 4 == 0:
            # Nested if statement if the year is divisible by 100
            if year_integer % 100 == 0:
                # If it is divisible by 100 it is not a leap year unless it
                # Is also divisible by 400
                if year_integer % 400:
                    print("{} Is a leap year!".format(year_integer))
                else:
                    print("{} Is not a leap year :(".format(year_integer))
            else:
                print("{} Is a leap year!".format(year_integer))
        else:
            print("{} is not a leap yer :(".format(year_input))


if __name__ == "__main__":
    main()
