class GroceryStore:
    def __init__(self):
        self.prices = {
            'APL001': 2.45,
            'MIL001': 1.00,
            'CK001': 8.00
        }
        self.cart = {}

    def add_to_cart(self, item_id, quantity):
        if item_id in self.prices and quantity > 0:
            if quantity > 15:
                print("Quantity exceeds the limit. Please enter a quantity less than or equal to 15.")
                return False
            if item_id in self.cart:
                self.cart[item_id] += quantity
            else:
                self.cart[item_id] = quantity
            return True
        else:
            return False

    def calculate_total(self):
        total = 0
        for item_id, quantity in self.cart.items():
            if item_id in self.prices:
                total += self.prices[item_id] * quantity
        return total

    def checkout(self):
        total = self.calculate_total()
        return total

if __name__ == '__main__':
    store = GroceryStore()

    while True:
        print("Available Items:")
        print("1. 1kg Apple (£2.45) - APL001")
        print("2. 1L Milk (£1.00) - MIL001")
        print("3. 1kg Cake (£8.00) - CK001")
        print("4. Checkout")
        choice = input(" Enter any character to continue or enter '4' to checkout: ")

        if choice == '4':
            break

        item_id = input("Enter the item ID for the item you wish to buy: ")
        quantity = int(input("Enter the quantity: "))

        if store.add_to_cart(item_id, quantity):
            print(f"{quantity} item(s) added to the cart.")
        else:
            print("Invalid item, quantity, or quantity exceeds the limit. Please try again.")

    total_amount = store.checkout()
    print(f"Total amount to be paid: £{total_amount:.2f}")

