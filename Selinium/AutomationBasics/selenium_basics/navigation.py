import time
from tkinter import image_names

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get("https://www.google.com")
time.sleep(5)

driver.get("https://www.wikipedia.com/")
time.sleep(2)

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()
time.sleep(3)
driver.refresh()
time.sleep(3)

driver.quit()







