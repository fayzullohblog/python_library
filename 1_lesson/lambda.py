# 1
add_to=lambda x,y,z: x+y+z
print(add_to(2,3,4))

# 2
db=lambda i:i**3
for i in range(1,10):
    print(db(i))


# 3
db=lambda x,a=3,b=2,c=1:a*x*x+b*x+c
print(db(4))

# 4
db=lambda x,y:lambda z: (x+y)*z
print(db(3,10)(100))

# 5
db=lambda father_age,mather_age:lambda father_name,mather_name: f'{father_name} aka xotini {mather_name} opadan {father_age-mather_age} yoshga katta'
print(db(38,30)('Fayzulloh','matluba'))