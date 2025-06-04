import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime


class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker with Database")

        # Database setup
        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # Input Frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Amount:").grid(row=0, column=0, padx=5)
        self.amount_entry = tk.Entry(input_frame, width=15)
        self.amount_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Category:").grid(row=0, column=2, padx=5)
        self.category_var = tk.StringVar(value="Food")
        tk.OptionMenu(input_frame, self.category_var, "Food", "Rent", "Travel", "Utilities", "Others").grid(row=0, column=3, padx=5)

        tk.Label(input_frame, text="Description:").grid(row=1, column=0, padx=5)
        self.description_entry = tk.Entry(input_frame, width=30)
        self.description_entry.grid(row=1, column=1, columnspan=3, padx=5)

        tk.Button(input_frame, text="Add Expense", command=self.add_expense).grid(row=0, column=4, rowspan=2, padx=5)

        # Expense List
        self.tree = ttk.Treeview(self.root, columns=("ID", "Amount", "Category", "Description", "Date"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Date", text="Date")
        self.tree.column("ID", width=50)
        self.tree.column("Amount", width=100)
        self.tree.column("Category", width=100)
        self.tree.column("Description", width=200)
        self.tree.column("Date", width=150)
        self.tree.pack(pady=10)

        # Monthly Summary
        self.summary_label = tk.Label(self.root, text="Total Expenses This Month: $0", font=("Arial", 12, "bold"))
        self.summary_label.pack(pady=10)

        # Load data
        self.load_expenses()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_expense(self):
        amount = self.amount_entry.get().strip()
        category = self.category_var.get()
        description = self.description_entry.get().strip()
        date = datetime.now().strftime("%Y-%m-%d")

        if not amount or not amount.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid amount!")
            return

        self.cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                            (float(amount), category, description, date))
        self.conn.commit()
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.load_expenses()

    def load_expenses(self):
        # Clear the treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch and display data
        self.cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)

        # Update summary
        self.cursor.execute("""
            SELECT SUM(amount) FROM expenses 
            WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
        """)
        total = self.cursor.fetchone()[0]
        self.summary_label.config(text=f"Total Expenses This Month: ${total:.2f}" if total else "Total Expenses This Month: $0")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
