import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


# Add expense
def add_expense():
    desc = input("Enter description: ")
    amount = input("Enter amount: ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount, category, datetime.now().strftime("%Y-%m-%d")])

    print(" Expense added successfully!\n")


# View all expenses
def view_expenses():
    print("\n--- All Expenses ---")

    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                if len(row) == 4:
                    print("Description:", row[0],
                          "| Amount:", row[1],
                          "| Category:", row[2],
                          "| Date:", row[3])
    except FileNotFoundError:
        print("No expenses found.")


# Search by category
def search_category():
    category = input("Enter category to search: ")

    print("\n--- Matching Expenses ---")

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) == 4 and row[2].lower() == category.lower():
                print(row)


# Total spent by category
def category_total():
    totals = {}

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) == 4:
                category = row[2]
                amount = int(row[1])

                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount

    print("\n--- Total by Category ---")

    for category, total in totals.items():
        print(category, ":", total)


# Monthly total
def monthly_total():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) == 4 and row[3].startswith(month):
                total += int(row[1])

    print("Monthly Total:", total)


# Main menu
while True:

    print("\n===== Expense Tracker 2.0 =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Total by Category")
    print("5. Monthly Total")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_category()

    elif choice == "4":
        category_total()

    elif choice == "5":
        monthly_total()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")