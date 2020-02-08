class Recipe:

    def __init__(self, foods, nutrition_items, name, total_price, creator):
        self.foods = foods
        self. nutrition_items = nutrition_items
        self.name = name
        self.total_price = total_price
        self.creator = creator


    def remove_food(self, food):
        self.foods.remve(food)
        self.total_price -= food.price

    def add_food(self, food):
        self.foods.append(food)

    def add_price(self, price):
        self.total_price += price

    def add_nutrition(self, nutrition_item):
        self.nutrition_items.append(nutrition_item)

