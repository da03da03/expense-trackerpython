import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    category = input("Enter category (Food, Travel, Bills, etc): ")
    amount = input("Enter amount: ")
    note = input("Optional note: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("Expense added successfully!\n")


def view_expenses():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            print("\n--- All Expenses ---")
            for row in reader:
                print(f"Date: {row[0]} | Category: {row[1]} | Amount: ₹{row[2]} | Note: {row[3]}")
            print()
    except FileNotFoundError:
        print("No expenses found.\n")


def total_spent():
    total = 0
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
        print(f"\nTotal Spent: ₹{total}\n")
    except FileNotFoundError:
        print("No data available.\n")


def menu():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_spent()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    menu()
