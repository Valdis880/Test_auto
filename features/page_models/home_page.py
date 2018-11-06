from features.locators.home_page import HomePageLocator
from features.page_models.base_page import BasePage


class HomePageElement(BasePage):
    @property
    def url(self):
        return super(HomePageElement, self).url + '/'

    @property
    def logo(self):
        return self.driver.find_element(*HomePageLocator.LOGO)

    @property
    def activity(self):
        return self.driver.find_element(*HomePageLocator.ACTIVITY_LINK)

    @property
    def mobile(self):
        return self.driver.find_element(*HomePageLocator.MOBILE_LINK)

    @property
    def blog(self):
        return self.driver.find_element(*HomePageLocator.BLOG_LINK)

    @property
    def help(self):
        return self.driver.find_element(*HomePageLocator.HELP_LINK)

    @property
    def find_faq(self):
        return self.driver.find_element(*HomePageLocator.FIND_FAQ_LINK)

    @property
    def faq(self):
        return self.driver.find_element(*HomePageLocator.FAQ_LINK)

    @property
    def forum(self):
        return self.driver.find_element(*HomePageLocator.FORUM_LINK)

    @property
    def guidelines(self):
        return self.driver.find_element(*HomePageLocator.GUIDELINES_LINK)

    @property
    def contact(self):
        return self.driver.find_element(*HomePageLocator.CONTACT_LINK)

    @property
    def search(self):
        return self.driver.find_element(*HomePageLocator.SEARCH_FIELD)

    @property
    def sign_up(self):
        return self.driver.find_element(*HomePageLocator.SIGN_UP_BUTTON)

    @property
    def log_in(self):
        return self.driver.find_element(*HomePageLocator.LOG_IN_BUTTON)

    @property
    def title(self):
        return self.driver.find_element(*HomePageLocator.TITLE)
