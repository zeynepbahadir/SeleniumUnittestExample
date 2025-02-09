from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, ElementNotVisibleException


def job_elements(driver, class_name_job, class_name_href):
    """xxx"""
    job_elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, class_name_job)))
    hrefs = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, class_name_href)))

    job_els = [job.text for job in job_elements]
    job_titles = job_els[::2] #fetching job titles from job_els list
    job_places = job_els[1::2] #fetching job places from job_els list
    job_links = [href.get_attribute('href') for href in hrefs] #fetching href for each job founded

    return job_titles, job_places, job_links