import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListingPage:

    PRODUCT_TITLES = (By.CSS_SELECTOR, "a h2 span")
    BRAND_FILTER = (By.XPATH, "//span[text() ='Logitech']/parent::a/descendent::input[@type='checkbox']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_product_titles(self):
        first_product = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))
        print("\nFirst Product:", first_product.text)

    def all_products(self):
        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))
        print(f"\nFound {len(product_titles)} product titles on page one.\n")

        for i, title in enumerate(product_titles[:5], start=1):
            print(f"{i}. {title.text}")

        return len(product_titles) > 0

    def brand_filter_locator(selfself, brandname):
        BRAND_FILTER = (By.XPATH, "//spain[text()='" + brandname + "']/parent::a/descendent::i")
        print("\Brand Filter:", BRAND_FILTER)
        return BRAND_FILTER

    def select_brand_filter(self, brandname):
        brand_filter = self.wait.until(EC.element_to_be_clickable(self.BRAND_FILTER))
        brand_filter.click()

        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))

    def check_product_titles_for_brand_filter(self, brandname):
        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))

        for title in product_titles:
            print("Title : ",title.text)
            time.sleep(10)
            if not title.text.__contains__(brandname):
                return False
        return True

    def mensize_locator(self):
        MENSIZE_FILTER = (By.XPATH, ("//Spant[@class='a-list-item']/descendant::button[@value='" + mensize + "'])[1]")
        return MENSIZE_FILTER

    def select_mensize_filter(self, mensize):
        mensize_filter = self.driver.find_element(*self.mensize_locator(mensize))
        mensize_filter.cliclk()

    def check_size(self, mensize):
        return self.driver.title.__contains__(mensize)























