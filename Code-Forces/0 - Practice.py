class Item:
  def __init__(self, name: str, price: float, quantity = 0):
    self.name = name
    self.price = price
    self.quantity = quantity

  def calculate_price(self):
    return self.price * self.quantity


i1 = Item("Lenevo", "100", 3)
print(i1.calculate_price())