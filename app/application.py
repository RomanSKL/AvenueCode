from pages.sign_in_page import SignIn
from pages.subtask_page import SubtaskPage
from pages.task_page import TaskPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.sign_in_page = SignIn(self.driver)
        self.subtask_page = SubtaskPage(self.driver)
        self.task_page = TaskPage(self.driver)
