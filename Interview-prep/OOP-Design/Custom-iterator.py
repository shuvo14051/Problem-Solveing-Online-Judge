class CustomIterator:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2**self.n
            self.n += 1
            return result

        else:
            raise StopIteration
        

c = CustomIterator(10)
iterator = iter(c)

for i in range(12):
    print(next(iterator))