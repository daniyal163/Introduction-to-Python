with open("text.txt", encoding="utf-8") as f:
    text = f.read().lower()

for p in ".,!?":
    text = text.replace(p, "")

words = text.split()
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

with open("report.text", "w", encoding="utf-8") as out:
    out.write(f"words: {len(words)}\n")
    out.write(f"unique: {len(counts)}\n")
    for w in sorted(counts):
        out.write(f"{w:>10} : {counts[w]}\n")

print("report saved")