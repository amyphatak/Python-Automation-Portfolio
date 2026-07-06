import time

from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(2)
driver.get("http://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_Url)
