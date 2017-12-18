class Calculator:
    name = 'Good calculator'
    price = 18
    def __init__(self, name, hight, width = 0, weight = 0):
        self.name = name
        self.hight = hight
        self.wid = width
        self.we = weight
    def add(self, x, y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self, x, y):
        result = x - y
        print(result)
    def times(self, x, y):
        print(x * y)
    def divide(self, x, y):
        print(x/y)

c = Calculator('band calculator', 17,18,19)
print(c.name, c.price, c.hight, c.wid, c.we)
d = Calculator('OK', 123)
print(d.name, d.price, d.hight, d.wid, d.we)