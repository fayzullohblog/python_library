from collections import namedtuple

# using from namedtuple(): there are three differnt ways
#1: access by index:
#2: access by keys:
#3: access by getattr() 

# these are some exampling following:


# 1: access by index:

from collections import namedtuple

Student=namedtuple('Student',['name','age','birth_year'])
db=Student('fayzulloh',23,2000)
print(db[1])    


# 2: access by key:

Student=namedtuple('Student',['name','age','birth_year'])
db=Student('fayzulloh',23,2000)
print(db.name)


# 3: access by getattr()

Student=namedtuple('Student',['name','age','birth_year'])
db=Student('fayzulloh',23,2000)
print(getattr(db,'birth_year'))


