# 1
def squery(a):
    if a>3:
        return True
    else:
        return False

db=list(filter(squery,[1,2,3,4,5]))
print(db)

# 2
db=list(filter(lambda x: x%2==0 and x%3==0, list(range(1,100))))
print(db)


