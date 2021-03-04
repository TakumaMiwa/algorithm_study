class FixedQueue:
    class Empty(Exception):
        def __init__(self):
            print("error")
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity):
        self.count = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count <= 0

    def is_full(self):
        return self.count >= self.capacity

    def enque(self, x):
        if self.is_full():
            raise FixedQueue.Full

        self.que[self.rear] = x
        self.rear += 1
        self.count += 1

        if self.rear == self.capacity:
            self.rear = 0

    def deque(self):
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.count -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def find(self, value):
        for i in range(self.count):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def clear(self):
        self.count = self.front = self.rear = 0


que = FixedQueue(10)
print(que.deque())
