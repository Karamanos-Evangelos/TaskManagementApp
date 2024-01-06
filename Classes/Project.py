## Class that represents a project

from database_handler import DatabaseHandler

class Project:
    def __init__(self, db_handler,unique_ID, name, description):
        self.db_handler = db_handler
        self.unique_ID = unique_ID
        self.name = name
        self.description = description

    def get_project(self):
        return {
            'UniqueID': self.unique_ID,
            'Name': self.name,
            'Description': self.description
        }

    def update_name(self, new_name):
        self.name = new_name

    def update_description(self, new_description):
        self.description = new_description

    # Function to be used upon the click of the SAVE button on a Project
    def save_button_update_project(self):
        # Assuming 'unique_ID' is the primary key
        query = "UPDATE project SET name = ?, description = ? WHERE unique_ID = ?;"
        values = (self.name, self.description, self.unique_ID)
        self.db_handler.execute_query(query, values)