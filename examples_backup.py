from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

#PATH = '/Users/zeynep/workplace/zg/SeleniumPytestExample/chromedriver-mac-arm64/chromedriver'
#driver = webdriver.Chrome(PATH)

cService = webdriver.ChromeService(executable_path='/Users/zeynep/workplace/zg/SeleniumUnittestExample/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service = cService, options=webdriver.ChromeOptions().add_argument('--start-maximized'))

#driver.get("https://www.youtube.com/")

'''
print(driver.title)
time.sleep(3)


search = driver.find_element(id, 'autoCompleteAppWrapper')
search = driver.find_element(By.CLASS_NAME, 'ytd-searchbox-spt')
driver.implicitly_wait(10.0)
time.sleep(2)
search.send_keys("test")
search.send_keys(Keys.RETURN)

print(driver.page_source)
'''

driver.get('https://www.youtube.com/results?search_query=python')
#time.sleep(5)

'''
#action chains
driver.implicitly_wait(5)
cookie = driver.find_element(By.ID, 'bigCookie')
cookie_count = driver.find_element(By.ID, 'cookies')
items = [driver.find_element(By.ID, 'productPrice' + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

'''

#cookies reject
cookies = driver.find_element(By.ID, 'dialog')
print(cookies.text)
reject = cookies.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div')
reject.click()

time.sleep(5)

#locating elements
try:
    section = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, 'ytd-section-list-renderer'))
    )

    contents = section.find_element(By.ID, 'contents')

    wait = WebDriverWait(driver, 5)

    ytd_item_section_renderer = WebDriverWait(driver, 1).until(
        EC.visibility_of_any_elements_located((By.CLASS_NAME, 'style-scope ytd-section-list-renderer')))
    print("len is:", len(ytd_item_section_renderer))

    element = ytd_item_section_renderer[0].find_element(By.XPATH, '//*[@id="video-title"]').text
    print(element)

    #navigating a page
    link = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, element))
    ).click()#send_keys(Keys.ENTER)

    time.sleep(5)

    driver.back()

    time.sleep(5)


except Exception as err:
    print("Error occured while waiting for the element:", err)
    driver.quit()

driver.quit()
