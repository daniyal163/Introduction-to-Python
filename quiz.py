scores = ["b","a","d","c"]
correct = ["b","a","c","d"]
for pos in range(len(scores)):
    if scores[pos]==correct[pos]:
        print(f"Score at position {pos} is correct")
    else:
        print(f"Score at position {pos} is incorrect")