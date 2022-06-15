from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('C:\\Users\\nballa\\Desktop\\python\\test\\googlesearch\\chromedriver.exe')

driver.get('https://www.google.com')


search = driver.find_element_by_name('q')
search.send_keys('omnatuor.com')

time.sleep(2)
search_btn = driver.find_element_by_css_selector('input[type="submit"]')
search_btn.click()

try:
	main = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "search"))
	)
	link = main.find_elements(By.TAG_NAME, 'a')
	for i in link:
		print(i.text)
finally:
    driver.quit()

