from selenium.webdriver.common.by import By
from pages.base_page import Page


class SubtaskPage(Page):
    MANAGESUBTASKSBUTTON = (By.CSS_SELECTOR, '.btn.btn-xs.btn-primary.ng-binding')
    MODALDIALOG = (By.ID, 'new_sub_task')
    NSUBTASKS = (By.XPATH, "//button[text()='(0) Manage Subtasks']")
    TASKID = (By.CSS_SELECTOR, '.modal-title.ng-binding')
    TASKDESCRIPTION = (By.ID, 'edit_task')
    DATEFORMAT = (By.CSS_SELECTOR, "[placeholder='MM/dd/yyyy']")
    TWOFIFTYDESC = (By.ID, 'new_sub_task')
    ADDSUBTASK = (By.ID, 'add-subtask')
    TWOFIFTYSUB = (By.XPATH, "//a[text()='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF']")
    REQFIELDS = (By.XPATH, "//a[text()='empty']")

    def verify_button_manage_subtask(self):
        self.wait_for_element_click(*self.MANAGESUBTASKSBUTTON)

    def verify_modal_dialog(self):
        self.wait_for_element_appear(*self.MODALDIALOG)

    def numbers_of_subtasks(self):
        self.verify_text('(0) Manage Subtasks', *self.NSUBTASKS)

    def verify_task_id(self):
        self.wait_for_element_appear(*self.TASKID)

    def verify_task_description(self):
        self.wait_for_element_appear(*self.TASKDESCRIPTION)

    def verify_due_date_format(self):
        self.wait_for_element_appear(*self.DATEFORMAT)

    def two_fifty_subtask_desc(self):
        self.input_text('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF', *self.TWOFIFTYDESC)

    def click_add_subtask(self):
        self.wait_for_element_click(*self.ADDSUBTASK)

    def verify_twofifty_created(self):
        twofiftysubtask = self.find_elements(*self.TWOFIFTYSUB)
        assert len(twofiftysubtask) != 0, f'ERROR! 250 characters subtask should be created'

    def verify_req_fields(self):
        req_fields = self.find_elements(*self.REQFIELDS)
        assert len(req_fields) == 0, f'ERROR! Task Description and Due Date are required fields'
