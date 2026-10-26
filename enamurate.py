scores = [12,17,9,15,14]
best = -1
best_pos = 0
for pos in range(len(scores)):
    if scores[pos]>best:
        best = scores[pos]
        best_pos = pos
print(f"Best score is {best} at position {best_pos}")



