import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.conn = self.create_connection()
        self.create_table()

    def create_connection(self):
        try:
            conn = sqlite3.connect('statistics.db')
            return conn
        except Error as e:
            print(e)
        return None

    def create_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS Statistic (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date INTEGER NOT NULL,
            earn_uzs INTEGER NOT NULL,
            earn_usd REAL NOT NULL
        );
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table_sql)
            self.conn.commit()
        except Error as e:
            print(e)

    def add_statistics(self, date, earn_uzs, earn_usd):
        sql = """
        INSERT INTO Statistic (date, earn_uzs, earn_usd) VALUES (?, ?, ?);
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (date, earn_uzs, earn_usd))
            self.conn.commit()
        except Error as e:
            print(e)