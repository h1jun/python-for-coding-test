from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
# 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자려구조를 활용하자.
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)