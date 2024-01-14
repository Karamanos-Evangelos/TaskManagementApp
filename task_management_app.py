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
        app_title = Label(text="Task Management", font_size=24, size_hint_y=0.2)  # Adjusted font size for title
        self.add_widget(app_title)

        # Add Buttons
        buttons_layout = BoxLayout(size_hint=(1, None), height=25, spacing=80, padding=(80, 0, 80, 0))  # Increased spacing between buttons
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
        self.function_label = Label(text="", font_size=12)  # Adjusted font size for function label
        self.add_widget(self.function_label)

        # Default Stage 1
        self.switch_to_tasks()

    def switch_to_tasks(self, instance=None):
        # Step 2: Switch to Stage 1: Tasks
        self.current_stage = 'Tasks'
        self.clear_stage()
        self.show_tasks_content()

    def switch_to_projects(self, instance=None):
        # Step 2: Switch to Stage 2: Projects
        self.current_stage = 'Projects'
        self.clear_stage()
        self.show_projects_content()

    def switch_to_people(self, instance=None):
        # Step 2: Switch to Stage 3: People
        self.current_stage = 'People'
        self.clear_stage()
        self.show_people_content()

    def clear_stage(self):
        # Clear existing content when switching stages
        self.function_label.text = f"Clearing existing content in stage: {self.current_stage}"

    def show_tasks_content(self):
        self.function_label.text = f"Showing content for Stage 1: Tasks"

    def show_projects_content(self):
        self.function_label.text = f"Showing content for Stage 2: Projects"

    def show_people_content(self):
        self.function_label.text = f"Showing content for Stage 3: People"

class MyApp(App):
    def build(self):
        return TaskManagementApp()

if __name__ == '__main__':
    MyApp().run()
