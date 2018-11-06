from selenium.webdriver.common.by import By


class HomePageLocator:
    LOGO = By.ID, 'wot-header-logo'
    TITLE = By.TAG_NAME, 'h1'
    ACTIVITY_LINK = By.ID, 'wot-header-menu-ACTIVITY'
    MOBILE_LINK = By.ID, 'wot-header-menu-MOBILE'
    BLOG_LINK = By.ID, 'wot-header-menu-BLOG'
    HELP_LINK = By.CSS_SELECTOR, '#root > div.jss1 > header > div > div:nth-child(2) > div > a'
    FIND_FAQ_LINK = By.CSS_SELECTOR, '#root > div.jss1 > header > div > div:nth-child(2) > div > a'
    FAQ_LINK = By.ID, 'wot-header-menu-FAQ'
    FORUM_LINK = By.ID, 'wot-header-menu-Forum'
    GUIDELINES_LINK = By.ID, 'wot-header-menu-Guidelines'
    CONTACT_LINK = By.ID, 'wot-header-menu-Contact'
    SEARCH_FIELD = By.ID, 'downshift-0-input-input'
    SIGN_UP_BUTTON = By.CSS_SELECTOR, '#root > div.jss1 > header > div > div.jss2.jss6 > div:nth-child(2) > ' \
                                      'a.jss99.jss73.jss84.jss85.jss87.jss88.jss18'
    LOG_IN_BUTTON = By.CSS_SELECTOR, '#root > div.jss1 > header > div > div.jss2.jss6 > div:nth-child(2) > ' \
                                     'a.jss99.jss73.jss75.jss78.jss18'
