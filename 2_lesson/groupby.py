from itertools import groupby

# 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

grouped = groupby(numbers, key=lambda x: x < 3) 

print(grouped)

for k,v in grouped:
    print(k,list(v))




# 2

def sub(x):
    if x>10:
        return True
    else:
        return False

db=groupby(list(range(1,15)),key=sub)
tool=[]
for k,v in db:
    tool.append(v)
    print(k,list(v))

