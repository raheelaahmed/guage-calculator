
print("welcome to crochet guage calculator")
# getting using name by input
name = input("What is your name? ")
print(f"Thank you, {name}, for using this app!\nThis app will help you calculate the number of stitches per inch.")

length = float(input("Enter the length (in inches): "))  # Get length as float
number_of_stitches = int(input("Enter the number of stitches: "))  # Get stitches as integer

# Calculate stitches per inch
stitches_per_inch = number_of_stitches/length 

# Print the result with proper formatting
print("Number of stitches per inch:", stitches_per_inch)
