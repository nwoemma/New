# import tkinter as tk
# from tkinter import ttk, messagebox
# import sqlite3
# import matplotlib.pyplot as plt

# # Database Setup
# def setup_database():
#     conn = sqlite3.connect("finance_manager.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS transactions (
#             id INTEGER PRIMARY KEY,
#             amount REAL NOT NULL,
#             category TEXT NOT NULL,
#             date TEXT NOT NULL,
#             notes TEXT
#         )
#     """)
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS budgets (
#             id INTEGER PRIMARY KEY,
#             category TEXT NOT NULL UNIQUE,
#             amount REAL NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()

# # Add Expense
# def add_expense(amount, category, date, notes):
#     conn = sqlite3.connect("finance_manager.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO transactions (amount, category, date, notes) VALUES (?, ?, ?, ?)",
#                    (amount, category, date, notes))
#     conn.commit()
#     conn.close()

# # View Transactions
# def view_transactions():
#     conn = sqlite3.connect("finance_manager.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM transactions")
#     rows = cursor.fetchall()
#     conn.close()
#     return rows

# # GUI Setup
# class FinanceManagerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Personal Finance Manager")
#         self.create_widgets()

#     def create_widgets(self):
#         # Add Expense Section
#         self.amount_label = tk.Label(self.root, text="Amount:")
#         self.amount_label.grid(row=0, column=0, padx=10, pady=5)
#         self.amount_entry = tk.Entry(self.root)
#         self.amount_entry.grid(row=0, column=1, padx=10, pady=5)

#         self.category_label = tk.Label(self.root, text="Category:")
#         self.category_label.grid(row=1, column=0, padx=10, pady=5)
#         self.category_entry = tk.Entry(self.root)
#         self.category_entry.grid(row=1, column=1, padx=10, pady=5)

#         self.date_label = tk.Label(self.root, text="Date (YYYY-MM-DD):")
#         self.date_label.grid(row=2, column=0, padx=10, pady=5)
#         self.date_entry = tk.Entry(self.root)
#         self.date_entry.grid(row=2, column=1, padx=10, pady=5)

#         self.notes_label = tk.Label(self.root, text="Notes:")
#         self.notes_label.grid(row=3, column=0, padx=10, pady=5)
#         self.notes_entry = tk.Entry(self.root)
#         self.notes_entry.grid(row=3, column=1, padx=10, pady=5)

#         self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
#         self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

#         # View Transactions Section
#         self.view_button = tk.Button(self.root, text="View Transactions", command=self.view_transactions)
#         self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

#         # Show Pie Chart
#         self.chart_button = tk.Button(self.root, text="Show Spending Chart", command=self.show_chart)
#         self.chart_button.grid(row=6, column=0, columnspan=2, pady=10)

#     def add_expense(self):
#         amount = self.amount_entry.get()
#         category = self.category_entry.get()
#         date = self.date_entry.get()
#         notes = self.notes_entry.get()

#         if not amount or not category or not date:
#             messagebox.showerror("Error", "All fields except Notes are required!")
#             return

#         try:
#             add_expense(float(amount), category, date, notes)
#             messagebox.showinfo("Success", "Expense added successfully!")
#             self.clear_entries()
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def view_transactions(self):
#         transactions = view_transactions()
#         view_window = tk.Toplevel(self.root)
#         view_window.title("Transactions")

#         tree = ttk.Treeview(view_window, columns=("Amount", "Category", "Date", "Notes"), show="headings")
#         tree.heading("Amount", text="Amount")
#         tree.heading("Category", text="Category")
#         tree.heading("Date", text="Date")
#         tree.heading("Notes", text="Notes")

#         for transaction in transactions:
#             tree.insert("", "end", values=transaction[1:])

#         tree.pack(fill="both", expand=True)

#     def show_chart(self):
#         transactions = view_transactions()
#         category_totals = {}

#         for transaction in transactions:
#             category = transaction[2]
#             amount = transaction[1]
#             category_totals[category] = category_totals.get(category, 0) + amount

#         categories = list(category_totals.keys())
#         amounts = list(category_totals.values())

#         plt.figure(figsize=(8, 6))
#         plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
#         plt.title("Spending by Category")
#         plt.show()

#     def clear_entries(self):
#         self.amount_entry.delete(0, tk.END)
#         self.category_entry.delete(0, tk.END)
#         self.date_entry.delete(0, tk.END)
#         self.notes_entry.delete(0, tk.END)

# # Main Program
# if __name__ == "__main__":
#     setup_database()
#     root = tk.Tk()
#     app = FinanceManagerApp(root)
#     root.mainloop()
x = 10
y = 
print(x +y )