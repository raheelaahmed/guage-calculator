
print("welcome to crochet guage calculator")
# getting using name by input
name = input("What is your name? ")

#i want to give three options here 1:calulate the guage forany project 2:calculate the number of stiches and rows for blankets from given sizes \n 3:calculate the rquired number of stiches and rows.  for your desired lenth and wdth. of the project


print("--------------------------------------------------------------------------------------------")

print("--------------------------------------------------------------------------------------------")

print("--------------------------------------------------------------------------------------------")
print(f"Thank you, {name}, for using this app!\nThis app will help you calculate the number of stitches per inch.") 
print("you need to follow these steps to calculate the number of stiches per inch \n 1:Make a swatch\n 2:Count the number of rows\n 3:Count the number of stiches in the row \n 4:Measure the width in inches\n 5:measure the length in inches")
def calculate_gauge():
#getting length by user input

    length = float(input("Enter the length (in inches): "))
#getting width by user input
width=float(input("Enter the width (in inches): ")) 
#getting the number of stiches by user input
number_of_stitches = int(input("Enter the number of stitches: ")) 
#getting the number of rows by user input
number_of_rows = int(input("Enter the number of rows: ")) 


# Calculate stitches per inch
stitches_per_inch = number_of_stitches/width

#Calculate the number of rows per inch

rows_per_inch = number_of_rows/ length

# Print the result 
print("Number of stitches per inch:", stitches_per_inch)
print("Number of stitches per inch:", rows_per_inch)


blanket_length=float(input("enter blanket  length"))
blanket_width=float(input("enter blanket width"))
#calculation rows for project
Rows=blanket_length*rows_per_inch
#caculation for stiches per row:
stiches=blanket_width*stitches_per_inch
print("number of rows:", Rows)
print("number of stichess:", stiches)
