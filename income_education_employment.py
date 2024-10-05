import sqlite3
import pandas as pd

class Database:
    def __init__(self):
        # Connect to SQLite database
        self.conn = sqlite3.connect('4ps.db')
        self.database = self.conn.cursor()
        
    def close(self):
        self.conn.close()

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

    def insert_sample_data(self):
        # Insert sample data into the table
        sample_data = [
            ('John Doe', 'Male', 30, 'Low', 15000, 'High School', 'Graduate', 'School A', 'Employed', 'Healthy', '2023-10-01'),
            ('Jane Smith', 'Female', 28, 'Medium', 30000, 'College', 'Graduate', 'School B', 'Unemployed', 'Healthy', '2023-10-02'),
            ('Alice Johnson', 'Female', 22, 'Low', 18000, 'High School', 'Graduate', 'School A', 'Employed', 'Healthy', '2023-10-03'),
            ('Bob Brown', 'Male', 35, 'High', 50000, 'College', 'Graduate', 'School C', 'Employed', 'Healthy', '2023-10-04'),
            ('Charlie Davis', 'Male', 29, 'Medium', 25000, 'College', 'Graduate', 'School D', 'Employed', 'Healthy', '2023-10-05'),
            ('Daisy Wilson', 'Female', 40, 'Low', 12000, 'High School', 'Graduate', 'School A', 'Unemployed', 'Healthy', '2023-10-06'),
        ]
        
        self.database.executemany('''
            INSERT INTO FourPsData (name, sex, age, income_level, monthly_income, education, education_status, school, employment_status, health_status, survey_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', sample_data)
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
    data_instance.insert_sample_data()  # Insert sample data
    percentages = data_instance.get_percentage_distribution()
    
    print("Income Level Distribution (%):\n", percentages['income_distribution'])
    print("\nEducation Distribution (%):\n", percentages['education_distribution'])
    print("\nEmployment Status Distribution (%):\n", percentages['employment_distribution'])
    print("\nAverage Monthly Income:\n", percentages['average_monthly_income'])
    print("\nMedian Monthly Income:\n", percentages['median_monthly_income'])
    data_instance.close()
