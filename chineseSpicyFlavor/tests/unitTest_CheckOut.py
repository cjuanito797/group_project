import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ll(self):
        user = "mizarp"
        pwd = "Mypage20"

        driver = self.driver
        driver.maximize_window()

        driver.get("http://127.0.0.1:8000")

        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/a[2]").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[6]/a").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem = driver.find_element_by_xpath("/html/body/header/div/form/p[3]/input").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[4]/a[2]/input").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/a[2]").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/p/a[1]").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/a[1]/img").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()
        time.sleep(2)

        try:
            elem = driver.find_element_by_xpath("/html/body/div[3]/p/a[2]").click()
            time.sleep(2)
            elem = driver.find_element_by_xpath("/html/body/div[3]/form/div/input").click()
            time.sleep(2)
            elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[1]/input").click()
            time.sleep(2)

            assert True

        except NoSuchElementException:
            self.fail("My Borrowed does not appear when My Borrowed clicked")
            assert False

    time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
