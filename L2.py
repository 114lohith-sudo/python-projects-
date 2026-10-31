def area(side):
    formula = side * side
    return formula

def rectangle(line1, line2):
    form = line1 * line2
    return form

def peri(side):
    equation = side * 4
    return equation

def rectPeri(line1, line2):
    equation = 2 * (line1 + line2)
    return equation


while True:
    print("\nChoose an operation:")
    print("1. Area of square")
    print("2. Area of rectangle")
    print("3. Perimeter of square")
    print("4. Perimeter of rectangle")
    print("5. Exit")

    op = input("Enter your choice (1-5): ")

    if op == "1":
        number = float(input("Enter a side: "))
        result = area(number)
        print("Area of square is " + str(result))

    elif op == "2":
        rectLine1 = float(input("Enter first side for rectangle: "))
        rectLine2 = float(input("Enter second side for rectangle: "))
        rectResult = rectangle(rectLine1, rectLine2)
        print("Area of rectangle is " + str(rectResult))

    elif op == "3":
        periNumber = float(input("Enter a side: "))
        periResult = peri(periNumber)
        print("Perimeter of square is " + str(periResult))

    elif op == "4":
        rectLine1 = float(input("Enter first side for rectangle: "))
        rectLine2 = float(input("Enter second side for rectangle: "))
        rectPeriResult = rectPeri(rectLine1, rectLine2)
        print("Perimeter of rectangle is " + str(rectPeriResult))

    elif op == "5":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Enter a number from 1 to 5.")