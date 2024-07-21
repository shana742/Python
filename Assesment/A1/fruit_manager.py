import json

def load_stock(stock_file):
    try:
        with open(stock_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_stock(stock, stock_file):
    with open(stock_file, 'w') as file:
        json.dump(stock, file, indent=4)

def add_fruit_stock(stock_file, log_transaction):
    stock = load_stock(stock_file)
    fruit_name = input("Enter Fruit Name: ").strip()
    qty = float(input("Enter qty (in kg): ").strip())
    price = float(input("Enter Price: ").strip())
    stock[fruit_name] = {'qty': qty, 'price': price}
    save_stock(stock, stock_file)
    log_transaction(f"Added {fruit_name} with qty {qty} kg and price {price} per kg.")
    print(f"{fruit_name} added to stock with qty {qty} kg and price {price} per kg.\n")

def view_fruit_stock(stock_file):
    stock = load_stock(stock_file)
    if not stock:
        print("No fruits in stock.\n")
    else:
        for fruit, details in stock.items():
            print(f"Fruit: {fruit}, Qty: {details['qty']} kg, Price: {details['price']} per kg")
        print()

def update_fruit_stock(stock_file, log_transaction):
    stock = load_stock(stock_file)
    fruit_name = input("Enter Fruit Name to update: ").strip()
    if fruit_name in stock:
        qty = float(input("Enter new qty (in kg): ").strip())
        price = float(input("Enter new Price: ").strip())
        stock[fruit_name] = {'qty': qty, 'price': price}
        save_stock(stock, stock_file)
        log_transaction(f"Updated {fruit_name} to qty {qty} kg and price {price} per kg.")
        print(f"{fruit_name} stock updated to qty {qty} kg and price {price} per kg.\n")
    else:
        print(f"{fruit_name} not found in stock.\n")
