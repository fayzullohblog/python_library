
# 1
def sub(x):
    return x**2

print(list(map(sub,list(range(1,10)))))

# 2

def family(mather_age):
    
    return f'ota {mather_age}  yoshda buladi'
db =list(map(family,list(range(1,10))))
print(db)


# 3
print(list(map(lambda x: x*3,list(range(1,100)))))
