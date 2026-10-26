# ByteBites data models
# Customer: Stores customer information and purchase history.
# MenuItem: Stores a food item's name, price, category, and popularity rating.
# Menu: Stores menu items and filters them by category.
# Order: Stores selected items and calculates the total cost.


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, order):
        """Add a completed Order to this customer's purchase history."""
        self.purchase_history.append(order)

    def has_purchase_history(self):
        """Return True if the customer has made at least one purchase."""
        return len(self.purchase_history) > 0


class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add a MenuItem to the menu."""
        self.items.append(item)

    def filter_by_category(self, category):
        """Return a list of menu items that match the given category."""
        matching_items = []
        for item in self.items:
            if item.category == category:
                matching_items.append(item)
        return matching_items

    def sort_by_price(self):
        """Return a new list of menu items sorted by price, lowest to highest."""
        return sorted(self.items, key=lambda item: item.price)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add a selected MenuItem to the order."""
        self.items.append(item)

    def calculate_total(self):
        """Return the total cost of all items in the order."""
        total = 0.0
        for item in self.items:
            total += item.price
        return total
