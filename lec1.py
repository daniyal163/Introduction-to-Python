#type conversiton
print (int("43")+23)
print (bool(0),bool(5))
print (bool(" "),bool("hi"))
print(str(100)+" points")
print(float(3.14)*2)
print(int(3.14))
x=5.6
print (type(x))

print (int("5")+3)

print("5"+str(3))

print(type(10/2))

# 9,4.0,77,14,flaot

quantity ="9"
unit_price = "4.0"
total = int(quantity) * float(unit_price) + 1 - 1
print("total:", total)

#input function
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name)    
print("Next year you will be:",age+1)
print(f"my name is {name}and i am {age} years old")
#f-strings
name = "John"
age = 30
print(f"my name is {name}and i am {age} years old")

print(f"my name is {{name}}")

price = 9.99
quantity = 345678
print(f"total price: {price*quantity:.2f}")
print(f"quantity: {quantity:,.3f}")
print(f"quantity: {price:.1%}")