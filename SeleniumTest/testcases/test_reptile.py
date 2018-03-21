import unittest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class TestReptile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cases(self):
        driver = self.driver
        driver.get('http://pythonscraping.com/pages/files/form.html')
        first_name_field = driver.find_element_by_name('firstname')
        last_name_field = driver.find_element_by_name('lastname')
        submit_button = driver.find_element_by_id('submit')

        actions = ActionChains(driver).click(first_name_field).send_keys('w')\
            .click(last_name_field).send_keys('lz')\
            .send_keys(Keys.RETURN)

        actions.perform()
        
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
