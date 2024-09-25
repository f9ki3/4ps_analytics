from database import *  # Ensure this imports your Database class properly
import sqlite3, json # Ensure sqlite3 is imported for error handling

class Accounts(Database):
    def create_account_table(self):
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

    def login_account(self, email, password):
        login_query = "SELECT * FROM accounts WHERE email = ? AND password = ?"
        self.database.execute(login_query, (email, password))
        result = self.database.fetchone()

        if result is not None:
            # Convert tuple to a dictionary for easier access
            user_data = {
                'id': result[0],
                'first_name': result[1],
                'last_name': result[2],
                'address': result[3],
                'gender': result[4],
                'birthday': result[5],
                'contact_number': result[6],
                'email': result[7]
            }
            return {'success': True, 'data': user_data}  # Return success status and user data
        else:
            return {'success': False}  # Return failure status




if __name__ == "__main__":
    accounts_instance = Accounts()
    # accounts_instance.create_account_table()  # Create the accounts table
