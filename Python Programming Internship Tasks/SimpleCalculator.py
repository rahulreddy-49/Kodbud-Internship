n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))
print("Select the Operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=input("Enter choice(1/2/3/4):")
if choice=='1':
    print("Result:",n1+n2)
elif choice=='2':
    print("Result:",n1-n2)
elif choice=='3':
    print("Result:",n1*n2)
elif choice=='4':
    if n2!=0:
        print("Result:",n1/n2)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid input")