from collections import OrderedDict

# Declare the product catalog
products = {
    "apple": {"price/kg": 30, "stock in kg": 50},
    "banana": {"price/kg": 10, "stock in kg": 100},
    "chocolate": {"price/kg": 50, "stock in kg": 40},
    "milk": {"price/kg": 25, "stock in kg": 60},
    "kiwi":{"price/kg":45,"stock in kg":55},
    "orange":{"price/kg":44,"stock in kg":65}
}

# Declare the cart
cart = OrderedDict()

#showprodcts

def show_products():
    print("\nAvailable Products:")
    print("-" * 40)
    print(f"{'Item':<15}{'Price/kg (₹)':<10}{'Stock in kg':<10}")
    print("-" * 40)
    for item, info in products.items():
        print(f"{item.title():<15}{info['price/kg']:<10}{info['stock in kg']:<10}")
    print("-" * 40)


# Add item to cart function
def add_to_cart(item, quantity):
    item = item.lower()

    # We don't need 'global' unless you're reassigning cart/products
    if item in products:
        if products[item]['stock in kg'] >= quantity:
            products[item]['stock in kg'] -= quantity
            if item in cart:
                cart[item]['quantity'] += quantity
            else:
                cart[item] = {
                    'price/kg': products[item]['price/kg'],
                    'quantity': quantity
                }
            print(f"Added {quantity} {item}(s) to cart.")
        else:
            print("Not enough stock.")
    else:
        print("Item not found.")

#remove item from the cart

def remove_from_cart(item):
    if item in cart:
        products[item]['stock in kg'] += cart[item]['quantity']
        del cart[item]
        print(f"Removed {item} from cart.")
    else:
        print("Item not in cart.")

#veiw cart
        
def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("\nYour Cart:")
    total = 0
    for item, details in cart.items():
        subtotal = details['price/kg'] * details['quantity']
        print(f"{item.title()}: ₹{details['price/kg']} x {details['quantity']} = ₹{subtotal}")
        total += subtotal
    print(f"Total: ₹{total}")

#generating invoice
def checkout():
    if not cart:
        print("Cart is empty.")
        return
    print("\nGenerating Invoice...")
    view_cart()
    print("Thank you for shopping!")
    cart.clear()

#main menu loop
def main():
    while True:
        print("\n--- E-Commerce Cart ---")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            show_products()
        elif choice == '2':
            item = input("Enter item name: ").lower()
            qty = int(input("Enter quantity: "))
            add_to_cart(item, qty)
        elif choice == '3':
            item = input("Enter item name to remove: ").lower()
            remove_from_cart(item)
        elif choice == '4':
            view_cart()
        elif choice == '5':
            checkout()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


