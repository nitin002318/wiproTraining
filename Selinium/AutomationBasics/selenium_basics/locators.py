import time
from tkinter import image_names

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
driver.get("https://www.google.com")

# time.sleep(15)
#
# search_input = driver.find_element(By.NAME, "q")
# search_input.send_keys("locators")
# time.sleep(3)

#googlesearch_button = driver.find_element(By.NAME, "btnk")
#googlesearch_button.click()
#search_input.clear()
#time.sleep(30)

#imfl_button = driver.find_element(By.CLASS_NAME, "RNmpXc")
#imfl_button.click()
#time.sleep(3)


#href_elements = driver.find_element(By.TAG_NAME, "a")
#for elmt in href_elements:
#    print(f'{elmt.text} -{elmt.get_attribute("href")}')

#images_link = driver.find_element(By.LINK_TEXT, "Images")
#images_link.click()
#time.sleep(10)

#images_link = driver.find_element(By.LINK_TEXT, "ma")
#images_link.click()
#time.sleep(10)

#search_input = driver.find_element(By.CSS_SELECTOR, 'div > textarea')
#search_input.send_keys('selenium')
#time.sleep(5)

#setting_text = driver.find_element(By.XPATH, 'html/body/div[2]/div[7]/div/div[2]/div[2]/span/span/g-popup/div[1]/div')
#print(setting_text.text)
#time.sleep(5)

driver.get("https://the-internet.herokuapp.com/tables")
time.sleep(5)


'''
and_example = driver.find_element(By.XPATH, "//td[text()='Tim' and @class='first-name']")
print(f"AND Example -> Found with both conditions: {and_example.text}")

or_example = driver.find_element(By.XPATH, "//td[text()='Tim' or text()='Frank']")
print(f"OR Example -> Found with OR condition: {or_example.text}")


rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr/td")
print(f"Child Example -> Found {len(rows)} columns in the first table.")

email_cell = driver.find_element(By.XPATH, "//table[@id='table1']/td[text()='jdoe@hotmail.com]")
parent_row = driver.find_element(By.XPATH, "//table[@id='table1']/td[text()='jdoe@hotmail.com]/parent::tr")
print(f"Parent Example -> Email '{email_cell.text}' belongs to row with first name: "
      f"{parent_row.find_element(By.XPATH,'.td[2]').text}")

'''

#driver.quit()
'''
ancestor_table = driver.find_element(By.XPATH,"//td[text()='jsmith@gmail.com']/ancestor::table" )
print(f"Ancestor Example -> Table ID: {ancestor_table.get_attribute('id')}")

descendants = driver.find_elements(By.XPATH, "//table[@id='table1']/descendant::td")
print(f"Descendant Example -> Found {len(descendants)} descendant cells.")

'''


#RELATIVE LOCATOR
#
# driver.get("https://www.saucedemo.com/")
# time.sleep(2)
#
# username_field = driver.find_element(By.ID, "user-name")
# password_field = driver.find_element(By.ID, "password")
# login_button = driver.find_element(By.ID, "login-button")
#
# elmt_above_password = driver.find_element(
#     locate_with(By.TAG_NAME, "input").above(password_field)
# )
# print(f"Above Example -> Text above password: {elmt_above_password.get_attribute('placeholder')}")
# time.sleep(5)
#
# field_below_username = driver.find_element(
#     locate_with(By.TAG_NAME, "input").below(username_field)
# )
#
# print(f"Below Example -> Placeholder below username: {field_below_username.get_attribute('placeholder')}")
# field_below_username.send_keys('secret_sauce')
# time.sleep(2)
# login_button.click()
# time.sleep(2)
#
# twitter_icon=driver.find_element(By.LINK_TEXT, "Twitter")
# facebook_icon=driver.find_element(locate_with(By.TAG_NAME, "a").to_right_of(twitter_icon))
# print(f"toRightOf Example -> Element to the right of Twitter icon has href: {facebook_icon.get_attribute('href')}")
#
# left_icon = driver.find_element(locate_with(By.TAG_NAME, "a").to_left_of(facebook_icon))
# print(f"toLeftOf Example -> Element to the left of Facebook icon has href: {left_icon.get_attribute('href')}")
#
# near_twitter = driver.find_elements(locate_with(By.TAG_NAME, "a").near(facebook_icon))
# for element in near_twitter:
#     print(f"Near Example -> Element near Facebook icon has href: {element.get_attribute('href')}")

time.sleep(3)

driver.quit()







