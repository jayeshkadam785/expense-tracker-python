# 💰 Expense Tracker (Python Mini Project)

A simple command-line based Expense Tracker built in Python. It lets you add, view, filter, and delete daily expenses, with data saved permanently in a local JSON file.

## ✨ Features
- ➕ Add new expenses with title, amount, category, and date
- 📋 View all recorded expenses in a clean table format
- 🔍 Filter and view expenses by category
- 📊 View a spending summary with category-wise breakdown and percentages
- 🗑️ Delete an expense by ID
- 💾 Auto-saves data to `expenses.json` — data persists across runs

## 🛠️ Tech Used
- Python 3 (standard library only — `json`, `os`, `datetime`)
- No external dependencies required

## 🚀 How to Run
```bash
python expense_tracker.py
```

Then follow the on-screen menu:
```
===== EXPENSE TRACKER =====
1. Add Expense
2. View All Expenses
3. View by Category
4. View Summary
5. Delete Expense
6. Exit
```

## 📁 Project Structure
```
expense-tracker/
├── expense_tracker.py   # Main program
├── expenses.json         # Auto-generated data file (created on first run)
└── README.md
```

## 📌 Example
```
Choose an option (1-6): 1
Expense title (e.g. Groceries): Groceries
Amount (Rs): 850
Category (e.g. Food, Travel, Bills, Shopping): Food
Date (DD-MM-YYYY) [press Enter for today]:
✅ Added: Groceries - Rs 850.0 (Food)
```

## 👤 Author
Jayesh Kadam
GitHub: [jayeshkadam785](https://github.com/jayeshkadam785)

#Python #MiniProject #ExpenseTracker #TechTitans
