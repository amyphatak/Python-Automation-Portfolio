from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj= Service("C:\Users\Amruta\Downloads\chromedriver-win64 (1).exe")
#driver= webdriver.chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("http://www.python.org")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

