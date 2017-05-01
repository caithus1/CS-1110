import inventory

print(inventory.restock('shop.csv', 'toaster', 5))
print(inventory.restock('shop.csv', 'marmalade', 5))
print(inventory.sell('shop.csv', 'marmalade', 4))
print(inventory.restock('shop.csv', 'toaster', 2))
print(inventory.sell('shop.csv', 'toaster', 6))
print(inventory.restock('shop.csv', 'marmalade', 2))
print(inventory.sell('shop.csv', 'toaster', 6))
print(inventory.sell('shop.csv', 'toaster', 1))