import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):

        cService = webdriver.ChromeService(executable_path='/Users/zeynep/workplace/zg/SeleniumPytestExample/chromedriver-mac-arm64/chromedriver')
        self.driver = webdriver.Chrome(service=cService)
        self.driver.get("http://www.python.org")

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultsPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()