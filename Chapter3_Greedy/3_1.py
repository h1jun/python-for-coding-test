n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 거슬러 줄 수 있는 동전의 개수
    n %= coin
    
print(count)
