## Class that represents a person

from database_handler import DatabaseHandler

class Person:
    def __init__(self, unique_ID, name, company, role):
        self.db_handler = DatabaseHandler()
        self.unique_ID = unique_ID
        self.name = name
        self.company = company
        self.role = role

    def get_person(self):
        return {
            'UniqueID': self.unique_ID,
            'Name': self.name,
            'Company': self.company,
            'Role': self.role
        }

    def update_name(self, new_name):
        self.name = new_name

    def update_company(self, new_company):
        self.company = new_company

    def update_role(self, new_role):
        self.role = new_role

    # Function to be used upon the click of the SAVE button on a Person
    def save_button_update_person(self):
        # Assuming 'unique_ID' is the primary key
        query = "UPDATE person SET name = ?, company = ?, role = ? WHERE unique_ID = ?;"
        values = (self.name, self.company, self.role, self.unique_ID)
        self.db_handler.execute_query(query, values)

