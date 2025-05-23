# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0]*k
        self.max_size = k
        self.head = 0
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
             return False
        self.tail = (self.tail + 1) % self.max_size
        self.data[self.tail] = value
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
             return False
        if self.head == self.tail:
            self.head = 0
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.max_size
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]
        
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.tail]

    def isEmpty(self) -> bool:
        return self.tail == -1
        
    def isFull(self) -> bool:
        return not self.isEmpty() and (self.tail + 1) % self.max_size == self.head

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()