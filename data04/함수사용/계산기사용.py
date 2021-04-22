from 함수정의.계산기 import *

data1 = int(input('숫자1>>'))
data2 = int(input('숫자1>>'))

result1 = add(data1, data2)
#변수에 넣거나, print할수 있는 경우는 return이 있는 경우만
print(add(data1, data2))

result2 = minus(data1, data2)
result3 = mul(data1, data2)
result4 = div(data1, data2)

print(data1, '+',data2,'=', result1)
print(data1, '-',data2,'=', result2)
print(data1, '*',data2,'=', result3)
print(data1, '/',data2,'=', result4)
