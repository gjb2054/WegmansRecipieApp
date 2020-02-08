class Food:

    #class attrib
    location = "Wegmans"

    #instance attrib
    def __init__(self, nutrition, price, name):
        self.name = name
        self.price = price
        self.nutrition = nutrition

    def description(self):
        return "Food: " + self.name + " with price: " + self.price
