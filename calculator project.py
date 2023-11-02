# Simple Calculator Project

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

# Main function
def main():
    print("Simple Calculator")
    
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'sub' for subtraction")
        print("Enter 'mul' for multiplication")
        print("Enter 'div' for division")
        print("Enter 'quit' to end the program")
        
        user_input = input(": ")
        
        if user_input == "quit":
            break
        
        if user_input in ["add", "sub", "mul", "div"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if user_input == "add":
                result = add(num1, num2)
            elif user_input == "sub":
                result = subtract(num1, num2)
            elif user_input == "mul":
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)
            
            print("Result: " + str(result))
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
