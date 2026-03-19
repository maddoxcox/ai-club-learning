# Day 11: Inventory System
# Store inventory management with advanced OOP.

import json
import os
from datetime import datetime


class Product:
    """Represents a product in the inventory."""
    _next_id = 1

    def __init__(self, name, price, quantity, category, product_id=None):
        # TODO: Store attributes, auto-assign ID if not provided
        pass

    @property
    def total_value(self):
        """Total value of this product's stock."""
        pass

    def to_dict(self):
        """Convert to dictionary for JSON serialization."""
        pass

    @classmethod
    def from_dict(cls, data):
        """Create a Product from a dictionary."""
        pass

    def __str__(self):
        pass


class Category:
    """Represents a product category."""
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        pass

    def remove_product(self, product_id):
        pass

    @property
    def total_value(self):
        pass


class Inventory:
    """Main inventory manager."""
    def __init__(self):
        self.categories = {}
        self.products = {}

    def add_product(self, name, price, quantity, category_name):
        pass

    def sell_product(self, product_id, quantity):
        pass

    def restock(self, product_id, quantity):
        pass

    def low_stock_alert(self, threshold=5):
        pass

    def search(self, query):
        pass

    def save(self, filename="inventory.json"):
        pass

    @classmethod
    def load(cls, filename="inventory.json"):
        pass

    def summary(self):
        pass


def main():
    """Interactive CLI menu."""
    pass


if __name__ == "__main__":
    main()
