"""
Loops example: How do I iterate over a list and print each item with its index?
"""

items = ["apple", "banana", "cherry", "date"]

for index, item in enumerate(items, start=1):
    print(f"Item {index}: {item}")
