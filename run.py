#Declaring variables


#tag line in form of. ascci art
tagline =  """
_  __                  ____      _                             _ 
| |/ /___  ___ _ __    / ___|__ _| |_ __ ___     __ _ _ __   __| |
| ' // _ \/ _ \ '_ \  | |   / _` | | '_ ` _ \   / _` | '_ \ / _` |
| . \  __/  __/ |_) | | |__| (_| | | | | | | | | (_| | | | | (_| |
|_|\_\___|\___| .__/  _\____\__,_|_|_| |_|_|_|  \__,_|_| |_|\__,_|
 / ___|_ __ __|_| ___| |__   ___| |_   / _ \ _ __                 
| |   | '__/ _ \ / __| '_ \ / _ \ __| | | | | '_ \                
| |___| | | (_) | (__| | | |  __/ |_  | |_| | | | |               
 \____|_|  \___/ \___|_| |_|\___|\__|  \___/|_| |_|"""

#boder
border = """
^^^^^^*******^^^^^^*******^^^^^^*******^^^^^*******
"""
# getting using name by input
name = input("What is your name? ")
def start():
    """ calculator start function"""

print(f"Dear {name} welcome to crochet guage calculator")
# getting using name by input

#print tagline
print (tagline)


print(border)

print(f"Thank you, {name}, for using this app!\nThis app will help you to calculate the Guage,  Estimated rows and Stiches Per row, Estimated yarn and Estimated cost for your project.") 

print(border)
print("you need to follow these steps: \n 1:Make a swatch\n 2:Count the number of rows\n 3:Count the number of stiches in the row \n 4:Measure the width in inches\n 5:measure the length in inches")
start()



 

def calculate_gauge():
   # """Calculates the gauge (stitches and rows per inch) based on a swatch."""
        swatch_length =float(input("Enter the swatch length (in inches): "))
        swatch_width = float(input("Enter the swatch width (in inches): "))
        number_of_stitches = int(input("Enter the number of stitches in the swatch: "))
        number_of_rows = int(input("Enter the number of rows in the swatch: "))

        # Calculate stitches and rows per inch (using swatch data)
        stitches_per_inch = number_of_stitches / swatch_width
        rows_per_inch = number_of_rows / swatch_length

        # Print results with clear labels
       # print("Number of stitches per inch:", stitches_per_inch)
       # print("Number of rows per inch:", rows_per_inch)
        print(border)
      
        print(f"Dear {name}, you Guage on the base of your swatch is {rows_per_inch} rows per inch and {stitches_per_inch} stiches per inch ")

        print(border)
       


# function for clculating rows. and stiches for any size
def blanket_row_stitch_calculation():


        # Get user input (assuming inches)
      
        number_of_stitches = int(input("Enter the number of stitches in a swatch: "))
        number_of_rows = int(input("Enter the number of rows in a swatch: "))
        length = int(input("Enter the swatch length: "))
        width = int(input("Enter your swatch width: "))
        # Calculate stitches and rows per inch (using swatch data)
        stitches_per_inch = number_of_stitches / width
        rows_per_inch = number_of_rows / length


        # Get user input for project dimensions
        print("Enter the required project length")
        required_project_length = float(input("Enter the project length (in inches): "))
        print("Enter the required project width")
        required_project_width = float(input("Enter the project width (in inches): "))

        # Calculate total rows and stitches (assuming rows_per_inch and stitches_per_inch are known)
        total_rows_for_project = required_project_length * rows_per_inch
        total_stitches_per_row = required_project_width * stitches_per_inch
        print(border)
       
        print(border)
        print(f"dear {name} you need {total_rows_for_project:.2f} Rows and {total_stitches_per_row:.2f} stiches per Row for this project")
        print(border)
    






def project_cost():
        swatch_length = float(input("Enter the swatch length (in inches): "))
        swatch_width = float(input("Enter the swatch width (in inches): "))
        yarn_weight = float(input("Enter the yarn weight used for the swatch (in grams): "))

        # Calculate swatch area (assuming rectangular swatch)
        swatch_area = swatch_length * swatch_width

        # Calculate yarn used per inch (assuming yarn is evenly distributed)
        yarn_per_inch = yarn_weight / swatch_area

        print(f"Yarn used per inch: {yarn_per_inch:.2f} grams")  # Format to 2 decimal places

        project_length=int(input("Enter project length in inches: "))
        project_width=int(input("Enter project width in inches: "))
        project_Area=  project_length*project_width
        estimated_yarn= project_Area*yarn_per_inch
        print(border)
        print(f" Dear {name} you need {estimated_yarn} grams yarn for the project.")
        print(border)

        cost=float(input("Enter the price per 100grams: "))

        project_cost=cost* estimated_yarn/100
        print(border)
        print(f" Dear {name} your project cost will be ${project_cost}")
        print(border)
       
       



def menu():
    print("[1] Enter 1 to calculate Project-Guage.")
    print("[2] Enter 2 to calculate Estimated Rows and Stitches per Row. for your Project.")
    print("[3] Enter 3. to calculate Estimated yarn and Cost for your project")
    print("[0] Exit the program")

    option = int(input("Enter your option here: "))
    return option

while True:
    option = menu()
    if option == 1:
         calculate_gauge()
         break
    elif option == 2:
        blanket_row_stitch_calculation()
        break
    elif option == 3:
     project_cost()
     break
    else:
        print("Invalid option")

