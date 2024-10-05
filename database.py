import sqlite3

class Database:
    def __init__(self):
        # Connect to SQLite database
        self.conn = sqlite3.connect('4ps.db')
        self.database = self.conn.cursor()
        
    def close(self):
        self.conn.close()
          

if __name__ == "__main__":
    Database()