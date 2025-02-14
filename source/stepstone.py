from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from contextlib import contextmanager
from utils.cookie_handle import cookie_rejection
from utils.continue_next_page import next_page
from selection_handle import selection, logging_in
from cfg import selections, main_page
from fetching_job_info import fetch_job_properties
from fetching_job_info.db import DB

#configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class StepstoneJobScraper:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.db = None

    def setup_driver(self) -> None:
        """Initialize and configure the web driver"""
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(main_page)
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 10)
            logger.info("WebDriver setup completed successfully")
        except Exception as e:
            logger.error(f"Failed to setup WebDriver: {e}")
            raise
    
    def navigate_to_main_page(self) -> None:
        """Navigate to the main page and handle cookies"""
        try:
            self.driver.get(main_page)
            cookie_rejection(self.driver)
            logger.info("Navigated to main page and handled cookies")
        except Exception as e:
            logger.error(f"Failed to navigate to main page: {e}")
            raise

    def select_job_type(self) -> None:
        """Select job type (full-time/part-time)"""
        try:
            job_type_xpath = f'//*[@id="app-search-assistant"]/div/div/div[2]/div[1]/div[1]/div[2]/div[{selections["job_type"]}]'
            self.wait.until(EC.visibility_of_element_located((By.XPATH, job_type_xpath))).click()
            logger.info(f"Selected job type: {selections['job_type']}")
        except Exception as e:
            logger.error(f"Failed to select job type: {e}")
            raise

    def select_location(self) -> None:
        """Select job location"""
        try:
            selection.selector(self.driver, selections["place"], '//*[contains(@id, "stepstone-form-element-:r")]')
            selection.selector_dropdown(self.driver, '//*[@id="sa-custom-autocomplete-checkbox-style-fix"]/li[1]')
            selection.check_selection(self.driver, 'search-assistant-service-ur9lzv', selections["place"])
            next_page()
            logger.info(f"Selected location: {selections['place']}")
        except Exception as e:
            logger.error(f"Failed to select location: {e}")
            raise

    def select_start_date(self) -> None:
        """Select job start date"""
        try:
            start_date_xpath = f'//*[@id="search-assistant-dialog"]/div[2]/div[1]/div[1]/div[2]/div[{selections["notice_period"]}]'
            self.wait.until(EC.visibility_of_element_located((By.XPATH, start_date_xpath))).click()
            logger.info("Selected start date")
        except Exception as e:
            logger.error(f"Failed to select start date: {e}")
            raise

    def select_job_title(self) -> None:
        """Select job title"""
        try:
            selection.selector(self.driver, selections["job_title"], '//*[contains(@id, "stepstone-form-element-:r")]')
            selection.selector_dropdown(self.driver, '//*[@id="sa-custom-autocomplete-checkbox-style-fix"]/li[1]')
            selection.check_selection(self.driver, 'search-assistant-service-ur9lzv', selections["job_title"])
            next_page()
            logger.info(f"Selected job title: {selections['job_title']}")
        except Exception as e:
            logger.error(f"Failed to select job title: {e}")
            raise

    def perform_login(self) -> None:
        """Perform login"""
        try:
            logging_in.give_username_psw(self.driver, selections["username"], selections["psw"])
            logging_in.login(self.driver)
            logger.info("Login successful")
        except Exception as e:
            logger.error(f"Failed to login: {e}")
            raise

    def fetch_jobs(self) -> tuple[list[str], list[str], list[str]]:
        """Fetch job listings"""
        try:
            job_titles, job_places, job_links = fetch_job_properties.job_elements(
                self.driver, 'res-nehv70', 'res-1foik6i'
            )
            logger.info(f"Fetched {len(job_titles)} jobs")
            return job_titles, job_places, job_links
        except Exception as e:
            logger.error(f"Failed to fetch jobs: {e}")
            raise

    def save_jobs_to_db(self, job_titles: list[str], job_places: list[str], job_links: list[str]) -> None:
        """Save fetched jobs to database"""
        try:
            self.db = DB()
            self.db.create_table()
            
            for i in range(len(job_titles)):
                self.db.write_db(i, job_titles[i], job_places[i], job_links[i])
            
            logger.info(f"Saved {len(job_titles)} jobs to database")
        except Exception as e:
            logger.error(f"Failed to save jobs to database: {e}")
            raise

    @contextmanager
    def cleanup(self):
        """Context manager for cleanup"""
        try:
            yield
        finally:
            if self.db:
                self.db.close()
                logger.info("Closed database connection")
            if self.driver:
                self.driver.quit()
                logger.info("Closed WebDriver")

    def run(self):
        """Main execution method"""
        with self.cleanup():
            self.setup_driver()
            self.navigate_to_main_page()
            self.select_job_type()
            self.select_location()
            self.select_start_date()
            self.select_job_title()
            self.perform_login()
            
            job_titles, job_places, job_links = self.fetch_jobs()
            self.save_jobs_to_db(job_titles, job_places, job_links)

def main():
    scraper = StepstoneJobScraper()
    try:
        scraper.run()
    except Exception as e:
        logger.error(f"Scraping failed: {e}")
        raise

if __name__ == "__main__":
    main()
