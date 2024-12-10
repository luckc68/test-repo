# app.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Division by zero is not allowed."

def main():
    print("Welcome to the Python CLI Calculator!")
    print("Select an operation: +, -, *, /")
    operation = input("Enter operation: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == '+':
        print(f"Result: {add(a, b)}")
    elif operation == '-':
        print(f"Result: {subtract(a, b)}")
    elif operation == '*':
        print(f"Result: {multiply(a, b)}")
    elif operation == '/':
        print(f"Result: {divide(a, b)}")
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()
