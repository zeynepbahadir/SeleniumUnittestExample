from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchCookieException

def cookie_rejection(driver: webdriver.Chrome) -> None:
    """
    Cookie Settings: selecting explicit references and then selecting preferences reject

    Args:
    driver (webdriver.Chrome): configured driver for handling operations
    """
    try:
        a = 4
        driver.find_element(By.ID, 'ccmgt_explicit_preferences').click() #cookie preferences
        driver.find_element(By.ID, 'ccmgt_preferences_reject').click() #cookie rejection
    except NoSuchCookieException as e:
        print(e)