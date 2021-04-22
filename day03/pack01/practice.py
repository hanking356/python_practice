c1 = [22, 99, 11, 23]
c2 = [44, 99, 66, 23]
a = int(0)
for i in range(len(c1)):
  if c1[i] == c2[i]:
    a = a + 1
    print("index : " + str(i) + ", 값: ",c1[i])
print('같은 값을 가지는 갯수:', a)