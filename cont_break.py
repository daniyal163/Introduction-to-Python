temps = {12,-999,15,-999}
for t in temps:
    if t==-999:
        continue
    print(t)
for n in range(100,200):
    if n%7==0:
        print("First multiple of 7 between 100 and 200 is : ",n)
        break
    print(n)