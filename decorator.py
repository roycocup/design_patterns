class Burger():
    name = "Generic Burger"
    ingredients = []
    
    def __init__(self) -> None:
        self.add_ingredient(self.name)

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredients(self):
        return self.ingredients

    def __str__(self):
        return ", ".join(self.get_ingredients())

class NormalBurger(Burger):
    name = "Normal Burger"

class CheeseBurger(Burger):
    name = "Cheese Burger"

class Ingredient(Burger):
    name = "Generic Ingredient"
    
    def __init__(self, ingredient):
        self.ingredients = ingredient.get_ingredients()
    
    def get_ingredients(self):
        self.ingredients.append(self.name)
        return self.ingredients


class Lettuce(Ingredient):
    name = "Lettuce"

class Tomato(Ingredient):
    name = "Tomato"

class Cheese(Ingredient):
    name = "Cheese"


if __name__ == "__main__":
    burger = NormalBurger()
    composed = Cheese(Tomato(Lettuce(burger)))
    print(composed)







