#튜플은 read only
target = ('영어999', '코딩마스터', 'ceo')
print(target[0])

#읽기 전용
#target[0] = '일본어 만점'
#print(target)

target2 = list(target)
print(target2)
print(type(target2))
print('마지막값>', target2[-1])
target2[0] = '일본어만점'
print(target2)
target = tuple(target2)
print(target)

next = ('여행', '또여행')
print(next + target)

next0, next1 = next
print(next0)
print(next1)