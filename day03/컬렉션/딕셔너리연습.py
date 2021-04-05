점수목록 = {'철수':90, '민수':85, '영희':80}
print(점수목록)

print(점수목록['철수'])
점수목록['민수'] = 70
print(점수목록)

del 점수목록['철수']
print(점수목록)

####################
과목점수 = dict()
최종점수 = {}

과목점수['수학'] = 100
과목점수['영어'] = 99
print(과목점수)

최종점수['국어'] = 88
print(최종점수)

print(과목점수.keys())
key_list = 과목점수.keys()
for x in key_list:
    print(x)

for x in 과목점수.keys():
    print(x)

for y in 과목점수.values():
    print(y)

print(과목점수.get('영어'))
과목점수.clear()
print(과목점수)
