import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('4ps.db')  
        self.database = self.conn.cursor()   
        
          

if __name__ == "__main__":
    Database()