class MyHashSet:

    def __init__(self):
        self.values = set()

    def add(self, key: int) -> None:
        self.values.add(key)

    def remove(self, key: int) -> None:
        self.values.remove(key)

    def contains(self, key: int) -> bool:
        key in self.values