def start():
    """ calculator start function"""

print("welcome to crochet guage calculator")
# getting using name by input
name = input("What is your name? ")

#i want to give three options here 1:calulate the guage forany project 2:calculate the number of stiches and rows for blankets from given sizes \n 3:calculate the rquired number of stiches and rows.  for your desired lenth and wdth. of the project

#tag line in form of. ascci art




tagline = """
_  __                  ____      _                             _ 
| |/ /___  ___ _ __    / ___|__ _| |_ __ ___     __ _ _ __   __| |
| ' // _ \/ _ \ '_ \  | |   / _` | | '_ ` _ \   / _` | '_ \ / _` |
| . \  __/  __/ |_) | | |__| (_| | | | | | | | | (_| | | | | (_| |
|_|\_\___|\___| .__/  _\____\__,_|_|_| |_|_|_|  \__,_|_| |_|\__,_|
 / ___|_ __ __|_| ___| |__   ___| |_   / _ \ _ __                 
| |   | '__/ _ \ / __| '_ \ / _ \ __| | | | | '_ \                
| |___| | | (_) | (__| | | |  __/ |_  | |_| | | | |               
 \____|_|  \___/ \___|_| |_|\___|\__|  \___/|_| |_|               """

#print tagline
print (tagline)


print("--------------------------------------------------------------------------------------------")

print("--------------------------------------------------------------------------------------------")

print("--------------------------------------------------------------------------------------------")
print(f"Thank you, {name}, for using this app!\nThis app will help you calculate the number of stitches per inch.") 
print("you need to follow these steps to calculate the number of stiches per inch \n 1:Make a swatch\n 2:Count the number of rows\n 3:Count the number of stiches in the row \n 4:Measure the width in inches\n 5:measure the length in inches")
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
        print("Number of stitches per inch:", stitches_per_inch)
        print("Number of rows per inch:", rows_per_inch)



# Call the function to start the calculation
calculate_gauge()
# function for clculating rows. and stiches for any size
def blanket_row_stitch_calculation():
# """Calculates the number of rows and stitches per inch for a blanket."""

        # Get user input (assuming inches)
        length = float(input("Enter the blanket length (in inches): "))
        width = float(input("Enter the blanket width (in inches): "))
        number_of_stitches = int(input("Enter the number of stitches in a swatch: "))
        number_of_rows = int(input("Enter the number of rows in a swatch: "))

        # Calculate stitches and rows per inch (using swatch data)
        stitches_per_inch = number_of_stitches / width
        rows_per_inch = number_of_rows / length

        # Print results with clear labels
        print("Number of stitches per inch:", stitches_per_inch)
        print("Number of rows per inch:", rows_per_inch)



# Call the function to start the calculation
blanket_row_stitch_calculation()