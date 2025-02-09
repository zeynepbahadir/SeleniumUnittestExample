from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, ElementNotVisibleException

def selector(driver, xpath, selection):
    """xxx"""
    try:
        form_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        form_element.click()
        form_element.send_keys(selection)

    except ElementNotInteractableException:
        driver.save_screenshot("after_error.png")
    
def selector_dropdown(driver, xpath):
    """xxx"""
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
    except ElementNotVisibleException as e:
        print(e)

def check_selection(driver, xpath, selection):
    """xxx"""
    check_selection = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, xpath)))
    if check_selection.text != selection:
        raise ElementNotVisibleException