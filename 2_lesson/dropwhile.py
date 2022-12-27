from itertools import dropwhile

print(list(dropwhile(lambda x: x<10,list(range(1,20)))))