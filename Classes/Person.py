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

