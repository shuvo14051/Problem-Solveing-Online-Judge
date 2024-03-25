from collections import Counter 

# This is one also got a time limit exceded
class FrequencyTracker:
    def __init__(self):
        self.counter = Counter()

    def add(self, number: int) -> None:
        self.counter[number] += 1

    def deleteOne(self, number: int) -> None:
        if self.counter[number] > 0:
            self.counter[number] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.counter.values()


# Time limit exceeded

"""
class FrequencyTracker:

    def __init__(self):
        self.frequencies = []
        
    def add(self, number: int) -> None:
        self.frequencies.append(number)

    def deleteOne(self, number: int) -> None:
        if number in self.frequencies:
            self.frequencies.remove(number)

    def hasFrequency(self, frequency: int) -> bool:
        counter = Counter(self.frequencies)
        values = list(counter.values())
        if frequency in values:
            return True
        return False
"""
    