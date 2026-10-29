a= float(input("Enter the first number: "))
b= float(input("Enter the second number: "))
op= input("Operator(+,-,/,*)")
op == "^"
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)          
elif op=='*':
    print(a*b)
elif op=='/':
    if b==0:
        print("Division by zero is not allowed")
    else:
        print(a/b)  
else:
    print("Invalid operator")