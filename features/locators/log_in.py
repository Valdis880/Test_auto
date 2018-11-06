from selenium.webdriver.common.by import By


class LogInLocators:
    LOG_IN_LOGO = By.CSS_SELECTOR, 'body > div.jss118.jss331.jss320.jss332 > div.jss42.jss68.jss43.jss334.jss335.jss338' \
                                   ' > div.jss321 > img'
    LOG_IN_TITLE = By.CSS_SELECTOR, 'body > div.jss118.jss331.jss320.jss332 > div.jss42.jss68.jss43.jss334.jss335.' \
                                    'jss338 > div.jss321 > div > h2'
    LOG_IN_GOOGLE_BUTTON = By.CSS_SELECTOR, 'body > div.jss118.jss331.jss320.jss332 > div.jss42.jss68.jss43.jss334.' \
                                            'jss335.jss338 > div.jss346.jss323 > form > div.jss170.jss237.jss327 > ' \
                                            'button'
    LOG_IN_PRETITILE = By.CSS_SELECTOR, 'body > div.jss118.jss331.jss320.jss332 > div.jss42.jss68.jss43.jss334.' \
                                        'jss335.jss338 > div.jss346.jss323 > form > div:nth-child(2) > h3'
    LOG_IN_USERNAME_INPUT = By.CSS_SELECTOR, '[data-automation="desktop-login-modal-email"] input'
    LOG_IN_PASSWORD_INPUT = By.CSS_SELECTOR, 'body > div.jss118.jss331.jss320.jss332 > div.jss42.jss68.jss43.jss334.' \
                                             'jss335.jss338 > div.jss346.jss323 > form > div:nth-child(4) > div > div > ' \
                                             'input'
    LOG_IN_FORGOT_LINK = By.CSS_SELECTOR, 'body > div.jss118.jss331.jss320.jss332 > div.jss42.jss68.jss43.jss334.' \
                                          'jss335.jss338 > div.jss346.jss323 > form > div:nth-child(4) > div > p > span ' \
                                          '> a'
    CREATE_ACCOUNT_BUTTON = By.CSS_SELECTOR, 'body > div.jss118.jss331.jss320.jss332 > div.jss42.jss68.jss43.jss334.' \
                                             'jss335.jss338 > div.jss368.jss324 > a'
    LOG_IN_BUTTON = By.CSS_SELECTOR, '#wot-login-button'

    PROFILE_BUTTON = By.CSS_SELECTOR, '#root > div.jss1 > header > div > div.jss2.jss6 > button'

    LOG_IN_LOG_OUT_BUTTON = By.CSS_SELECTOR, '#menu-list-grow > ul > a:nth-child(5)'

    LOG_IN_FORM = By.CSS_SELECTOR, 'body > div.jss118.jss331.jss320.jss332 > div.jss42.jss68.jss43.jss334.jss335.jss338'

    LOG_IN_WRONG_NOTIFICATION = By.CSS_SELECTOR, '#message-id'

