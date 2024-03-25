import heapq

# Wrong answer
class Fancy:

    def __init__(self):
        self.values = []

    def append(self, val: int) -> None:
        self.values.append(val)

    def addAll(self, inc: int) -> None:
        self.values = [inc+x for x in self.values]
        

    def multAll(self, m: int) -> None:
        self.values = [m*x for x in self.values]
        
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        return self.values[idx]

fancy =  Fancy()
fancy.append(2)
fancy.addAll(3)
fancy.append(7)
fancy.multAll(2)
print(fancy.getIndex(0))
fancy.addAll(3)
fancy.append(10)
print(fancy.values)
fancy.multAll(2)
print(fancy.values)
print(fancy.getIndex(0))