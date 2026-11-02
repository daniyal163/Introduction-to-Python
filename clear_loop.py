lines = ["the cat i black ", "the is browmn"]
words = []
for line in lines:
    for word in line.split():
        if len(word) > 2 and word != "the":
            words.append(word.upper())
print(words)

price = [12,15,133,99, 134, 242]
with_tax = [round(p*1.2,2)for p in price if p>100]
print(with_tax)

def grades(path):
    grade = {}
    with open(path , encoding = "utf-8") as f:
        for line in f:
            name, g = line.split()
            grade[name] = int(g)
    return grade
    