from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, ElementNotVisibleException


def job_elements(driver: webdriver.Chrome, class_name_job: str, class_name_href: str) -> tuple[list[str], list[str], list[str]]:
    """
    Fetching job_titles, job_places and job_links from the output list and returning them

    Args:
    driver (webdriver.Chrome): configured driver for handling operations
    class_name_job (str): class_name of the job on output list
    class_name_href (str): class_name of the href link of the job on output list
    """
    job_elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, class_name_job)))
    hrefs = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, class_name_href)))

    job_els = [job.text for job in job_elements]
    job_titles = job_els[::2] #fetching job titles from job_els list
    job_places = job_els[1::2] #fetching job places from job_els list
    job_links = [href.get_attribute('href') for href in hrefs] #fetching href for each job founded

    return job_titles, job_places, job_links