import csv

FILE_NAME = "expenses.csv"


# Function to add expense
def add_expense():
    desc = input("Enter expense description: ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])

    print("Expense added successfully!\n")


# Function to view expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)

            print("\nAll Expenses:")
            print("---------------------")

            for row in reader:
                print(f"Item: {row[0]}, Amount: ₹{row[1]}")

            print()

    except FileNotFoundError:
        print("No expenses found.\n")


# Function to calculate total expenses
def total_expenses():

    total = 0

    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                total += float(row[1])

        print(f"\nTotal Expenses: ₹{total}\n")

    except FileNotFoundError:
        print("No expenses found.\n")


# Main menu function
def menu():

    while True:

        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice, try again.\n")


# Run the program
menu()