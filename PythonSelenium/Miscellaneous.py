from selenium import webdriver

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollheight);")
driver.get_screenshot_as_file("screenshot.png")
