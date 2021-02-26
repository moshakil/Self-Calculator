try:
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator: ")
    num2 = float(input("Enter the second number: "))

    if op == "+":
        print(num1+num2)
    elif op == "-":
        print(num1-num2)
    elif op == "*":
        print(num1*num2)
    elif op == "/":
        print(num1/num2)
    else:
        print("\n-------- Sorry! Invalid Operators.\n")
except ValueError:
    print("\n  Invalid Input You Fool! It's a Calculator not Notebook.\n")

