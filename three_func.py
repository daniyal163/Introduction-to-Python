def max_value(val):
    best =val[0]
    for v in val:
        if v>best:
            best = v
        return best
def count_occ(val,item):
    count=0
    for i in val:
        if i ==item:
            count+=1
    return count
def filter_val(val,min):
    return{k: v for k, v in val.items()if v>=min}
print(filter_val({"anc": 4 , "cup":4 ,"plate": 3}, 4))