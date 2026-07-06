from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#parent to child traverse --- //form/div[1]/input
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("hello@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("hello@1234")
driver.find_element(By.XPATH,"//button[@type='submit']").click()