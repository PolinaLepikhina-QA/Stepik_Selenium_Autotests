import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

import pdb # for debugging purpose

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():
    message = ""
    urls = [
            "https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"
        ]
    @pytest.mark.parametrize('link', urls)
    def test_guest_should_open_link(self, browser, link):
        print("\nstart browser for test suite..")
        browser.get(link)
        browser.implicitly_wait(7)

        input1 = browser.find_element(By.CSS_SELECTOR, "textarea[id^=ember]")
        input1.send_keys(math.log(int(time.time())))

        button = browser.find_element(By.CLASS_NAME, "submit-submission")
        button.click()

        # breakpoint()
        expected_result = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text

        assert expected_result == "Correct!"

if __name__ == "__main__":
    pytest.main()
