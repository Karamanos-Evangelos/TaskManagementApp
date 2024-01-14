from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TaskManagementApp(BoxLayout):
    def __init__(self, **kwargs):
        super(TaskManagementApp, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Step 1: Initialization
        self.current_stage = 'Tasks'  # Default stage
        self.initialize_app()

    def initialize_app(self):
        # Step 1: Setup main layout
        self.setup_main_layout()

    def setup_main_layout(self):
        # Add App Title
        app_title = Label(text="Task Management", font_size=24, size_hint_y=0.2)
        self.add_widget(app_title)

        # Add Buttons
        buttons_layout = BoxLayout(size_hint=(1, None), height=25, spacing=80, padding=(80, 0, 80, 0))
        tasks_button = Button(text="Tasks", size_hint_x=1, height=25, on_press=self.switch_to_tasks)
        projects_button = Button(text="Projects", size_hint_x=1, height=25, on_press=self.switch_to_projects)
        people_button = Button(text="People", size_hint_x=1, height=25, on_press=self.switch_to_people)

        # Add buttons to layout
        buttons_layout.add_widget(tasks_button)
        buttons_layout.add_widget(projects_button)
        buttons_layout.add_widget(people_button)

        # Add buttons layout to the main layout
        self.add_widget(buttons_layout)

        # Add a Label for displaying function names
        self.function_label = Label(text="", font_size=12)
        self.add_widget(self.function_label)

        # Default Stage 1
        self.switch_to_tasks()

    def switch_to_tasks(self, instance=None):
        self.current_stage = 'Tasks'
        self.clear_stage()
        self.show_content(self.get_tasks_by_status, "Stage 1: Tasks")

    def switch_to_projects(self, instance=None):
        self.current_stage = 'Projects'
        self.clear_stage()
        self.show_content(self.get_projects_list, "Stage 2: Projects")

    def switch_to_people(self, instance=None):
        self.current_stage = 'People'
        self.clear_stage()
        self.show_content(self.get_people_list, "Stage 3: People")

    def clear_stage(self):
        # Clear existing content when switching stages
        self.function_label.text = f"Clearing existing content in stage: {self.current_stage}"
        # Clear the content layout
        self.remove_content_layout()

    def remove_content_layout(self):
        for widget in self.children:
            if isinstance(widget, BoxLayout) and widget.orientation == 'vertical':
                self.remove_widget(widget)

    def show_content(self, data_fetch_method, stage_name):
        # Clear existing content
        self.clear_stage()

        content_layout = BoxLayout(orientation='vertical', spacing=10)

        data_list = data_fetch_method()

        for data_item in data_list:
            data_button = Button(text=data_item['Name'],
                                 on_press=lambda instance, item=data_item: self.show_item_tasks(item))
            content_layout.add_widget(data_button)

        self.function_label.text = f"Showing content for {stage_name}"
        self.add_widget(content_layout)

    def show_item_tasks(self, item):
        self.function_label.text = f"Showing tasks for {item['Name']}"

    def get_tasks_by_status(self):
        return [{'Name': f'Task {i}', 'Status': 'Pending'} for i in range(1, 4)]

    def get_projects_list(self):
        return [{'Name': f'Project {i}'} for i in range(1, 4)]

    def get_people_list(self):
        return [{'Name': f'Person {i}'} for i in range(1, 4)]

class MyApp(App):
    def build(self):
        return TaskManagementApp()

if __name__ == '__main__':
    MyApp().run()
