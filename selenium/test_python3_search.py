import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        # get()实质上是等待”onload”事件执行完毕
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_wenlizhe(self):
        driver = self.driver
        driver.get('https://www.wenlizhe.xyz')
        # self.assertIn('')
        user = driver.find_element_by_name('email')
        user.send_keys('administrator')
        pwd = driver.find_element_by_name('password')
        pwd.send_keys('administrator')
        submit = driver.find_element_by_xpath('//a[@class="btn btn-lg btn-default major"]').click()

    def tearDown(self):
        # self.driver.close()
        pass


if __name__ == "__main__":
    unittest.main()
