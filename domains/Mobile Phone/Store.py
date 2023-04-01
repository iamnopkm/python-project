import sqlite3
from Models import MobilePhone

class Store:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect('store.db')
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS inventory
                            (name TEXT, brand TEXT, price REAL, stock INTEGER)''')
        self.conn.commit()

    def add_phone(self, phone):
        self.cursor.execute("INSERT INTO inventory VALUES (?, ?, ?, ?)",
                            (phone.name, phone.brand, phone.price, phone.stock))
        self.conn.commit()
    
    def remove_phone(self, name):
        self.cursor.execute("DELETE FROM inventory WHERE name=?", (name,))
        self.conn.commit()
    
    def search_phone(self, name):
        self.cursor.execute("SELECT * FROM inventory WHERE name=?", (name,))
        row = self.cursor.fetchone()
        return None if row is None else MobilePhone(row[0], row[1], row[2], row[3])
    
    def list_phones(self):
        self.cursor.execute("SELECT * FROM inventory")
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"{row[1]} {row[0]} - ${row[2]} ({row[3]} in stock)")
    
    def sell_phone(self, name):
        phone = self.search_phone(name)
        if phone is None:
            print("Phone not found.")
        elif phone.stock == 0:
            print("Phone out of stock.")
        else:
            self.cursor.execute("UPDATE inventory SET stock=? WHERE name=?",
                                (phone.stock - 1, name))
            self.conn.commit()
            print(f"Sold {phone.brand} {phone.name}. {phone.stock-1} remaining.")
    
    def restock_phone(self, name, amount):
        phone = self.search_phone(name)
        if phone is None:
            print("Phone not found.")
        else:
            self.cursor.execute("UPDATE inventory SET stock=? WHERE name=?",
                                (phone.stock + amount, name))
            self.conn.commit()
            print(f"Restocked {phone.brand} {phone.name}. {phone.stock+amount} in stock.")

    def close_connection(self):
        self.conn.close()