from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import time


class Selenium_infra:
    def __init__(self):
        self.driver = webdriver.Chrome('./driver/chromedriver.exe')
        self.driver.maximize_window()

    # Get the url
    def getURL(self, url):
        try:
            self.driver.get(url)
        except:
            print(f'Got error while trying to get the url {url}')

    # Validate url
    def validateURL(self, page_name):
        try:
            page_name = page_name.lower()
            current_url = self.driver.current_url
            if page_name in current_url:
                print(f'This is the right url: {current_url}')
            else:
                print('This is the wrong url')
        except:
            print('Got error validating url')

    # Click on element
    def click_element(self, locator_type, locator_value, element=None, from_element=None):
        try:
            if not element:
                if from_element:
                    element = WebDriverWait(from_element, 10).until(
                        ec.element_to_be_clickable((locator_type, locator_value)))
                else:
                    element = WebDriverWait(self.driver, 10).until(
                        ec.element_to_be_clickable((locator_type, locator_value)))
            element.click()
            print(f'Clicked on element with {locator_type} = {locator_value}')
        except:
            print(f'Got error while trying to click the element with {locator_type} = {locator_value}')

    # Send keys to element
    def write(self, data, locator_type, locator_value, element=None, from_element=None):
        try:
            if not element:
                if from_element:
                    element = WebDriverWait(from_element, 10).until(
                        ec.presence_of_element_located((locator_type, locator_value)))
                else:
                    element = WebDriverWait(self.driver, 10).until(
                        ec.presence_of_element_located((locator_type, locator_value)))
            element.send_keys(data)
            print(f'Send Keys to element with {locator_type} = {locator_value}')
        except:
            print(f'Got error while trying to send keys to element with {locator_type} = {locator_value}')

    # Get the text from element
    def text_from_element(self, locator_type, locator_value, element=None, from_element=None):
        try:
            if not element:
                if from_element:
                    element = WebDriverWait(from_element, 20).until(
                        ec.presence_of_element_located((locator_type, locator_value)))
                else:
                    element = WebDriverWait(self.driver, 20).until(
                        ec.presence_of_element_located((locator_type, locator_value)))
            print(f'Get text from element with {locator_type} = {locator_value}')
            return element.text
        except:
            print(f'Got error while trying to get text from element with {locator_type} = {locator_value}')
            return ""

    # Clear element field
    def clear_element_field(self, locator_type, locator_value, element=None, from_element=None):
        try:
            if not element:
                if from_element:
                    element = WebDriverWait(from_element, 10).until(
                        ec.presence_of_element_located((locator_type, locator_value)))
                else:
                    element = WebDriverWait(self.driver, 10).until(
                        ec.presence_of_element_located((locator_type, locator_value)))
                element.clear()
                print(f'Clear text from element with {locator_type} = {locator_value}')
        except:
            print(f'Got error while trying clear text from element with {locator_type} = {locator_value}')

    # Check if element exists
    def element_is_exists(self, locator_type, locator_value, element=None, from_element=None):
        try:
            if not element:
                if from_element:
                    from_element.find_element(by=locator_type, value=locator_value)
                else:
                    self.driver.find_element(by=locator_type, value=locator_value)
            return True
        except NoSuchElementException:
            return False

    # Find element(s) list by
    def find_elementList_by(self, locator_type, locator_value, from_element=None):
        try:
            if from_element:
                element = WebDriverWait(from_element, 10).until(
                        ec.presence_of_all_elements_located((locator_type, locator_value)))
            else:
                element = WebDriverWait(self.driver, 10).until(
                        ec.presence_of_all_elements_located((locator_type, locator_value)))
            print(f'Find elementList with {locator_type} = {locator_value}')
            return element
        except:
            print(f'Got error while trying to find the elementList with {locator_type} = {locator_value}')

    # Find element by
    def find_element_by(self, locator_type, locator_value, from_element=None):
        try:
            if from_element:
                element = WebDriverWait(from_element, 10).until(
                        ec.presence_of_all_elements_located((locator_type, locator_value)))
            else:
                element = WebDriverWait(self.driver, 10).until(
                        ec.presence_of_all_elements_located((locator_type, locator_value)))
            print(f'Find element with {locator_type} = {locator_value}')
            return element
        except:
            print(f'Got error while trying to find the element with {locator_type} = {locator_value}')

    # Implicit wait - wait until element shows in the page
    def wait(self, sec):
        self.driver.implicitly_wait(sec)

    # Close the browser
    def close(self):
        time.sleep(3)
        self.driver.quit()


