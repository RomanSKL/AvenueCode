from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click a button labeled as Manage Subtasks')
def verify_button_manage_subtask(context):
    context.app.subtask_page.verify_button_manage_subtask()


@when('Enter TWO FIFTY SubTask Description')
def two_fifty_subtask_desc(context):
    context.app.subtask_page.two_fifty_subtask_desc()


@when('Click add subtask')
def click_add_subtask(context):
    context.app.subtask_page.click_add_subtask()
    sleep(4)


@then('Verify modal dialog')
def verify_modal_dialog(context):
    context.app.subtask_page.verify_modal_dialog()


@then('Verify button Manage Subtasks has the number of subtasks')
def numbers_of_subtasks(context):
    context.app.subtask_page.numbers_of_subtasks()


@then('Verify task ID')
def verify_task_id(context):
    context.app.subtask_page.verify_task_id()


@then('Verify task description')
def verify_task_description(context):
    context.app.subtask_page.verify_task_description()


@then('Verify SubTask due date (MM/dd/yyyy format)')
def verify_due_date_format(context):
    context.app.subtask_page.verify_due_date_format()


@then('Verify TWO FIFTY subtask created')
def verify_twofifty_created(context):
    context.app.subtask_page.verify_twofifty_created()


@then('Verify Task Description and Due Date are required fields')
def verify_req_fields(context):
    context.app.subtask_page.verify_req_fields()




