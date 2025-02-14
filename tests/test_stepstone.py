import unittest
from unittest.mock import Mock, patch
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from source.fetching_job_info.db import DB
from source.fetching_job_info import fetch_job_properties


class TestStepstone(unittest.TestCase):
    def setUp(self):
        # Mock the webdriver
        self.mock_driver = Mock()
        self.mock_wait = Mock()
        self.mock_element = Mock()
        
    @patch('selenium.webdriver.Chrome')
    def test_driver_initialization(self, mock_chrome):
        """Test that the Chrome driver is initialized correctly"""
        from selenium import webdriver
        driver = webdriver.Chrome()
        mock_chrome.assert_called_once()
    
    @patch('source.utils.cookie_handle.cookie_rejection')
    def test_cookie_rejection(self, mock_cookie_rejection):
        """Test cookie rejection functionality"""
        mock_cookie_rejection(self.mock_driver)
        mock_cookie_rejection.assert_called_once_with(self.mock_driver)

    def test_db_operations(self):
        """Test database operations"""
        test_db = DB()
        
        # Test table creation
        test_db.create_table()
        
        # Test writing to database
        test_job_data = {
            'id': 1,
            'title': 'Test Job',
            'place': 'Test Location',
            'link': 'http://test.com'
        }
        
        test_db.write_db(
            test_job_data['id'],
            test_job_data['title'],
            test_job_data['place'],
            test_job_data['link']
        )
        
        # Clean up
        test_db.close()

    @patch('source.fetching_job_info.fetch_job_properties.job_elements')
    def test_job_fetching(self, mock_job_elements):
        """Test job fetching functionality"""
        expected_data = (
            ['Job 1', 'Job 2'],
            ['Place 1', 'Place 2'],
            ['Link 1', 'Link 2']
        )
        mock_job_elements.return_value = expected_data
        
        result = fetch_job_properties.job_elements(
            self.mock_driver,
            'test-class-1',
            'test-class-2'
        )
        
        self.assertEqual(result, expected_data)
        mock_job_elements.assert_called_once_with(
            self.mock_driver,
            'test-class-1',
            'test-class-2'
        )

    @patch('source.selection_handle.selection.selector')
    @patch('source.selection_handle.selection.selector_dropdown')
    @patch('source.selection_handle.selection.check_selection')
    def test_selection_process(self, mock_check, mock_dropdown, mock_selector):
        """Test the selection process"""
        test_place = "Berlin"
        test_xpath = '//*[contains(@id, "stepstone-form-element-:r")]'
        
        # Test selection process
        mock_selector(self.mock_driver, test_place, test_xpath)
        mock_dropdown(self.mock_driver, '//*[@id="sa-custom-autocomplete-checkbox-style-fix"]/li[1]')
        mock_check(self.mock_driver, 'search-assistant-service-ur9lzv', test_place)
        
        mock_selector.assert_called_once_with(self.mock_driver, test_place, test_xpath)
        mock_dropdown.assert_called_once()
        mock_check.assert_called_once()

    @patch('source.selection_handle.logging_in.give_username_psw')
    @patch('source.selection_handle.logging_in.login')
    def test_login_process(self, mock_login, mock_credentials):
        """Test the login process"""
        test_username = "test_user"
        test_password = "test_pass"
        
        mock_credentials(self.mock_driver, test_username, test_password)
        mock_login(self.mock_driver)
        
        mock_credentials.assert_called_once_with(self.mock_driver, test_username, test_password)
        mock_login.assert_called_once_with(self.mock_driver)

if __name__ == '__main__':
    unittest.main() 