from database import Database

class Survey(Database):
    def create_survey_table(self):
        """Create the survey_trends table if it doesn't exist."""
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS survey_trends (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            response TEXT NOT NULL,
            user_id INTEGER NOT NULL,         -- Add user_id column
            survey_date DATE NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)  -- Assuming you have a users table
        )
        '''
        self.database.execute(create_table_query)
        self.conn.commit()  # Save the changes

    def insert_response(self, response, user_id, survey_date):
        """Insert a survey response into the database."""
        insert_query = '''
        INSERT INTO survey_trends (response, user_id, survey_date) VALUES (?, ?, ?)
        '''
        self.database.execute(insert_query, (response, user_id, survey_date))  # Include user_id
        self.conn.commit()  # Save the changes
    
    def user_has_submitted(self, user_id):
        """Check if the user_id exists in the survey_trends table."""
        query = '''
        SELECT COUNT(*) FROM survey_trends WHERE user_id = ?
        '''
        cursor = self.database.execute(query, (user_id,))
        count = cursor.fetchone()[0]
        return count > 0  # Return True if user has submitted, else False
    
    def get_user_response(self, user_id):
        """Get the survey response for a specific user."""
        query = '''
        SELECT response FROM survey_trends WHERE user_id = ?
        '''
        cursor = self.database.execute(query, (user_id,))
        return cursor.fetchone()  # Returns None if no response is found
    
    def get_response_percentage(self):
        """Calculate the percentage of Emergency Needs and Livelihood Support responses."""
        # Count total responses
        total_query = '''
        SELECT COUNT(*) FROM survey_trends
        '''
        total_cursor = self.database.execute(total_query)
        total_count = total_cursor.fetchone()[0]

        # Count Emergency Needs responses
        emergency_query = '''
        SELECT COUNT(*) FROM survey_trends WHERE response = 'Emergency Needs'
        '''
        emergency_cursor = self.database.execute(emergency_query)
        emergency_count = emergency_cursor.fetchone()[0]

        # Count Livelihood Support responses
        livelihood_query = '''
        SELECT COUNT(*) FROM survey_trends WHERE response = 'Livelihood Support'
        '''
        livelihood_cursor = self.database.execute(livelihood_query)
        livelihood_count = livelihood_cursor.fetchone()[0]

        # Calculate percentages
        if total_count > 0:
            emergency_percentage = (emergency_count / total_count) * 100
            livelihood_percentage = (livelihood_count / total_count) * 100
        else:
            emergency_percentage = 0
            livelihood_percentage = 0

        # Return results as a dictionary
        return {
            'emergency_percentage': emergency_percentage,
            'livelihood_percentage': livelihood_percentage
        }
    
    def get_monthly_response_percentage_2024(self):
        """Get the monthly percentage of Emergency Needs and Livelihood Support responses for the year 2024."""
        months = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]

        emergency_percentages = []  # List to hold Emergency Needs percentages
        livelihood_percentages = []  # List to hold Livelihood Support percentages
        month_list = []              # List to hold month names

        for month in range(1, 13):  # Loop through months 1 to 12
            # Format month as two digits
            month_str = f"{month:02d}"

            # Count total responses for the month
            total_query = '''
            SELECT COUNT(*) FROM survey_trends WHERE strftime('%Y-%m', survey_date) = '2024-?'
            '''
            total_cursor = self.database.execute(total_query.replace('?', month_str))
            total_count = total_cursor.fetchone()[0]

            # Count Emergency Needs responses for the month
            emergency_query = '''
            SELECT COUNT(*) FROM survey_trends WHERE response = 'Emergency Needs' AND strftime('%Y-%m', survey_date) = '2024-?'
            '''
            emergency_cursor = self.database.execute(emergency_query.replace('?', month_str))
            emergency_count = emergency_cursor.fetchone()[0]

            # Count Livelihood Support responses for the month
            livelihood_query = '''
            SELECT COUNT(*) FROM survey_trends WHERE response = 'Livelihood Support' AND strftime('%Y-%m', survey_date) = '2024-?'
            '''
            livelihood_cursor = self.database.execute(livelihood_query.replace('?', month_str))
            livelihood_count = livelihood_cursor.fetchone()[0]

            # Calculate percentages
            if total_count > 0:
                emergency_percentage = (emergency_count / total_count) * 100
                livelihood_percentage = (livelihood_count / total_count) * 100
            else:
                emergency_percentage = 0
                livelihood_percentage = 0
            
            # Append results to the lists
            emergency_percentages.append(emergency_percentage)  # Store Emergency Needs percentage
            livelihood_percentages.append(livelihood_percentage)  # Store Livelihood Support percentage
            month_list.append(months[month - 1])               # Store month name

        # Return results as a dictionary with the required format
        return {
            'emergency_percent': emergency_percentages,
            'livelihood_percent': livelihood_percentages,
            'month': month_list
        }



# # Example of usage
# if __name__ == "__main__":
#     survey = Survey()
#     print(survey.get_monthly_response_percentage_2024())

    # # Example response (You would get this from the HTML form submission)
    # example_response = "EMERGENCY NEEDS"  # Or "LIVELIHOOD SUPPORT"
    # example_date = "2024-10-07"  # Replace with actual date input
    # survey.insert_response(example_response, example_date)
