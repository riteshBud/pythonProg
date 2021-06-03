def Calculater():
    operation = input("Enter Arthmetic Operation name: ")
    x = input("Enter First Number ")
    y = input('Enter Second Number ')

    sum = float(x) + float(y)   
    multiply = float(x) * float(y)
    divide = float(x) / float(y)
    substarct = float(x) - float(y)
    if operation == "Sum":
        print("Sum :",sum)
    elif operation == "Multiply":
        print("Product :",multiply)
    elif operation == "Substract":
        print("Difference :",substarct)
    elif operation == "Divide":
        print("Quotient :",divide)

Calculater()
