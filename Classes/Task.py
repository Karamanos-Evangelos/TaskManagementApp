## Class that represents a task

from database_handler import DatabaseHandler

class Task:
    def __init__(self,unique_ID, name, description, status, priority, assignee, project, date_created,
                 date_started, date_closed, time_tracked, dependencies, completion_percentage):
        self.db_handler = DatabaseHandler()
        self.unique_ID = unique_ID
        self.name = name
        self.description = description
        self.status = status
        self.priority = priority
        self.assignee = assignee
        self.project= project
        self.date_created = date_created
        self.date_started = date_started
        self.date_closed = date_closed
        self.time_tracked = time_tracked
        self.dependencies = dependencies
        self.completion_percentage = completion_percentage


    def get_task(self):
        return {
            'UniqueID': self.unique_ID,
            'Name': self.name,
            'Description': self.description,
            'Status': self.status,
            'Priority': self.priority,
            'Assignee': self.assignee,
            'Project': self.project,
            'DateCreated': self.date_created,
            'DateStarted': self.date_started,
            'DateClosed': self.date_closed,
            'TimeTracked': self.time_tracked,
            'Dependencies': self.dependencies,
            'CompletionPercentage': self.completion_percentage
        }

    def update_name(self, new_name):
        self.name = new_name

    def update_description(self, new_description):
        self.description = new_description

    def update_status(self, new_status):
        self.status = new_status

    def update_priority(self, new_priority):
        self.priority = new_priority

    def update_assignee(self, new_assignee):
        self.assignee = new_assignee

    def update_project(self, new_project):
        self.project = new_project

    def update_date_created(self, new_date_created):
        self.date_created = new_date_created

    def update_date_started(self, new_date_started):
        self.date_started = new_date_started

    def update_date_closed(self, new_date_closed):
        self.date_closed = new_date_closed

    def update_time_tracked(self, new_time_tracked):
        self.time_tracked = new_time_tracked

    def update_dependencies(self, new_dependencies):
        self.dependencies = new_dependencies

    def update_completion_percentage(self, new_completion_percentage):
        self.completion_percentage = new_completion_percentage

    def save_button_update_task(self):
        # Assuming 'unique_ID' is the primary key
        query = "UPDATE tasks SET name = ?, description = ?, status = ?, priority = ?, assignee = ?, project = ?, date_created = ?, date_started = ?, date_closed = ?, time_tracked = ?, dependencies = ?, completion_percentage = ? WHERE unique_ID = ?;"
        values = ( self.name, self.description, self.status, self.priority, self.assignee, self.project, self.date_created, self.date_started, self.date_closed, self.time_tracked, self.dependencies, self.completion_percentage, self.unique_ID)
        self.db_handler.execute_query(query, values)