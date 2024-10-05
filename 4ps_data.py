from database import *  
import sqlite3

class Data(Database):
    def create_table(self):
        # SQL command to create the table
        self.database.execute('''
            CREATE TABLE IF NOT EXISTS FourPsData (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                sex TEXT,
                age INTEGER,
                income_level TEXT,
                monthly_income INTEGER,
                education TEXT,
                education_status TEXT,
                school TEXT,
                employment_status TEXT,
                health_status TEXT,
                survey_date DATE
            );
        ''')
        self.conn.commit() 
        self.conn.close()  
        

if __name__ == "__main__":
    Data().create_table()
