#!/usr/bin/python3
from collections import deque
queue = deque(["a","b","c"])
queue.append('d')
queue.append('e')
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)

