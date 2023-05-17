import sys
def multiply_number(input_number):
    multiplied = input_number * 2  # Perform the mathematical function
    return multiplied

# Check if an argument was provided
if len(sys.argv) < 2:
    print("Please provide an input number as an argument.")
    sys.exit(1)

# Get the input number from command-line argument
input_number = float(sys.argv[1])

# Call the function with the input number
result = multiply_number(input_number)

# Print the result
print(f"The multiplied value is: {result}")
