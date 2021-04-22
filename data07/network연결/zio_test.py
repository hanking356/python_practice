names = ['홍길동', '김길동', '박길동']
ages = [100, 200, 300]

# names와 ages 모두 리스트 타입이어야 함
total_list = list(zip(names, ages))
print(len(total_list))
print(tuple(total_list))