from itertools import cycle,islice
# 1
student=['fayzulloh','jasur','azizbek','xurshid']
cycles=cycle(student)
db=islice(cycles,0,student)
print(list(db))



