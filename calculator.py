print("This a simple calculator program.")

def calculater():
    print("Enter the values :")
    x = float(input())
    y = float(input())
    print("Choose arithmatic operation.")
    print("1. Sum, 2. Multiply, 3. Substract, 4. Divide")
    z = int(input())
    print("the result is: ")
    
    if z == 1:
        print(x+y)
    elif z == 2:
        print(x*y)
    elif z == 3:
        print(x-y)
    elif z == 4:
        print(x/y)

calculater()
