#hobby=[]라는 리스트는, 리스트를 먼저 설정한 후 뒤에서 하나식 담는 것을 의미

#append를 활용해 코딩을 hobby에 추가한 후 hobby의 갯수를 print
hobby =[]
hobby.append('코딩')
print('개수>>', len(hobby))

#append를 활용해 등산을 추가한 후 hobby의 갯수를 print
hobby.append('등산')
print('개수>>', len(hobby))

#요소 3개를 data에 입력 받아서 hobby에 추가
for _ in range(3): #0,1,2
    data = input('당신의 새로운 취미는>>')
    hobby.append(data)

#hobby의 개수를 출력하는 것
print('개수>>', len(hobby))

#hobby에 있는 요소를 차례대로 하나씩 뽑아서 print 함
for x in hobby:
    print(x)

