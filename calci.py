print(" SIMPLE CALCULATOR")
operator=input("Enter the operator:")
a=float(input("Enter the first num:"))
b=float(input("Enter the second num:"))
if operator=="+":
    print("The addition of a and b is: ",a+b)
elif operator=="-":
    print("The subtarction of a and b is: ",a-b)
elif operator=="*":
    print("The muliplication of a  and b is: ",a*b)
elif operator=="/":
    print("The division of a and  b is: ",a/b)
elif operator=="%":
    print("The modulus of a and b is: ",a%b)
elif operator=="//":
    print("The integer division of a and b is: ",int(a//b))
else:
    print("The operator is invalid")