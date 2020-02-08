class Food:

    #class attrib
    location = "Wegmans"

    #instance attrib
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def description(self):
        return "Food: " + self.name + " with price: " + self.price

    def set_price(self, new_price):
        self.price = new_price