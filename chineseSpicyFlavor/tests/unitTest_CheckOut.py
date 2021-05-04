import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ll(self):
        user = "mizarp"
        pwd = "Mypage20"

        card = "4111 1111 1111 1111"
        cvv = "564"
        edate = "02/2023"

        driver = self.driver
        driver.maximize_window()

        driver.get("http://127.0.0.1:8000")

        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/a[2]").click()
        time.sleep(3)
        # Login
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[6]/a").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        # Log-in
        elem = driver.find_element_by_xpath("/html/body/header/div/form/p[3]/input").click()
        time.sleep(3)
        # Order
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/ul/li[5]/a").click()
        time.sleep(3)
        # Order Now
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/ul/li[5]/ul/li[1]/a").click()
        time.sleep(3)
        # Momo image
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[1]/a[1]/img").click()
        time.sleep(2)
        # Add to Cart
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/form/input[3]").click()
        time.sleep(2)
        # Continue shopping
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[3]/p/a[1]").click()
        time.sleep(2)
        # Chaumain
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/a[1]/img").click()
        time.sleep(2)
        # Add to Cart
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/form/input[3]").click()
        time.sleep(2)



        try:
            # Checkout
            elem = driver.find_element_by_xpath("/html/body/div[2]/div[3]/p/a[2]").click()
            time.sleep(2)
            # Select the address
            elem = driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/div/input").click()
            time.sleep(2)
            # Place order
            elem = driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/p[1]/input").click()
            time.sleep(2)


            assert True

        except NoSuchElementException:
            self.fail("Checkout does not appear when Checkout clicked")
            assert False

    time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
