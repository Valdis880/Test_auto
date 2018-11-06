from behave import *
from selenium import webdriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from features.locators.home_page import HomePageLocator
from features.locators.log_in import LogInLocators
from features.page_models.home_page import HomePageElement
from features.page_models.log_in import LogInElement

use_step_matcher('re')


@given('Log in form opened')
def step_impl(context):
    context.driver = webdriver.Chrome()
    log_in_page = LogInElement(context.driver)
    context.driver.get(log_in_page.log_in_url)


@then('I see expected elements')
def step_impl(context):
    form_logo = LogInElement(context.driver)
    form_title = LogInElement(context.driver)
    form_google_button = LogInElement(context.driver)
    form_pretitle = LogInElement(context.driver)
    form_username = LogInElement(context.driver)
    form_password = LogInElement(context.driver)
    form_forgot = LogInElement(context.driver)
    form_create_button = LogInElement(context.driver)
    form_log_in_button = LogInElement(context.driver)

    assert form_logo.log_in_logo.tag_name == 'img'
    assert form_title.log_in_title.tag_name == 'h2'
    assert form_title.log_in_title.text == 'Log in below'
    assert form_google_button.log_in_google_button.get_attribute('type') == 'button'
    assert form_google_button.log_in_google_button.text == 'LOG IN WITH GOOGLE'
    assert form_pretitle.log_in_pretitle.text == 'OR'
    assert form_username.log_in_username_input.tag_name == 'input'
    assert form_username.log_in_username_input.get_attribute('placeholder') == 'Email or Username'
    assert form_password.log_in_password_input.tag_name == 'input'
    assert form_password.log_in_password_input.get_attribute('placeholder') == 'Password'
    assert form_forgot.log_in_forgot_link.tag_name == 'a'
    assert form_forgot.log_in_forgot_link.text == 'Forgot Password?'
    assert form_create_button.log_in_create_account_button.get_attribute('role') == 'button'
    assert form_create_button.log_in_create_account_button.text == 'CREATE ACCOUNT'
    assert form_log_in_button.log_in_button.tag_name == 'button'
    assert form_log_in_button.log_in_button.get_attribute('disabled') == 'true'
    assert form_log_in_button.log_in_button.text == 'LOG IN'

    context.driver.quit()


@when('I enter valid email in the "Email or Username" field')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_username_input.clear()
    log_in_page.log_in_username_input.send_keys(log_in_page.valid_email)


@when('I enter valid password in the "Password" field')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_password_input.clear()
    log_in_page.log_in_password_input.send_keys(log_in_page.valid_pass)


@when('I press the submit button')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_button.click()


@given('I wait for the "My Profile" to load')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        expected_conditions.invisibility_of_element(LogInLocators.LOG_IN_FORM)
    )


@then('"My Profile" menu appears')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    assert log_in_page.profile_button.is_displayed
    assert log_in_page.profile_button.get_attribute('type') == 'button'

    context.driver.quit()


@when('I enter valid username in the "Email or Username" field')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_username_input.clear()
    log_in_page.log_in_username_input.send_keys(log_in_page.valid_username)


@when('I click "Log out" button')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.profile_button.click()
    WebDriverWait(context.driver, 10).until(
        expected_conditions.visibility_of_element_located(LogInLocators.PROFILE_BUTTON)
    )
    assert log_in_page.log_in_log_out_button.text == 'Log out'
    log_in_page.log_in_log_out_button.click()
    WebDriverWait(context.driver, 10).until(
        expected_conditions.visibility_of_element_located(HomePageLocator.LOG_IN_BUTTON)
    )


@then('"My Profile" menu disappears')
def step_impl(context):
    log_in_page = HomePageElement(context.driver)
    assert log_in_page.log_in.is_displayed
    assert log_in_page.sign_up.is_displayed

    context.driver.quit()


@then('Log in button is disabled')
def step_impl(context):
    log_in_page = LogInElement(context.driver)

    assert log_in_page.log_in_button.text == 'LOG IN'
    assert log_in_page.log_in_button.get_attribute('disabled') == 'true'

    context.driver.quit()


@when('I enter invalid username in the "Email or Username" field')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_username_input.clear()
    log_in_page.log_in_username_input.send_keys(log_in_page.invalid_username)


@when('I enter invalid password in the "Password" field')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_password_input.clear()
    log_in_page.log_in_password_input.send_keys(log_in_page.invalid_pass)


@then('Wrong notification appears')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    WebDriverWait(context.driver, 10).until(
        expected_conditions.visibility_of_element_located(LogInLocators.LOG_IN_WRONG_NOTIFICATION)
    )
    assert log_in_page.log_in_wrong_notification.is_displayed
    assert log_in_page.log_in_wrong_notification.text == 'Incorrect username or password'
    assert log_in_page.log_in_title.text == 'Log in below'

    context.driver.quit()


@when('I enter valid username')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_username_input.clear()
    log_in_page.log_in_username_input.send_keys(log_in_page.valid_username_2)


@when('I enter valid password, which is 8 symbols long')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_password_input.clear()
    log_in_page.log_in_password_input.send_keys(log_in_page.valid_8_symb_pass)


@when('I enter valid email in the "Password" field')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_username_input.clear()
    log_in_page.log_in_username_input.send_keys(log_in_page.valid_pass)


@when('I enter valid password in the "Email or Username" field')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_password_input.clear()
    log_in_page.log_in_password_input.send_keys(log_in_page.valid_username)


@when('I enter script in the "Email or Username" field')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_username_input.clear()
    log_in_page.log_in_username_input.send_keys(log_in_page.log_in_with_script)


@when('I enter SQL query in the "Email or Username" field')
def step_impl(context):
    log_in_page = LogInElement(context.driver)
    log_in_page.log_in_username_input.clear()
    log_in_page.log_in_username_input.send_keys(log_in_page.log_in_with_sql)