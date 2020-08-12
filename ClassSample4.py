class Computer:
    def __init__(self):
        self.sell.__maxprice = 900

    def sell(self):
     print("Selling Price: {}".format(self.sell.__maxprice))


def setMaxPrice(self, price):
    sell.__maxprice = price


c = Computer()

c.sell()

# change the price


c.__maxprice = 1000

c.sell()

# using setter function


c.setMaxPrice(1000)

c.sell()