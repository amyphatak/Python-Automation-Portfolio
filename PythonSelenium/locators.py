import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12344")
checkbox = driver.find_element(By.ID, "exampleCheck1")
driver.execute_script("arguments[0].click();", checkbox)

#//input[@type='submit']
#css - //input[name='name']
driver.find_element(By.NAME,"//input[name='name']").send_keys("rahulshetty")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "success" in message


