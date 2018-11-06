from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains

from features.page_models.home_page import HomePageElement

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome(/Users/Vladislav_Aks/Desktop/Test_auto/features/steps/chromedriver)
    page = HomePageElement(context.driver)
    context.driver.get(page.url)


@then('I see all expected elements')
def step_impl(context):
    title_tag = HomePageElement(context.driver)
    logo_link = HomePageElement(context.driver)
    activity_link = HomePageElement(context.driver)
    mobile_link = HomePageElement(context.driver)
    blog_link = HomePageElement(context.driver)
    help_link = HomePageElement(context.driver)
    find_faq_link = HomePageElement(context.driver)
    find_faq_link.find_faq.click()
    faq_link = HomePageElement(context.driver)
    forum_link = HomePageElement(context.driver)
    guidelines_link = HomePageElement(context.driver)
    contact_link = HomePageElement(context.driver)
    search_field = HomePageElement(context.driver)
    sign_up_button = HomePageElement(context.driver)
    log_in_button = HomePageElement(context.driver)

    assert title_tag.title.text == 'Web of Trust (MyWOT)'
    assert logo_link.logo.tag_name == 'a'
    assert activity_link.activity.text == 'ACTIVITY'
    assert mobile_link.mobile.text == 'MOBILE'
    assert blog_link.blog.text == 'BLOG'
    assert help_link.help.text == 'HELP'
    assert faq_link.faq.text == 'FAQ'
    assert forum_link.forum.text == 'Forum'
    assert guidelines_link.guidelines.text == 'Guidelines'
    assert contact_link.contact.text == 'Contact'
    assert search_field.search.get_attribute('placeholder') == 'Search any website'
    assert sign_up_button.sign_up.text == 'SIGN UP'
    assert log_in_button.log_in.text == 'LOG IN'

    context.driver.quit()


@when('I click on the "WOT" logo')
def step_impl(context):
    logo_link = HomePageElement(context.driver)
    logo_link.logo.click()


@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePageElement(context.driver).url
    assert context.driver.current_url == expected_url

    context.driver.quit()


@when('I click the "Activity" tab')
def step_impl(context):
    activity_link = HomePageElement(context.driver)
    activity_link.activity.click()


@then('I am on the "Activity" page')
def step_impl(context):
    expected_url = 'https://www.mywot.ninja/en/community'
    assert context.driver.current_url == expected_url

    context.driver.quit()


@when('I click the "Blog" tab')
def step_impl(context):
    blog_link = HomePageElement(context.driver)
    blog_link.blog.click()


@then('I am on the "Blog" page')
def step_impl(context):
    expected_url = 'https://www.mywot.ninja/blog/'
    assert context.driver.current_url == expected_url

    context.driver.quit()


@when('I click the "Help" tab')
def step_impl(context):
    help_link = HomePageElement(context.driver)
    help_link.help.click()


@when('I click the "FAQ" tab')
def step_impl(context):
    faq_link = HomePageElement(context.driver)
    faq_link.faq.click()


@then('I am on the "FAQ" page')
def step_impl(context):
    expected_url = 'https://mywot.zendesk.com/hc/en-us'
    assert context.driver.current_url == expected_url

    context.driver.quit()


@when('I click the "Forum" tab')
def step_impl(context):
    forum_link = HomePageElement(context.driver)
    forum_link.forum.click()


@then('I am on the "Forum" page')
def step_impl(context):
    expected_url = 'https://forum.mywot.ninja/'
    assert context.driver.current_url == expected_url

    context.driver.quit()


@when('I click the "Guidelines" tab')
def step_impl(context):
    guidelines_link = HomePageElement(context.driver)
    assert guidelines_link.guidelines.text == 'Guidelines'

    guidelines_link.guidelines.click()


@then('I am on the "Guidelines" page')
def step_impl(context):
    expected_url = 'https://www.mywot.ninja/en/guidelines'
    assert context.driver.current_url == expected_url

    context.driver.quit()


@when('I click the "Contact" tab')
def step_impl(context):
    contact_link = HomePageElement(context.driver)
    assert contact_link.contact.text == 'Contact'

    contact_link.contact.click()


@then('I am on the "Contact" page')
def step_impl(context):
    expected_url = 'https://www.mywot.ninja/en/contact'
    assert context.driver.current_url == expected_url

    context.driver.quit()


@when('I click the "Sign Up" button')
def step_impl(context):
    sign_up_button = HomePageElement(context.driver)
    assert sign_up_button.sign_up.text == 'SIGN UP'
    sign_up_button.sign_up.click()


@then('Sign up popup appears')
def step_impl(context):
    expected_url = 'https://www.mywot.ninja/signup'
    assert context.driver.current_url == expected_url

    context.driver.quit()


@when('I click the "Log in" button')
def step_impl(context):
    log_in_button = HomePageElement(context.driver)
    assert log_in_button.log_in.text == 'LOG IN'
    log_in_button.log_in.click()


@then('Log in popup appears')
def step_impl(context):
    expected_url = 'https://www.mywot.ninja/login'
    assert context.driver.current_url == expected_url

    context.driver.quit()


@when('I click outside the "Sign Up" form')
def step_impl(context):
    actions = ActionChains(context.driver)
    actions.move_by_offset(100, 100).perform()
    actions.click().perform()


@when('I click outside the "Log in" form')
def step_impl(context):
    actions = ActionChains(context.driver)
    actions.move_by_offset(50, 50).perform()
    actions.click().perform()


