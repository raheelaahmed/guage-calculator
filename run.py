import math
# Declaring variables
border = """
^^^^^^*******^^^^^^*******^^^^^^*******^^^^^*******
"""

# Getting user name by input
name = input("What is your name? ")


def start():
    """ calculator start function"""


print(f"Dear {name} welcome to crochet guage calculator")
# printing border at the end of print statement.
print(f"Thank you, {name}, for using this app!")
print("This app will help you to calculate the Guage.")
print("Estimated rows and Stitches Per row.")
print("Estimated yarn and Estimated cost for your project.")

print(border)
print("you need to follow these steps:")
print("1:Make a swatch.")
print("2:Count the number of rows.")
print("3:Count the number of stiches in the row.")
print("4:Measure the width in inches.")
print("5:measure the length in inches.")
print(border)
global swatch_length
swatch_length = float(input("Enter the swatch length (in inches): "))
# getting user input for swatch width.
global swatch_width
swatch_width = float(input("Enter the swatch width (in inches): "))

# getting user input for number of stitches per row in swatch.
global number_of_stitches
global number_of_rows
number_of_stitches = int(input("Enter the number of stitches\
per row in the swatch: "))
# getting user input for number of rows in swatch.
number_of_rows = int(input("Enter the number of rows in the swatch: "))


# calling start function.
start()

print(border)
print(border)

# printing statment to select options.
print("Please enter from one of the following option: ")


# function calculate_guage
def calculate_gauge():
    # """Calculates the gauge (stitches and rows per inch)
    # based on a swatch."""
    # Calculate stitches and rows per inch (using swatch data)
    # rounding the result as whole number us int data type.
    stitches_per_inch = int(number_of_stitches / swatch_width)
    rows_per_inch = int(number_of_rows / swatch_length)
    # printing border and print statment, border will\
    # be before and after the print statment.
    print(border)
    print(f"Dear {name}, you Guage on the base of your swatch \
    is {rows_per_inch}rows per inch and {stitches_per_inch} stiches per inch ")
    print(border)
    # printing Thankyou statement
    print("Thankyou for visiting")
    # function for clculating rows. and stiches for any size


def blanket_row_stitch_calculation():
    # Calculate stitches and rows per inch (using swatch data)\
    #  and rounding up result as whole number.
    stitches_per_inch = int(number_of_stitches / swatch_width)
    rows_per_inch = int(number_of_rows / swatch_length)
    # Get user input for project dimensions
    print("Enter the required project length")
    # getting user input for the required project length.
    required_project_length = float(input("Enter the project\
    length (in inches): "))
    print("Enter the required project width")
    # getting user input for required project width.
    required_project_width = float(input("Enter the project\
    width (in inches): "))
    # Calculate total rows and stitches.
    total_rows_for_project = int(required_project_length * rows_per_inch)
    total_stitches_per_row = int(required_project_width * stitches_per_inch)
    # printing border and print statment for result
    # adding users name in the statment.
    print(border)
    print(f"dear {name} you need {total_rows_for_project} Rows and\
    {total_stitches_per_row} stiches per Row for this project")
    print(border)
    # printing Thankyou statement.
    print("Thankyou for visiting")
    # function to calculate the estimated yarn and cost for the project.


def project_cost():
    # getting user input for yarn used for swatch in grams.
    yarn_weight = float(input("Enter the yarn weight used\
    for the swatch (in grams): "))

    # Calculate swatch area
    swatch_area = swatch_length * swatch_width
    # Calculate yarn used per inch
    yarn_per_inch = yarn_weight / swatch_area
    # getting the user input for required project length.
    project_length = int(input("Enter project length in inches: "))
    # getting user input for required project width.
    project_width = int(input("Enter project width in inches: "))
    # calculating project_Area and estimated_yarn.
    project_Area = project_length*project_width
    estimated_yarn = project_Area*yarn_per_inch
    yarn_ball_in_grams = 100
    Total_balls_of_yarn = math.ceil(estimated_yarn/100)
    # printing boder and result statement using user name.
    print(border)
    print(f" Dear {name} you need {Total_balls_of_yarn } \
    balls of yarn for the project.")
    print(border)
    # getting user input for price of yarn per 100grams.
    cost = float(input("Enter the price per 100grams: "))
    # calculating project cost.
    project_cost = cost * Total_balls_of_yarn
    # printing border and the result statement using user name.
    print(border)
    print(f" Dear {name} your project cost will be ${project_cost}")
    print(border)
    # printing Thankyou statement.
    print("Thankyou for visiting")
    # function for main menu.


def menu():
    # printing options.
    print("[1] Enter 1 to calculate Project-Guage.")
    print("[2] Enter 2 to calculate Estimated Rows and \
    Stitches per Row. for your Project.")
    print("[3] Enter 3. to calculate Estimated yarn and Cost for your project")
    print("[0] Exit the program")
    # getting user input  for options.
    option = int(input("Enter your option here: "))
    return option
    # using while loop, if user enter correct option it will start
    # calling functions accoring to user choosen option.


while True:
    option = menu()
    if option == 1:
        # if user choose option 1 calling function calculate_gauge().
        calculate_gauge()

    elif option == 2:
        # if user choose option 2 calling function\
        # blanket_row_stitch_calculation().
        blanket_row_stitch_calculation()

    elif option == 3:

        # if user choose option 3 calling function project_cost().
        project_cost()

    elif option == 0:
        print("Exiting the program.")
        # if user choose option 0  Exit the loop.
        break

    else:
        # printing invalid statment
        print("Invalid option")
