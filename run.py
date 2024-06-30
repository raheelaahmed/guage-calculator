
print("welcome to crochet guage calculator")
# getting using name by input
name = input("What is your name? ")
print(f"Thank you, {name}, for using this app!\nThis app will help you calculate the number of stitches per inch.") 
print("you need to follow these steps to calculate the number of stiches per inch \n 1:Make a swatch\n 2:Count the number of rows\n 3:Count the number of stiches in the row")

length = float(input("Enter the length (in inches): ")) 
number_of_stitches = int(input("Enter the number of stitches: "))  

# Calculate stitches per inch
stitches_per_inch = number_of_stitches/length 

# Print the result 
print("Number of stitches per inch:", stitches_per_inch)
