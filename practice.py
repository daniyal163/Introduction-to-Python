#Comprehension in list and dictionries
list = [i*i for i in range(1,11) if i%2==0]
print(list)

names = ["Ana","Benjamin","Chloe"]
length = {name :len(name) for name in names}
print(length)
letters = [name for name in names if len(name)>3]
print(letters)