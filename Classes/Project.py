## Class that represents a project

class Project:
    def __init__(self, UniqueID, Name, Description):
        self.unique_ID = UniqueID
        self.name = Name
        self.description = Description

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

        with self.db_connection:
            self.cursor.execute(query, values)