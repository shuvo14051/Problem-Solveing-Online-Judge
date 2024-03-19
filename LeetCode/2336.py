class SmallestInfiniteSet:
    def __init__(self):
        self.elements = list(range(1, 1001))
        
    def popSmallest(self) -> int:
        if self.elements:
            m = min(self.elements)
            self.elements.remove(m)
            return m
    
    def addBack(self, num: int) -> None:
        if num not in self.elements:
            self.elements.append(num)
