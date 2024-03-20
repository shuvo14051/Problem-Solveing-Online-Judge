class ProductOfNumbers:

    def __init__(self):
        self.values = []

    def add(self, num: int) -> None:
        self.values.append(num)

    def getProduct(self, k: int) -> int:
        prod = 1
        for i in (self.values[-k:]):
            prod *= i
        return prod
        

p =  ProductOfNumbers()
p.add(3)
p.add(0) 
p.add(2)   
p.add(5) 
p.add(4)
print(p.getProduct(2))
print(p.getProduct(3))
p.add(8)
print(p.getProduct(2))