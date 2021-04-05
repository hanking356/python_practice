food = ['아이스크림','아이스아메리카노','생수'] #목록(list)
# hobby = []
print(food[0])
print(food[1])
print(food[2])

#food의 요소 3개를 변수 i로 순서대로 print 함
for i in range (0,3):
    print(food[i], end='')

print()

#food에 있는 요소를 차례대로 하나씩 뽑아서 print 함
for x in food: #for-each
    print(x, end='')

######
#오늘 끝나고 나서, 할 일 5가지를 목록으로 만들어보세요.
#2가지 방식으로 프린트!

print()
print()

activity=['운동하기','밥먹기','샤워하기','유튜브보기','잠 자기']

#activity의 요소 5개를 변수 i로 순서대로 print 함
for i in range(0,5):
    print(activity[i],  end=' ')

print()

#food에 있는 요소를 차례대로 하나씩 뽑아서 print 함
for x in activity:
    print(x,  end=' ')

#activity의 요소 5개를 변수 i로 순서대로 print 함. 다만, len()는 activity lsit의 갯수를 뽑아내는 함수 이므로 마지막 값 대신 사용 가능
print()
for i in range(0,len(activity)):
    print(activity[i], end=' ')



