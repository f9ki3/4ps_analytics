import sqlite3
import pandas as pd
from database import *

class Data2(Database):
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

    def get_data(self):
        # Fetch data from the database
        self.database.execute('SELECT * FROM FourPsData')
        return self.database.fetchall()
            
    def get_percentage_distribution(self):
        # Get data and create a DataFrame
        data = self.get_data()
        columns = [column[0] for column in self.database.description]
        df = pd.DataFrame(data, columns=columns)
        
        # Calculate percentage distributions
        income_distribution = df['income_level'].value_counts(normalize=True) * 100
        education_distribution = df['education'].value_counts(normalize=True) * 100
        employment_distribution = df['employment_status'].value_counts(normalize=True) * 100
        health_distribution = df['health_status'].value_counts(normalize=True) * 100
        education_status_distribution = df['education_status'].value_counts(normalize=True) * 100
        
        # Calculate average and median monthly income
        average_monthly_income = df['monthly_income'].mean()
        median_monthly_income = df['monthly_income'].median()
        
        return {
            'income_distribution': income_distribution,
            'education_distribution': education_distribution,
            'employment_distribution': employment_distribution,
            'health_distribution': health_distribution,
            'education_status_distribution': education_status_distribution,
            'average_monthly_income': average_monthly_income,
            'median_monthly_income': median_monthly_income,
        }

if __name__ == "__main__":
    data_instance = Data2()
    data_instance.create_account_table()  # Create accounts table if it doesn't exist
    percentages = data_instance.get_percentage_distribution()
    
    print("Income Level Distribution (%):\n", percentages['income_distribution'])
    print("\nEducation Distribution (%):\n", percentages['education_distribution'])
    print("\nEmployment Status Distribution (%):\n", percentages['employment_distribution'])
    print("\nHealth Status Distribution (%):\n", percentages['health_distribution'])
    print("\nEducation Status Distribution (%):\n", percentages['education_status_distribution'])
    print("\nAverage Monthly Income:\n", percentages['average_monthly_income'])
    print("\nMedian Monthly Income:\n", percentages['median_monthly_income'])
    data_instance.close()
