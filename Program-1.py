a=float(input("Enter a: "))
b=float(input("Enter b: "))
operation=input("Enter operation:")
if operation == "add":
    print("Result:",a+b)
elif operation=="sub":
    print("Result:",a-b)
elif operation=="mul":
    print("Result:",a*b)
elif operation=="div":
    if b==0:
        print("Error: Division by zero")
    else:
        print("Result:",a/b)
else:
    print("Invalid Operation")

