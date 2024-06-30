
print("welcome to crochet guage calculator")

length = float(input("Enter the length (in inches): "))  # Get length as float
number_of_stitches = int(input("Enter the number of stitches: "))  # Get stitches as integer

# Calculate stitches per inch
stitches_per_inch = number_of_stitches/length 

# Print the result with proper formatting
print("Number of stitches per inch:", stitches_per_inch)
