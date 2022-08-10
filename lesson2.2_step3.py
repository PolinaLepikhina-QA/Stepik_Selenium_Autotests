from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element(By.ID, "num1")
	y_element = browser.find_element(By.ID, "num2")
	x = x_element.text
	y = y_element.text
	c = str(int(x) + int(y))

	select = Select(browser.find_element(By.ID, "dropdown"))
	select.select_by_value(value=c)
	
	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()