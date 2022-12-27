from functools import reduce

# 1

def age(a,b):
    return a*b

db=reduce(age,list(range(1,4)))

print(db)


# 2

db=reduce(lambda x,y:x**y,list(range(1,6)))
print(db)