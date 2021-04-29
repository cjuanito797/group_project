import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ll(self):
        user = "pmizar"
        pwd = "Group2021"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        # Clicks "Log in" Button
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/form/div[3]/input").click()
        time.sleep(3)
        # Clicks "Products" Tab
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[4]/th/a").click()
        time.sleep(3)

        try:
            # Clicks "Add Product + " Tab
           elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/ul/li/a").click()

           assert True

        except NoSuchElementException:
            self.fail("Product add page did not appear when Product Add clicked")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()