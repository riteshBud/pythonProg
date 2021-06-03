def Calculater():
    operation = input("Enter Arthmetic Operation name: ")
    x = input("Enter First Number ")
    y = input('Enter Second Number ')

    sum = float(x) + float(y)   
    multiply = float(x) * float(y)
    divide = float(x) / float(y)
    substarct = float(x) - float(y)
    if operation == "+":
        print("Sum :",sum)
    elif operation == "*":
        print("Product :",multiply)
    elif operation == "-":
        print("Difference :",substarct)
    elif operation == "/":
        print("Quotient :",divide)

Calculater()
