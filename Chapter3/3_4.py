# 주어진 n에 대하여 최대한 많이 나누기를 수행하면 된다.
# 정당성 분석 : N이 아무리 큰 수여도, K로 계속 나눈다면 기하급수적으로 빠르게 줄일수 있다.


# My Code
count = 0
n, k = map(int, input().split())
 
while True:

    if n % k == 0:
        n /= k
        count += 1
    elif n > 1:
        n -= 1
        count += 1
    elif n == 1:
        break
print(count)




# 답안 예시
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k  # 가장 가까운 K로 나누어 떨어지는 수를 알아내기 -> target은 k로 나누어 떨어지는 수
    result += (n - target) # 1을 빼는 연산을 총 몇번하는지 한번에 계산하여 넣어주기
    n = target

    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # K로 나누기
    result += 1
    n //=k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n -1)
print(result)
