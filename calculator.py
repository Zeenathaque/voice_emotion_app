def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def calculator():
    print("Welcome to Command Line Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'



            
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'

        print(f"{num1} {operation} {num2} = {result}")

        next_calc = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calc != 'yes':
            print("Goodbye!")
            break

# Run the calculator
if __name__ == "__main__":
    calculator()
