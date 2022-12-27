from collections import Counter

# 1
str_db='dsjdnqr cowcbacdscsdcjkeancbdc dljnscuncnlsdcnaducs'
db=Counter(str_db)
print(db)


# 2
print(db.most_common(2))

# 3
print(sorted(db))

# 4
print(db.values())

# 5
print(db.get('d'))

# 6
print(db.items())

# 7
print(db.keys())

# 8
print(db.update(db))

# 9
from collections import Counter
a = [[1920, 1939], [1911, 1944], [1920, 1955], [1938, 1939],[1936, 1940],[1935, 1940],[1935, 1940]]

# a=[ [1920,1939], [1911,1944],[1920,1955],[1938,1939]]
birth_1=[]

for i in range(0,len(a)):
    birth_iteam=a[i][1]-1
    birth_1.append(birth_iteam)

db=Counter(birth_1)
the_best_repeat=db.most_common(1)
db=list(the_best_repeat[0])[0]
print(db)




