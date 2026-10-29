counts = {}
with open("text.txt",encoding = "utf-8") as f:
     for line in f:
         line = line.lower()
         for p in ".,!?":
             line = line.replace(p,"")
         for word in line.split():
             counts[word]= counts.get(word,0)+1
for word, n in counts.items():
    print(f"{word:<10}{n}")