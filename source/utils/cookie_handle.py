from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchCookieException

def cookie_rejection(driver):
    """xxx"""
    try:
        driver.find_element(By.ID, 'ccmgt_explicit_preferences').click() #cookie preferences
        driver.find_element(By.ID, 'ccmgt_preferences_reject').click() #cookie rejection
    except NoSuchCookieException as e:
        print(e)