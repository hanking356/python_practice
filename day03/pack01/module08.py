for x in range(20):
    print(x, end=' ')
print()

for x in range(1,101):
    print(x, end=' ')
print()

for x in range(0,201):
    print(x, end=' ')
print()

for x in range(1,101,2):
    print(x, end=' ')
print()

for x in range(100,501,5):
    print(x, end=' ')
print()

sum2 = 0
for x in range(100,501,10):
    sum2 = sum2 + x
print(sum2)

mul2 = 1
for x in range(3,201,8):
    mul2 = mul2*x
print(mul2)

food = ['감자','고구마','양파']
for x in food:
    print(x + '짱!')
for x in food:
    print(x + '짱!', end=' ')

print()
food2 = "감자 고구마 양파 스프 국수 라면"
food3 = food2.split()
for x3 in food3:
    if x not in ['양파', '국수']:
    #if x3 != '양파' and x3 != '국수':
        print(x3 + '맛있어!', end=' ')
        continue

