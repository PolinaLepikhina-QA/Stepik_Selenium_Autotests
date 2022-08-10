from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
	link = "http://SunInJuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element(By.ID, "input_value")
	def calc(x):
	  return str(math.log(abs(12*math.sin(int(x)))))
	x = x_element.text
	y = calc(x)

	button = browser.find_element(By.TAG_NAME, "button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()

	input1 = browser.find_element(By.ID, "answer")
	input1.send_keys(y)

	option1 = browser.find_element(By.ID, "robotCheckbox")
	option1.click()
	option2 = browser.find_element(By.ID, "robotsRule")
	option2.click()

	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()