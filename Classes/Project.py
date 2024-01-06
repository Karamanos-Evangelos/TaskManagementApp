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
