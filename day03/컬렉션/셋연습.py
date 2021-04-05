#중복 제거
#순서가 없음
friends = ['영수', '철수', '철수', '영진', '영수', '길동']
print(friends)
print(len(friends))

friends_set = set(friends)
print(friends_set)
print(len(friends_set))

friends_set.add('아이유')
print(friends_set)

friends_set.update({'재석', '용만'})
print(friends_set)

friends_set.clear()
print(friends_set)

term1 = {10, 20, 30, 40}
term2 = {11, 22, 33, 10}
result1 = term1 & term2
result1 = term1.intersection(term2)
print(result1)

result2 = term1 | term2
result2 = term1.union(term2)
print(result2)

result3 = term1 - term2
result3 = term1.difference(term2)
print(result3)
