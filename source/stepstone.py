from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.cookie_handle import cookie_rejection
from utils.continue_next_page import next_page
from selection_handle import selection
from selection_handle import logging_in
from cfg import selections, main_page
from fetching_job_info import fetch_job_properties
from fetching_job_info.db import DB

#configuring driver
driver = webdriver.Chrome()
driver.get(main_page)
driver.maximize_window()

#rejecting cookies
cookie_rejection(driver)

#5 Steps of listing job search
#1. select parttime or fulltime
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="app-search-assistant"]/div/div/div[2]/div[1]/div[1]/div[2]/div[{selections["job_type"]}]'))).click()

#2. search and select place
selection.selector(driver, selections["place"], '//*[contains(@id, "stepstone-form-element-:r")]') #'//*[@id="stepstone-form-element-:rb:"]' '//*[@id="stepstone-form-element-:r9:"]'
selection.selector_dropdown(driver, '//*[@id="sa-custom-autocomplete-checkbox-style-fix"]/li[1]')
selection.check_selection(driver, 'search-assistant-service-ur9lzv', selections["place"])
next_page()

#3. select start date
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="search-assistant-dialog"]/div[2]/div[1]/div[1]/div[2]/div[{selections["notice_period"]}]'))).click()

#4. search and select job title
selection.selector(driver, selections["job_title"], '//*[contains(@id, "stepstone-form-element-:r")]') #'//*[@id="stepstone-form-element-:r1e:"]' '//*[@id="stepstone-form-element-:r1u:"]' '//*[@id="stepstone-form-element-:r1e:"]'
selection.selector_dropdown(driver, '//*[@id="sa-custom-autocomplete-checkbox-style-fix"]/li[1]')
selection.check_selection(driver, 'search-assistant-service-ur9lzv', selections["job_title"])
next_page()

#5. sign in
logging_in.give_username_psw(driver, selections["username"], selections["psw"])
logging_in.login(driver)

#fetching founded jobs  
job_titles, job_places, job_links= fetch_job_properties.job_elements(driver, 'res-nehv70', 'res-1foik6i')

#connecting to Database and creating table
db = DB()
db.create_table()

#writing fetched jobs to DB
for i in range(len(job_titles)):
    db.write_db(i, job_titles[i], job_places[i], job_links[i])

db.close()

driver.quit()
