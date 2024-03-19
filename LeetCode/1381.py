class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        
    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        
    def pop(self) -> int:  
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k >= len(self.stack):
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val
        

s = CustomStack(3)
s.push(1)
s.push(2)
s.pop()
s.push(2)                          
s.push(3)                          
s.push(4)
s.increment(5, 100)
s.increment(2, 100)
print(s.stack)