from selenium import webdriver
from selenium.webdriver.common.by import By

browserSortedVeggies = []
driver= webdriver.chrome()

#click on column header
# collect all veggies in one list-- browser sortted vegiie list
#sort this veggi list =>newsorted list
# browser sorted list == new list

driver.find_element(By.Xpath,"//span[text()='Veg/fruit name']").click()
veggieWebelements= driver.find_elements(By.XPATH,"//tr/td[1]")
for element in veggieWebelements:
    browserSortedVeggies.append(element.text)

originalBrowserSortedlist = browserSortedVeggies.copy()
browserSortedVeggies.sort()
assert browserSortedVeggies== originalBrowserSortedlist