from itertools import count

db=count(10,100)
print(next(db))  # 10
print(next(db))  # 110
print(next(db))  # 210
