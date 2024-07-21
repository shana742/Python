# Core Python Assessment Test

import json
import datetime
from fruit_manager import add_fruit_stock, view_fruit_stock, update_fruit_stock

STOCK_FILE = 'fruit_stock.json'
LOG_FILE = 'transaction_log.txt'

# Utility functions
def validate_choice(choice, max_option):
    if choice.isdigit() and 1 <= int(choice) <= max_option:
        return True
    else:
        print("Invalid choice, please select a valid option.\n")
        return False

def validate_continue():
    continue_operation = input("Do you want to perform another operation? Press y for yes and n for no: ").strip().lower()
    return continue_operation == 'y'

def log_transaction(transaction):
    with open(LOG_FILE, 'a') as file:
        file.write(f"{datetime.datetime.now()}: {transaction}\n")

def display_menu():
    print("\nWelcome to Fruit Market")
    print("1) Manager")
    print("2) Customer")

def display_manager_menu():
    print("\nFruit Market Manager")
    print("1) Add Fruit Stock")
    print("2) View Fruit Stock")
    print("3) Update Fruit Stock")

def main():
    while True:
        display_menu()
        role = input("Select your Role: ")

        if role == '1':
            while True:
                display_manager_menu()
                choice = input("Enter your choice: ")

                if validate_choice(choice, 3):
                    if choice == '1':
                        add_fruit_stock(STOCK_FILE, log_transaction)
                    elif choice == '2':
                        view_fruit_stock(STOCK_FILE)
                    elif choice == '3':
                        update_fruit_stock(STOCK_FILE, log_transaction)

                if not validate_continue():
                    break
        elif role == '2':
            print("Customer functionality not yet implemented.\n")
        else:
            print("Invalid role selection. Please try again.\n")

if __name__ == "__main__":
    main()
