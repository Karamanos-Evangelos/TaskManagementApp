## Class that represents a person

class Person:
    def __init__(self, UniqueID, Name, Company, Role):
        self.unique_ID = UniqueID
        self.name = Name
        self.company = Company
        self.role = Role

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
        query = "UPDATE people SET name = ?, company = ?, role = ? WHERE unique_ID = ?;"
        values = (self.name, self.company, self.role, self.unique_ID)

        with self.db_connection:
            self.cursor.execute(query, values)

