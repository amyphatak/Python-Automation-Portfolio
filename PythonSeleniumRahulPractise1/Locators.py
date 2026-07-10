import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CLASS_NAME, ".form-control.ng-touched.ng-dirty.ng-valid").send_keys("rahushettyacademy.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123")
driver.find_element(By.ID, "exampleCheck1").click()


#//tagname[@attribute='value']--. //input[@type='submit']----- XPATH
# CSS- tagname[attribute='value']
#CSS- #id, .classname
driver.find_element(By.CSS_SELECTOR, "inlineRadio1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message= driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "success" in message

#static dropdwons
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()




