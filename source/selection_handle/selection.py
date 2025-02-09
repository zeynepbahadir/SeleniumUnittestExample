from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, ElementNotVisibleException

def selector(driver: webdriver.Chrome, xpath: str, selection: str) -> None:
    """
    Finding search box and sending desired selection
    
    Args:
    driver (webdriver.Chrome): configured driver for handling operations
    xpath (str): xpath of the element for search box
    selection (str): desired selection
    """
    try:
        form_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        form_element.click()
        form_element.send_keys(selection)

    except ElementNotInteractableException:
        driver.save_screenshot("after_error.png")
    
def selector_dropdown(driver: webdriver.Chrome, xpath: str) -> None:
    """
    Finding desired selection on dropdown menu and selecting
    
    Args:
    driver (webdriver.Chrome): configured driver for handling operations
    xpath (str): xpath of the element for dropdown
    """
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
    except ElementNotVisibleException as e:
        print(e)

def check_selection(driver: webdriver.Chrome, xpath: str, selection: str) -> None | Exception:
    """
    Checking if the desired selection is selected
    
    Args:
    driver (webdriver.Chrome): configured driver for handling operations
    xpath (str): xpath of the element for located selection
    selection (str): desired selection
    """
    check_selection = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, xpath)))
    if check_selection.text != selection:
        raise ElementNotVisibleException