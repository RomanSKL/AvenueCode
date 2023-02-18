from selenium.webdriver.common.by import By
from pages.base_page import Page


class TaskPage(Page):
    MY_TASKS_LINK = (By.ID, 'my_task')
    ACTUAL_TEXT = (By.CSS_SELECTOR, 'h1')
    ENTERTASKFIELD = (By.ID, 'new_task')
    PLUSBUTTON = (By.CSS_SELECTOR, '.input-group-addon.glyphicon.glyphicon-plus')
    NEWTASK = (By.XPATH, "//a[text()='ABCDE']")
    TWOCHARTASK = (By.XPATH, "//a[text()='XY']")
    TWOFIFTYONE = (By.XPATH, "//a[text()='EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE']")


    def verify_my_task_link(self):
        self.wait_for_element_appear(*self.MY_TASKS_LINK)

    def click_on_my_tasks_link(self):
        self.wait_for_element_click(*self.MY_TASKS_LINK)

    def verify_the_task_page(self):
        self.verify_url_contains_query('https://qa-test.avenuecode.io/tasks')

    def displayed_message(self):
        self.verify_text('Hey Roman Skliarov, this is your todolist for today', *self.ACTUAL_TEXT)

    def enter_task_name(self, name):
        self.input_text(name, *self.ENTERTASKFIELD)

    def click_plus(self):
        self.click(*self.PLUSBUTTON)

    def new_task_created(self):
        self.wait_for_element_appear(*self.NEWTASK)

    def enter_two_characters_task_name(self):
        self.input_text('XY', *self.ENTERTASKFIELD)

    def twochar_task_not_created(self):
        twochartask = self.find_elements(*self.TWOCHARTASK)
        assert len(twochartask) == 0, f'ERROR! 2 characters task should not be created'

    def enter_two_fifty_one(self):
        self.input_text('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', *self.ENTERTASKFIELD)

    def twofiftyone_task_not_created(self):
        twofiftyonetask = self.find_elements(*self.TWOFIFTYONE)
        assert len(twofiftyonetask) == 0, f'ERROR! 251 characters task should not be created'
