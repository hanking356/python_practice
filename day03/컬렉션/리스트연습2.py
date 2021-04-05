#리스트는 순서가 있는게 가장 큰 특징
buy = []
wish = []

for _ in range(5):
    buy.append(input('입력:'))

for x in buy:
    print(x, end='')

print()

wish2 = input('입력:')
wish = wish2.split(',')
# for each
for x in wish:
    print('나는' + x + '가 되고 싶어요!')