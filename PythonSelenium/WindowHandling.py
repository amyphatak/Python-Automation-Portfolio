import at
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PythonSelenium.WindowHandleAssignment import windowsOpened

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.XPATH,"//a[contains(text(),'Free Access to InterviewQues/ResumeAssistance/Mate']")
windowsOpened= driver.window_handles
driver.switch_to.window(windowsOpened[1])
message = driver.find_element(By.CLASS_NAME,".im-para.red").text
var= message.split(at)[1].strip("")[0]
driver.close()
driver.find_element(By.ID, "username").send_keys(var)
driver.find_element(By.ID, "password").send_keys(var)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)



