#Name: Quinn Dickey
#Class: 5th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Items:
    def __init__(self, stock, cost, weights):
        self.stock=stock
        self.cost=cost
        self.weights=weights
    def double_cost(self):
        self.cost *= (2)
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
oranges=Items(200,0.95,0.5)
milk=Items(50,6.68,8.6)
chicken_legs=Items(100,11.02,4.28)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"orange stock: {oranges.stock}")
print(f"milk stock: {milk.stock}")
print(f"chicken legs stock: {chicken_legs.stock}")
print(f"milk cost per carton: {milk.cost}")

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
milk.double_cost()
print(f" new price of milk per carton: {milk.cost}")
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
chicken_legs.stock=25
print(f"chicken legs stock change:{chicken_legs.stock}")
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del oranges

try:
    print(f"orange weight: {oranges.weights}")
except NameError:
    print("orange is not defined")
