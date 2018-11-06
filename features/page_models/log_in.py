from features.locators.log_in import LogInLocators
from features.page_models.base_page import BasePage


class LogInElement(BasePage):
    @property
    def log_in_url(self):
        return super(LogInElement, self).url + '/login'

    @property
    def log_in_logo(self):
        return self.driver.find_element(*LogInLocators.LOG_IN_LOGO)

    @property
    def log_in_title(self):
        return self.driver.find_element(*LogInLocators.LOG_IN_TITLE)

    @property
    def log_in_google_button(self):
        return self.driver.find_element(*LogInLocators.LOG_IN_GOOGLE_BUTTON)

    @property
    def log_in_pretitle(self):
        return self.driver.find_element(*LogInLocators.LOG_IN_PRETITILE)

    @property
    def log_in_username_input(self):
        return self.driver.find_element(*LogInLocators.LOG_IN_USERNAME_INPUT)

    @property
    def log_in_password_input(self):
        return self.driver.find_element(*LogInLocators.LOG_IN_PASSWORD_INPUT)

    @property
    def log_in_forgot_link(self):
        return self.driver.find_element(*LogInLocators.LOG_IN_FORGOT_LINK)

    @property
    def log_in_create_account_button(self):
        return self.driver.find_element(*LogInLocators.CREATE_ACCOUNT_BUTTON)

    @property
    def log_in_button(self):
        return self.driver.find_element(*LogInLocators.LOG_IN_BUTTON)

    @property
    def profile_button(self):
        return self.driver.find_element(*LogInLocators.PROFILE_BUTTON)

    @property
    def log_in_log_out_button(self):
        return self.driver.find_element(*LogInLocators.LOG_IN_LOG_OUT_BUTTON)

    @property
    def log_in_x_button(self):
        return self.driver.find_element(*LogInLocators.LOG_IN_X_BUTTON)

    @property
    def log_in_wrong_notification(self):
        return self.driver.find_element(*LogInLocators.LOG_IN_WRONG_NOTIFICATION)

    @property
    def valid_email(self):
        return 'baks11000@yandex.ru'

    @property
    def valid_pass(self):
        return 'Terepazotov1!'

    @property
    def valid_username(self):
        return 'baks1100040'

    @property
    def invalid_username(self):
        return '><><><>'

    @property
    def invalid_pass(self):
        return '11111'

    @property
    def valid_username_2(self):
        return 'validusername'

    @property
    def valid_8_symb_pass(self):
        return 'qwerty12'

    @property
    def log_in_with_script(self):
        return "<script>alert('123')</script>"

    @property
    def log_in_with_sql(self):
        return 'SELECT * FROM wotdata.wotcomments ORDER BY wotcomments.timestamp DESC LIMIT 10;'
