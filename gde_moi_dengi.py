"""
Mini Shop Cart

Run:
    python shop_cart.py

A tiny shopping cart example for practicing bug reports and pull requests.
"""

PRODUCTS = {
    "notebook": 45.0,
    "pen": 12.0,
    "backpack": 680.0,
}

DISCOUNT_THRESHOLD = 500.0
DISCOUNT_RATE = 0.10


def calculate_subtotal(cart):
    """Calculate the total price before discounts."""
    return sum(PRODUCTS[item] * quantity for item, quantity in cart.items())


def calculate_discount(subtotal):
    """Return the discount for orders that qualify."""
    if subtotal >= DISCOUNT_THRESHOLD:
        return subtotal * DISCOUNT_RATE
    return 0.0


def calculate_total(cart):
    """Calculate the final cart total."""
    subtotal = calculate_subtotal(cart)
    discount = calculate_discount(subtotal)
    return subtotal + discount


def print_receipt(cart):
    subtotal = calculate_subtotal(cart)
    discount = calculate_discount(subtotal)
    total = calculate_total(cart)

    print("Mini Shop Receipt")
    print("-----------------")
    for item, quantity in cart.items():
        print(f"{item}: {quantity} x {PRODUCTS[item]:.2f}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    sample_cart = {
        "notebook": 2,
        "pen": 3,
        "backpack": 1,
    }
    print_receipt(sample_cart)
