def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"
try:
    #  User input lena
    print("Faiz Calculator Running...\n")
    print("Select operation:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

    choice : int = input("Enter choice (1/2/3/4): ")
    a : float = float(input("Enter first number: "))
    b : float = float(input("Enter second number: "))

    #  Condition check karna
    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    else:
        print("Invalid input! Please enter 1, 2, 3 or 4.")
except ValueError:
    print("Invalid input! Please enter numeric values for numbers.")

print("Calculator has been closed.")
print("Thank you for using Faiz Calculator!")