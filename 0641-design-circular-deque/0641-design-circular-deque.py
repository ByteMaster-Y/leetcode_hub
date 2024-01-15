class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.deque = [None] * k
        self.front = 0
        self.rear = 0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.size) % self.size
        self.deque[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.size) % self.size
        self.count -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.deque[(self.rear - 1 + self.size) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
