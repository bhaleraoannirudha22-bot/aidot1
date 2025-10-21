def add(a, b):
    """This function adds two numbers"""
    return a + b

if __name__ == "__main__":
    try:
        num1_str = input("Enter the first number: ")
        num1 = float(num1_str)
        num2_str = input("Enter the second number: ")
        num2 = float(num2_str)
        result = add(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
