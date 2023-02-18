from behave import given, when, then


@given('Open Sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Enter Email')
def enter_email(context):
    context.app.sign_in_page.enter_email()


@when('Enter Password')
def enter_password(context):
    context.app.sign_in_page.enter_password()


@then('Sign In')
def sign_in(context):
    context.app.sign_in_page.sign_in()
