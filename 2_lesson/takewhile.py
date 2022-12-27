from itertools import takewhile

print(list(takewhile(lambda x: x<10,list(range(1,20)))))
