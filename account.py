from database import *  # Ensure this imports your Database class properly

class Accounts(Database):
    def create_accountTable(self):
        """Create the accounts table if it doesn't exist."""
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            address TEXT,
            gender TEXT,
            birthday TEXT,
            contact_number TEXT,
            email TEXT UNIQUE,
            password TEXT NOT NULL
        )
        '''
        self.database.execute(create_table_query)
        self.conn.commit()  # Save the changes

    def create_account(self, first_name, last_name, address, gender, birthday, contact_number, email, password):
        """Insert a new account into the accounts table."""
        create_account_query = '''
        INSERT INTO accounts (first_name, last_name, address, gender, birthday, contact_number, email, password)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        try:
            self.database.execute(create_account_query, (first_name, last_name, address, gender, birthday, contact_number, email, password))
            self.conn.commit()
            return True  # Account created successfully
        except sqlite3.IntegrityError:
            return False  # Email already exists or some other integrity issue

if __name__ == "__main__":
    # Create an instance of Accounts,
    Accounts().create_accountTable()