# Tests for the ByteBites data models.
# Run with: python3 -m pytest

from models import Menu, MenuItem, Order


def test_calculate_total_with_multiple_items():
    """The order total is the sum of all item prices."""
    order = Order()
    order.add_item(MenuItem("Spicy Burger", 8.50, "Food", 4.5))
    order.add_item(MenuItem("Large Soda", 2.25, "Drinks", 4.0))
    order.add_item(MenuItem("Brownie", 3.75, "Desserts", 4.8))

    assert order.calculate_total() == 14.50


def test_calculate_total_empty_order():
    """An order with no items has a total of 0.0."""
    order = Order()

    assert order.calculate_total() == 0.0


def test_filter_by_category():
    """Filtering returns only the items in the chosen category."""
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 8.50, "Food", 4.5))
    menu.add_item(MenuItem("Large Soda", 2.25, "Drinks", 4.0))
    menu.add_item(MenuItem("Brownie", 3.75, "Desserts", 4.8))
    menu.add_item(MenuItem("Milkshake", 5.00, "Drinks", 4.2))

    drinks = menu.filter_by_category("Drinks")

    drink_names = []
    for item in drinks:
        drink_names.append(item.name)
    assert drink_names == ["Large Soda", "Milkshake"]


def test_sort_by_price():
    """Sorting returns items from lowest to highest price and leaves the menu unchanged."""
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 8.50, "Food", 4.5))
    menu.add_item(MenuItem("Large Soda", 2.25, "Drinks", 4.0))
    menu.add_item(MenuItem("Brownie", 3.75, "Desserts", 4.8))

    sorted_items = menu.sort_by_price()

    sorted_names = []
    for item in sorted_items:
        sorted_names.append(item.name)
    assert sorted_names == ["Large Soda", "Brownie", "Spicy Burger"]

    menu_names = []
    for item in menu.items:
        menu_names.append(item.name)
    assert menu_names == ["Spicy Burger", "Large Soda", "Brownie"]


def test_filter_by_category_no_matches():
    """Filtering by a category with no items returns an empty list."""
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 8.50, "Food", 4.5))
    menu.add_item(MenuItem("Large Soda", 2.25, "Drinks", 4.0))

    assert menu.filter_by_category("Desserts") == []
