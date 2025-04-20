class Pizza:
    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def __str__(self):
        return f"Pizza with toppings: {', '.join(self.toppings)}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.add_topping("Cheese")
        return self

    def add_pepperoni(self):
        self.pizza.add_topping("Pepperoni")
        return self

    def build(self):
        return self.pizza