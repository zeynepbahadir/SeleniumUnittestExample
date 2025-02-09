from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException


def next_page(driver):
    """xxx"""
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-assistant-dialog"]/div[2]/div[2]/div/button[2]/span'))).click()
    except ElementNotVisibleException as e:
        print(e)