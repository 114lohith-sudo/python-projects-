def area(side):
    formula = side * side
    return formula

number = float(input("Enter a side:"))
result = area(number)
print("Area of square is " + str(result))

def rectangle(line1,line2):
    form = line1 * line2
    return form

rectLine1 = float(input("Enter first side for rectangle: "))
rectLine2 = float(input("Enter second side for rectange: "))
rectResult = rectangle(rectLine1,rectLine2)
print("Area of rectangle is " + str(rectResult))

def peri(side):
    equation = side * 4
    return equation

periNumber = float(input("Enter a side: "))
periResult = peri(periNumber)
print("Perimeter of square is " + str(periResult))