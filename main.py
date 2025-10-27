# Define a function to add two numbers
def add(a, b):
    """This function adds two numbers"""
    return a + b

# This block of code will only run when the script is executed directly
if __name__ == "__main__":
    try:
        # Get the first number from the user
        num1_str = input("Enter the first number: ")
        # Convert the input string to a float
        num1 = float(num1_str)
        # Get the second number from the user
        num2_str = input("Enter the second number: ")
        # Convert the input string to a float
        num2 = float(num2_str)
        # Call the add function with the two numbers
        result = add(num1, num2)
        # Print the result
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        # Handle the case where the user enters a non-numeric value
        print("Invalid input. Please enter valid numbers.")