# Priority Queue :


import queue

q = queue.PriorityQueue()

q.put(10)
q.put(60)
q.put(20)
q.put(40)
q.put(40)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
