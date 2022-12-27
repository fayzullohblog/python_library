from collections import defaultdict


# 1

def default_value():
    return 'bizda xali qolgan mashina yeli anniqlanmagan'

db=defaultdict(default_value)
for i in range(2010,2022):
    db[i]=i
print(db[2019])
print(db[334])
    
# 2
db =defaultdict(lambda: 'bizda ism va yoshi bor faqat')
db['age']=22
db['name']='fayziulloh'

print(db['age'])
print(db['last name'])

