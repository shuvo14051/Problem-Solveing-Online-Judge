import random

class RandomizedSet:

    def __init__(self):
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        self.values.remove(val)
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.values)
    
    

