from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on My Tasks link')
def click_on_my_tasks_link(context):
    context.app.task_page.click_on_my_tasks_link()


@when('Enter task {name} name')
def enter_task_name(context, name):
    context.app.task_page.enter_task_name(name)


@when('Click plus')
def click_plus(context):
    context.app.task_page.click_plus()


@when('Enter two characters task name')
def enter_two_characters_task_name(context):
    context.app.task_page.enter_two_characters_task_name()


@when('Enter two fifty one characters task name')
def enter_two_fifty_one(context):
    context.app.task_page.enter_two_fifty_one()


@then('Verify My Tasks link')
def verify_my_task_link(context):
    context.app.task_page.verify_my_task_link()


@then('Verify the task page')
def verify_the_task_page(context):
    context.app.task_page.verify_the_task_page()


@then('Verify displayed message')
def displayed_message(context):
    context.app.task_page.displayed_message()


@then('Verify that new task created')
def new_task_created(context):
    context.app.task_page.new_task_created()


@then('Verify two characters task name not created')
def twochar_task_not_created(context):
    context.app.task_page.twochar_task_not_created()


@then('Verify two fifty one characters task name not created')
def twofiftyone_task_not_created(context):
    context.app.task_page.twofiftyone_task_not_created()
