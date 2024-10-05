import sqlite3
import pandas as pd
from database import *

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

    def get_data(self):
        # Fetch data from the database
        self.database.execute('SELECT * FROM FourPsData')
        return self.database.fetchall()
        
    def get_percentage_distribution(self):
        # Get data and create a DataFrame
        data = self.get_data()
        columns = [column[0] for column in self.database.description]
        df = pd.DataFrame(data, columns=columns)
        
        # Calculate percentage distribution
        income_distribution = df['income_level'].value_counts(normalize=True) * 100
        education_distribution = df['education'].value_counts(normalize=True) * 100
        employment_distribution = df['employment_status'].value_counts(normalize=True) * 100
        
        # Calculate average and median monthly income
        average_monthly_income = df['monthly_income'].mean()
        median_monthly_income = df['monthly_income'].median()
        
        return {
            'income_distribution': income_distribution,
            'education_distribution': education_distribution,
            'employment_distribution': employment_distribution,
            'average_monthly_income': average_monthly_income,
            'median_monthly_income': median_monthly_income,
        }

if __name__ == "__main__":
    data_instance = Data()
    data_instance.create_table()  # Create table if it doesn't exist
    percentages = data_instance.get_percentage_distribution()
    
    print("Income Level Distribution (%):\n", percentages['income_distribution'])
    print("\nEducation Distribution (%):\n", percentages['education_distribution'])
    print("\nEmployment Status Distribution (%):\n", percentages['employment_distribution'])
    print("\nAverage Monthly Income:\n", percentages['average_monthly_income'])
    print("\nMedian Monthly Income:\n", percentages['median_monthly_income'])
    data_instance.close()
