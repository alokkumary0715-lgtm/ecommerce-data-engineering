import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


# --------------------------------------------------
# Configuration
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

random.seed(42)


# --------------------------------------------------
# Helper functions
# --------------------------------------------------

def random_date(start_date, end_date):
    days = (end_date - start_date).days
    random_days = random.randint(0, days)
    return start_date + timedelta(days=random_days)


# --------------------------------------------------
# Generate customers
# --------------------------------------------------

def generate_customers(n=100):
    customers = []

    for customer_id in range(1, n + 1):
        customers.append(
            {
                "customer_id": customer_id,
                "first_name": f"Customer{customer_id}",
                "email": f"customer{customer_id}@example.com",
                "city": random.choice(
                    ["Pune", "Mumbai", "Delhi", "Bangalore", "Hyderabad"]
                ),
                "created_at": random_date(
                    datetime(2024, 1, 1),
                    datetime(2025, 12, 31),
                ),
            }
        )

    return pd.DataFrame(customers)


# --------------------------------------------------
# Generate products
# --------------------------------------------------

def generate_products(n=30):
    products = []

    categories = [
        "Electronics",
        "Fashion",
        "Home",
        "Books",
        "Sports",
    ]

    for product_id in range(1, n + 1):
        products.append(
            {
                "product_id": product_id,
                "product_name": f"Product {product_id}",
                "category": random.choice(categories),
                "price": round(random.uniform(100, 50000), 2),
            }
        )

    return pd.DataFrame(products)


# --------------------------------------------------
# Generate orders
# --------------------------------------------------

def generate_orders(n=500):
    orders = []

    for order_id in range(1, n + 1):
        orders.append(
            {
                "order_id": order_id,
                "customer_id": random.randint(1, 100),
                "order_date": random_date(
                    datetime(2025, 1, 1),
                    datetime(2025, 12, 31),
                ),
                "status": random.choice(
                    ["completed", "completed", "completed", "cancelled"]
                ),
            }
        )

    return pd.DataFrame(orders)


# --------------------------------------------------
# Generate order items
# --------------------------------------------------

def generate_order_items(orders):
    order_items = []

    item_id = 1

    for order_id in orders["order_id"]:
        number_of_items = random.randint(1, 4)

        for _ in range(number_of_items):
            order_items.append(
                {
                    "order_item_id": item_id,
                    "order_id": order_id,
                    "product_id": random.randint(1, 30),
                    "quantity": random.randint(1, 5),
                }
            )

            item_id += 1

    return pd.DataFrame(order_items)


# --------------------------------------------------
# Generate payments
# --------------------------------------------------

def generate_payments(orders):
    payments = []

    for order_id in orders["order_id"]:
        payments.append(
            {
                "payment_id": order_id,
                "order_id": order_id,
                "payment_method": random.choice(
                    ["UPI", "Credit Card", "Debit Card", "Net Banking"]
                ),
                "payment_status": random.choice(
                    ["success", "success", "success", "failed"]
                ),
            }
        )

    return pd.DataFrame(payments)


# --------------------------------------------------
# Main
# --------------------------------------------------

def main():

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    print("Generating source data...")

    customers = generate_customers()
    products = generate_products()
    orders = generate_orders()
    order_items = generate_order_items(orders)
    payments = generate_payments(orders)

    customers.to_csv(RAW_DIR / "customers.csv", index=False)
    products.to_csv(RAW_DIR / "products.csv", index=False)
    orders.to_csv(RAW_DIR / "orders.csv", index=False)
    order_items.to_csv(RAW_DIR / "order_items.csv", index=False)
    payments.to_csv(RAW_DIR / "payments.csv", index=False)

    print("Source data generated successfully!")
    print(f"Location: {RAW_DIR}")

    print("\nRecords generated:")
    print(f"Customers   : {len(customers)}")
    print(f"Products    : {len(products)}")
    print(f"Orders      : {len(orders)}")
    print(f"Order Items : {len(order_items)}")
    print(f"Payments    : {len(payments)}")


if __name__ == "__main__":
    main()