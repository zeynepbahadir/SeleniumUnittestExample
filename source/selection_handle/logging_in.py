from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def give_username_psw(driver: webdriver.Chrome, user_name: str, password:str) -> None:
    """
    Entering username and password

    Args:
    driver (webdriver.Chrome): configured driver for handling operations
    user_name (str): username to give
    password (str): password to give
    """
    #giving username
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'stepstone-form-element-:rc2:'))).clear().send_keys(user_name)

    #continue password page
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-assistant-dialog"]/div[2]/div[1]/div[2]/div/div/div[1]/button'))).click()

    #giving password
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, 'stepstone-form-element-:rcg:'))).clear().send_keys(password)

def login(driver: webdriver.Chrome) -> None:
    """ Unchecking stay logged in option and logging in
    
    Args:
    driver (webdriver.Chrome): configured driver for handling operations
    """
    #uncheck stay logged in
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="stepstone-checkbox-:rck:"]'))).click() #uncheck stay logged in

    #log in
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-assistant-dialog"]/div[2]/div[1]/div[2]/div/div/div[3]/div/div[3]/button'))).click()