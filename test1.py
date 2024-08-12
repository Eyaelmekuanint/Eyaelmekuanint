x = (input("Enter an operator (+ - × /) : "))
a= float(input(" Enter the first number : "))
b=float(input("Enter the second number: "))

if x=="+" :
    s=a+b
elif x== "-":
    s=a-b
elif x== "*":
    s=a*b
elif x== "/":
    s=a/b
else:
    print("invalid operator ")
print(s)

