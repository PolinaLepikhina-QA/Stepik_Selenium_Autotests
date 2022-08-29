import time
from selenium.webdriver.common.by import By

link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_goods_has_add_to_basket_button(browser):
    browser.get(link)

    time.sleep(30) #sleep для проверки правильности инициализации браузера

    add_to_basket = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')

    assert add_to_basket, 'кнопка добавления товара отсутствует'