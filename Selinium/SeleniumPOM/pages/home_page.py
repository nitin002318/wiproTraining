from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # fixed timeout from 0 to 10 seconds

    def type_search_input(self):
        search_box = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search_box.clear()
        search_box.send_keys("wireless mouse")

    def click_search_button(self):
        search_button = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))  # fixed find_elements -> wait
        search_button.click()

    def is_amazon_page_loaded(self):
        return self.driver.current_url.__contains__('amazon')and self.driver.title.lower()













'''from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 0)

    def type_search_input(self):
        search_box = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search_box.clear()
        search_box.send_keys("wireless mouse")

    def click_search_button(self):
        search_button = self.driver.find_elements(*self.SEARCH_BUTTON)
        search_button.click()

    def is_amazon_page_loaded(self):
        return self.driver.current_url.__contains__('amazon') and self.driver.title.__contains__('Amazon')

'''