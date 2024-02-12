from queue import Queue

q = Queue(maxsize = 3)
for x in range(3):
    q.put(x)
    print(x)

print(q.full())