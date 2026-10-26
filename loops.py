total = 0
n= int(input("Enter 1: ForLoop 2: WhileLoop "))
num = int(input("Enter the number until which you want to sum:"))
if n==1:
    for i in range(1,num+1):
        total += i
    print(f"Total for the {num} is : {total} with ForLoop")
elif n==2:
    i=1
    while i<5:
        total += i
        i+=1
    print(f"Total for the {num} is {total} with while Loop")