import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, item, priority):
        heapq.heappush(self._queue, (priority, item))

    def dequeue(self):
        return heapq.heappop(self._queue)[-1]

    def changePriority(self, item, priority):
        i = 0
        while i < len(self):
            if self._queue[i][1] == item:
                self._queue[i] = (priority, item)
            i = i + 1