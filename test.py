from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

driver.get("http://localhost:3000")
print(driver.title)
assert driver.title == 'Express'
