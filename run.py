import math
import time
import colorama
colorama.init()


# Declaring variables
border = """
-----------------------------------------------------------------
"""

# Getting user name by input
while True:
    name = str(input(colorama.Fore.GREEN + "What is your name? "))
    # Validate name length and characters
    if len(name) < 3 or not name.isalpha():
        print(colorama.Fore.RED + "Name can only be letters and\
  must be at least 3 letters long")
        continue
    # Break the loop if name is valid
    break
time.sleep(0.5)
print(colorama.Fore.WHITE + border)


def start():
    """ calculator start function"""


time.sleep(0.5)
print(colorama.Fore.BLUE + f"Dear {name}, welcome to crochet guage calculator")
time.sleep(0.5)
print(colorama.Fore.WHITE + border)
# printing border at the end of print statement.

print(f"You can use this app to calculate following:")

print(border)
time.sleep(0.5)
print("* This app will help you to calculate the Guage.")
time.sleep(0.5)
print("* Estimated rows and Stitches Per row.")
time.sleep(0.5)
print("* Estimated yarn and Estimated cost for your project.")
time.sleep(0.5)
print(border)
time.sleep(1)
print(colorama.Fore.BLUE + "you need to follow these steps:")
time.sleep(0.5)
print(colorama.Fore.WHITE + border)
time.sleep(0.5)
print(colorama.Fore.WHITE + "1:Make a swatch.")
time.sleep(0.5)
print("2:Count the number of rows of the swatch.")
time.sleep(0.5)
print("3:Count the number of stiches in the row.")
time.sleep(0.5)
print("4:Measure the width in inches.")
time.sleep(0.5)
print("5:measure the length in inches.")
time.sleep(0.5)
print("6:Weight the swatch to find out how many grams\
  of yarn is used for swatch")
print(border)
global swatch_length
while True:
    try:
        swatch_length = float(input(colorama.Fore.GREEN + "Enter the swatch length (in inches): "))
        # Valid input, break out of the loop
        break
    except ValueError:
        print(colorama.Fore.RED + "Invalid input Please enter a number.")


# getting user input for swatch width.
global swatch_width
while True:
    try:
        swatch_width = float(input(colorama.Fore.GREEN + "Enter the swatch width (in inches): "))
       # Valid input, break out of the loop
        break
    except ValueError:
        print(colorama.Fore.RED + "Invalid input Please enter a number.")

# getting user input for number of stitches per row in swatch.
global number_of_stitches
global number_of_rows
while True:
    try:
        number_of_stitches = int(input(colorama.Fore.GREEN + "Enter the number of stitches \
per row in the swatch: "))
   # Valid input, break out of the loop
        break
    except ValueError:
        print(colorama.Fore.RED + "Invalid input Please enter a number.")
# getting user input for number of rows in swatch.

while True:
    try:
        number_of_rows = int(input(colorama.Fore.GREEN + "Enter the number of rows in the swatch: "))
        # Valid input, break out of the loop
        break
    except ValueError:
        print(colorama.Fore.RED + "Invalid input Please enter a number.")
#taking user input for yarn weight used for swach and declaring it as global variable
global yarn_weight
while True:    
    try:
        yarn_weight = float(input(colorama.Fore.GREEN + "please enter yarn\
 weight in grams that is used in swatch: "))
        break
    except ValueError:
            print(colorama.Fore.RED + "Invalid input please enter a number") 


# Print instructions for project length and width after successful input of number of rows
print(colorama.Fore.WHITE + border)
print("please enter required project length and width\
 (length and width of the project that you want to make)")
print(border)    

global required_project_length

while True:
        try:
            required_project_length = float(input(colorama.Fore.GREEN + "Enter the project length (in inches): "))
            # Valid input, break out of the loop
            break
        except ValueError:
            print(colorama.Fore.RED + "Invalid input. Please enter a number.")
    
        print(colorama.Fore.WHITE + "Enter the required project width")
    # getting user input for required project width.
global required_project_width

while True:
        try:  
            required_project_width = float(input(colorama.Fore.GREEN + "Enter\
 the project width (in inches): "))
           # Valid input, break out of the loop
            break
        except ValueError:
            print(colorama.Fore.RED + "Invalid input. Please enter a number.")

global cost
    # getting user input for price of yarn per 100grams.
while True:
    try:
        # Noramlly a yarn ball weight 100grams        
        cost = float(input(colorama.Fore.GREEN + "Enter the price of yarn per 100grams: "))
        break
    except ValueError:
        print(colorama.Fore.RED + "please enter the price in numbers")
# calling start function.
start()

# printing statment to select options.
print(colorama.Fore.WHITE + border)
time.sleep(0.5)
print(colorama.Fore.WHITE + "Please enter from one of the following option: ")
time.sleep(0.5)
print(border)


# function calculate_guage
def calculate_gauge():
    """Function to calculate the guage for the project"""
  
    
    # Calculate stitches and rows per inch (using swatch data)
    # rounding the result as whole number us int data type.
    stitches_per_inch = math.ceil(number_of_stitches / swatch_width)
    rows_per_inch = math.ceil(number_of_rows / swatch_length)
    # printing border and print statment, border will\
    # be before and after the print statment.
    time.sleep(0.5)
    print(colorama.Fore.WHITE + border)
    time.sleep(1)
    print(colorama.Fore.BLUE + f"Dear {name}, your Guage on the base of the\
 swatch is {rows_per_inch} rows per inch\
 and {stitches_per_inch} stiches per inch.")
    time.sleep(0.5)
    print(colorama.Fore.WHITE + border)
    # printing sample_length statement
    time.sleep(0.5)
    print("Thank you for visiting")
    # function for clculating rows. and stiches for any size
    time.sleep(0.5)
    print(border)


def blanket_row_stitch_calculation():
    """Funtion to calculate Total Rows and Stitches per row\
    for the project according to input provided by user"""
    # Calculate stitches and rows per inch (using swatch data)\
    # and rounding up result as whole number.
    stitches_per_inch = float(number_of_stitches / swatch_width)
    rows_per_inch = float(number_of_rows / swatch_length)
    # Calculate total rows and stitches.
    total_rows_for_project = math.ceil(required_project_length * rows_per_inch)
    total_stitches_per_row = math.ceil(required_project_width * stitches_per_inch)
    # printing border and print statment for result
    # adding users name in the statment.
    time.sleep(0.5)
    print(colorama.Fore.WHITE + border)
    time.sleep(1)
    print(colorama.Fore.BLUE + f"dear {name}, you need\
 {total_rows_for_project} Rows and \
 {total_stitches_per_row} stiches per Row for this project.")
    time.sleep(0.5)
    print(colorama.Fore.WHITE + border)
    # printing Thank you statement.
    time.sleep(0.5)
    print("Thank you for visiting")
    time.sleep(0.5)
    print(border)
    # function to calculate the estimated yarn and cost for the project.


def project_cost():
    """function to calculate Estmated yarn and Estimated cost for the project/
     using the input provided by the user"""
    # getting user input for yarn used for swatch in grams.
  

    swatch_area = swatch_length * swatch_width
    # Calculate yarn used per inch
    yarn_per_inch = yarn_weight / swatch_area
    # calculating project_Area and estimated_yarn.
    project_Area = required_project_length*required_project_width
    estimated_yarn = project_Area*yarn_per_inch
    yarn_ball_in_grams = 100
    Total_balls_of_yarn = math.ceil(estimated_yarn/100)
    # printing boder and result statement using user name.
    time.sleep(0.5)
    # calculating project cost.
    project_cost = cost * Total_balls_of_yarn
    # printing border and the result statement using user name.
    time.sleep(0.5)
    print(colorama.Fore.WHITE + border)
    time.sleep(1)
    print(colorama.Fore.BLUE + f" Dear {name}, you need {Total_balls_of_yarn }\
 balls of yarn for the project and project cost will be ${project_cost} .")
    print(colorama.Fore.WHITE + border)
    # printing Thank you statement.
    time.sleep(0.5)
    print("Thank you for visiting")
    time.sleep(0.5)
    print(border)
    # function for main menu.
 


def menu():
    # printing options.
    time.sleep(0.5)
    print("[1] Enter 1 to calculate Project-Guage.")
    time.sleep(0.5)
    print("[2] Enter 2 to calculate Estimated Rows and\
    Stitches per Row for your Project.")
    time.sleep(0.5)
    print("[3] Enter 3 to calculate Estimated yarn and Cost for your project")
    time.sleep(0.5)
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