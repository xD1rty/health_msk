import sqlite3
from datetime import date

class Database():
    def __init__(self) -> None:
        self.db = sqlite3.connect(f"{date.today()}.sql")
        self.cursor = self.db.cursor()
        create_table_if_not_exists = """
CREATE TABLE IF NOT EXISTS health (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER NOT NULL,
    country TEXT NOT NULL,
    health TEXT NOT NULL
);"""
        self.cursor.execute(create_table_if_not_exists)
        self.db.commit()
    
    def create(self, telegram_id, country, health):
        self.cursor.execute("INSERT INTO health (telegram_id, country, health) VALUES (?, ?, ?)", (telegram_id, country, health))
        self.db.commit()

    def get_by_id(self, telegram_id):
        self.cursor.execute("SELECT * FROM health WHERE telegram_id=?;", (telegram_id,))
        return self.cursor.fetchone()