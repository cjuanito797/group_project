import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ll(self):

        driver = self.driver
        driver.maximize_window()

        driver.get("http://127.0.0.1:8000")
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div/a[2]").click()

        time.sleep(5)
        try:
            elem = driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[4]/a").click()

            assert True

        except NoSuchElementException:
            self.fail("Order now does not appear when order now clicked")
            assert False

    time.sleep(2)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()