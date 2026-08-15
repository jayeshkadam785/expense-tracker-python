"""
Expense Tracker - Python Mini Project
Author: Jayesh Kadam
--------------------------------------
A simple command-line Expense Tracker that lets you:
  1. Add an expense
  2. View all expenses
  3. View expenses by category
  4. View total spending summary
  5. Delete an expense
  6. Exit (auto-saves to expenses.json)

Data is stored persistently in a local JSON file (expenses.json),
so your records remain even after you close the program.
"""

import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"


def load_expenses():
    """Load expenses from the JSON file, or return an empty list if none exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_expenses(expenses):
    """Save the current list of expenses to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses):
    print("\n--- Add New Expense ---")
    title = input("Expense title (e.g. Groceries): ").strip()

    while True:
        amount_str = input("Amount (Rs): ").strip()
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    category = input("Category (e.g. Food, Travel, Bills, Shopping): ").strip().title()
    if not category:
        category = "Other"

    date_str = input("Date (DD-MM-YYYY) [press Enter for today]: ").strip()
    if not date_str:
        date_str = datetime.now().strftime("%d-%m-%Y")

    expense = {
        "id": len(expenses) + 1,
        "title": title if title else "Untitled",
        "amount": round(amount, 2),
        "category": category,
        "date": date_str,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✅ Added: {expense['title']} - Rs {expense['amount']} ({expense['category']})")


def view_expenses(expenses):
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'ID':<4}{'Date':<12}{'Title':<20}{'Category':<15}{'Amount':>10}")
    print("-" * 61)
    for e in expenses:
        print(f"{e['id']:<4}{e['date']:<12}{e['title']:<20}{e['category']:<15}{e['amount']:>10.2f}")


def view_by_category(expenses):
    print("\n--- Expenses by Category ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    category = input("Enter category to filter: ").strip().title()
    filtered = [e for e in expenses if e["category"] == category]

    if not filtered:
        print(f"No expenses found under '{category}'.")
        return

    total = sum(e["amount"] for e in filtered)
    print(f"\n{'ID':<4}{'Date':<12}{'Title':<20}{'Amount':>10}")
    print("-" * 46)
    for e in filtered:
        print(f"{e['id']:<4}{e['date']:<12}{e['title']:<20}{e['amount']:>10.2f}")
    print("-" * 46)
    print(f"Total in '{category}': Rs {total:.2f}")


def view_summary(expenses):
    print("\n--- Spending Summary ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = sum(e["amount"] for e in expenses)
    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    print(f"Total expenses recorded : {len(expenses)}")
    print(f"Total amount spent      : Rs {total:.2f}\n")
    print(f"{'Category':<15}{'Amount':>10}{'Percent':>10}")
    print("-" * 35)
    for cat, amt in sorted(summary.items(), key=lambda x: x[1], reverse=True):
        percent = (amt / total) * 100
        print(f"{cat:<15}{amt:>10.2f}{percent:>9.1f}%")


def delete_expense(expenses):
    print("\n--- Delete Expense ---")
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)
    id_str = input("\nEnter ID of expense to delete: ").strip()

    if not id_str.isdigit():
        print("Invalid ID.")
        return

    exp_id = int(id_str)
    for e in expenses:
        if e["id"] == exp_id:
            expenses.remove(e)
            save_expenses(expenses)
            print(f"🗑️  Deleted: {e['title']} - Rs {e['amount']}")
            return

    print("Expense ID not found.")


def print_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View by Category")
    print("4. View Summary")
    print("5. Delete Expense")
    print("6. Exit")


def main():
    expenses = load_expenses()

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            view_summary(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("\nAll expenses saved to expenses.json. Goodbye! 👋")
            break
        else:
            print("Invalid choice, please enter a number between 1-6.")


if __name__ == "__main__":
    main()
