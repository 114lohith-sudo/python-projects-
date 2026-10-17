num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))
op=str(input("Enter your opparation: ")) 
if op == "Add" or op == "+":
    result=num1+num2
    print("Result of addition:" + str(result)) 
elif op == "Subtract" or op == "-":
    result=num1-num2
    print("Result of subtraction:" + str(result))
elif op == "Multiply" or op == "Multiplication" or op == "*":
    result=num1*num2
    print("Result of multiplication:" + str(result))
elif op == "Divide" or op == "/":
    result=num1/num2
    print("Result of division:" + str(result)) 
elif op == "Exponent" or op == "**":
    result=num1**num2
    print("Result of Exponent:" + str(result))
elif op == "Modulus" or op == "%":
    result=num1%num2
    print("Result of modulus:" + str(result))