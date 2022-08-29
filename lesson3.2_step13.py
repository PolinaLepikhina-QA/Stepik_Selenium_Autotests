from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestAbs(unittest.TestCase):
	def test_abs1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)

		input1 = browser.find_element(By.TAG_NAME, "input")
		input1.send_keys("Ivan")
		input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
		input2.send_keys("Petrov") 
		input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
		input3.send_keys("lepikhina_p@mail.ru")

		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()

		time.sleep(1)

		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		welcome_text = welcome_text_elt.text

		time.sleep(5)

		self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!", )

	def test_abs2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)

		input1 = browser.find_element(By.TAG_NAME, "input")
		input1.send_keys("Ivan")
		input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
		input2.send_keys("Petrov") 
		input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
		input3.send_keys("lepikhina_p@mail.ru")

		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()

		time.sleep(1)

		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		welcome_text = welcome_text_elt.text

		time.sleep(5)
		
		self.assertEqual("Congratulations! You have successfully registered!", "NoSuchElementException", )

if __name__ == "__main__":
	unittest.main()