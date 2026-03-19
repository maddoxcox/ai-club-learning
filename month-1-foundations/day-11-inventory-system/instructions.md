# Day 11: Inventory System

## What You're Building
A store inventory management system using advanced OOP. Products, Categories, and an Inventory manager — all working together with JSON persistence.

## What You'll Learn
- Composition — classes that contain other classes
- Class methods (`@classmethod`) and static methods (`@staticmethod`)
- JSON serialization of custom objects (`to_dict()` / `from_dict()`)
- Advanced OOP patterns (encapsulation, composition over inheritance)

## Requirements
Build `inventory.py` with:

### Product Class
- Attributes: id, name, price, quantity, category
- Method: `to_dict()` — convert to dictionary for JSON
- Class method: `from_dict(data)` — create Product from dictionary
- Property: `total_value` — price * quantity
- `__str__`: "Widget ($29.99) - 15 in stock"

### Category Class
- Attributes: name, products (list)
- Methods: `add_product()`, `remove_product()`, `get_products()`
- Property: `total_value` — sum of all product values

### Inventory Class
- Contains all categories and products
- Methods:
  - `add_product(name, price, quantity, category)` — auto-creates category if new
  - `sell_product(product_id, quantity)` — reduce stock, handle out-of-stock
  - `restock(product_id, quantity)` — add stock
  - `low_stock_alert(threshold=5)` — list products below threshold
  - `search(query)` — search products by name
  - `save(filename)` / `load(filename)` — JSON persistence
  - `summary()` — print formatted report

### CLI Menu
Interactive menu to manage inventory.

## Also Today: Push ALL Python Projects to GitHub
Make sure days 1-11 are all committed and pushed.

## Stretch Goals
- Add transaction history (log every sale/restock with timestamp)
- Add profit/loss tracker
- Generate reports as CSV

## When You're Done
```
git add . && git commit -m "Day 11: Inventory System with advanced OOP" && git push
```
