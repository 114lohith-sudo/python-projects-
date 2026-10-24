
while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    print("6. Modulus")
    print("7. Exit")

    op = input("Enter your choice (1-7): ")

    if op == "1":
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        result = num1 + num2
        print("Result of addition:", result)

    elif op == "2":
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        result = num1 - num2
        print("Result of subtraction:", result)

    elif op == "3":
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        result = num1 * num2
        print("Result of multiplication:", result)

    elif op == "4":
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result of division:", result)

    elif op == "5":
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        result = num1 ** num2
        print("Result of exponent:", result)

    elif op == "6":
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        if num2 == 0:
            print("Error: Cannot use modulus with zero.")
        else:
            result = num1 % num2
            print("Result of modulus:", result)

    elif op == "7":
        print("Calculator closed.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")