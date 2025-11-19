class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total_price(self):
        return self.price

class Beverage(MenuItem):
    def __init__(self, name, price, size, with_ice):
        super().__init__(name, price)
        self.size = size
        self.with_ice = with_ice

class Appetizer(MenuItem):
    def __init__(self, name, price, shareable):
        super().__init__(name, price)
        self.shareable = shareable

class MainCourse(MenuItem):
    def __init__(self, name, price, calories, is_vegetarian):
        super().__init__(name, price)
        self.calories = calories
        self.is_vegetarian = is_vegetarian

class Dessert(MenuItem):
    def __init__(self, name, price, contains_sugar):
        super().__init__(name, price)
        self.contains_sugar = contains_sugar

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def calculate_subtotal(self):
        return sum(item.get_total_price() for item in self.items)

    def apply_discounts(self, subtotal):
        discount = 0

        # Descuento 1: el total supera 50000
        if subtotal > 50000:
            discount += 0.10

        # Descuento 2: más de 3 items
        if len(self.items) >= 4:
            discount += 0.05

        # Descuento 3: al menos 1 bebida y 1 plato fuerte
        has_beverage = any(isinstance(i, Beverage) for i in self.items)
        has_main = any(isinstance(i, MainCourse) for i in self.items)
        if has_beverage and has_main:
            discount += 0.05

        return subtotal * (1 - discount)

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        return self.apply_discounts(subtotal)

menu = [
    Beverage("Coca-Cola", 5000, "350ml", True),
    Beverage("Limonada", 6000, "400ml", False),
    Beverage("Café", 4000, "250ml", False),

    Appetizer("Papas Fritas", 8000, True),
    Appetizer("Aros de Cebolla", 9000, True),

    MainCourse("Hamburguesa", 18000, 850, False),
    MainCourse("Pizza Personal", 20000, 1200, False),
    MainCourse("Ensalada Vegetariana", 15000, 400, True),

    Dessert("Helado", 7000, True),
    Dessert("Brownie", 9000, True)
]

order = Order()

order.add_item(menu[0])  # Coca-Cola
order.add_item(menu[3])  # Papas fritas
order.add_item(menu[5])  # Hamburguesa
order.add_item(menu[8])  # Helado
order.add_item(menu[9])  # Brownie
order.add_item(menu[9])  # Brownie

print("Subtotal:", order.calculate_subtotal())
print("Total con descuentos:", order.calculate_total())
