
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get("https://www.google.com")

'''
driver.implicitly_wait(5)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
googlesearch_button = driver.find_element(By.NAME, "btnK")
googlesearch_button.click()
'''


''''
wait = WebDriverWait(driver, 10)

search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
search_box.send_keys("Explicit Wait")

#googlesearch_button = driver.find_element(By.NAME, "btnK")

googlesearch_button = wait.until(EC.element_to_be_clickable(By.NAME, "btnK"))
googlesearch_button.click()
'''


wait = WebDriverWait(driver, timeout=10, poll_frequency=0.1,
                     ignored_exceptions=[NoSuchElementException])

search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
search_box.send_keys("Fluent Wait")

imfl_button = wait.until(EC.element_to_be_clickable((By.NAME, "btnI")))
imfl_button.click()


driver.quit()