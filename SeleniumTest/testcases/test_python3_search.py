import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from SeleniumTest.common.log import Logger


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # def test_search_in_python_org(self):
    #     driver = self.driver
    #     # get()实质上是等待”onload”事件执行完毕
    #     driver.get("http://www.python.org")
    #     self.assertIn("Python", driver.title)
    #     elem = driver.find_element_by_name("q")
    #     elem.send_keys("pycon")
    #     elem.send_keys(Keys.RETURN)
    #     assert "No results found." not in driver.page_source

    def test_wenlizhe(self):
        driver = self.driver
        driver.get('http://www.wenlizhe.xyz')
        try:
            user = driver.find_element_by_name('email')
            user.send_keys('administrator')
            pwd = driver.find_element_by_name('password')
            pwd.send_keys('administrator')
            driver.find_element_by_xpath('//a[@class="btn btn-lg btn-default major"]').click()
            status = driver.find_element_by_link_text('任务状态')
            ActionChains(driver).move_to_element(status).perform()
            record = driver.find_element_by_link_text('任务记录')
            # self.assertIn('中国移动端到端测试平台', driver.title)
            time.sleep(3)
        except BaseException as e:
            print(str(e))

    def tearDown(self):
        # self.driver.close()
        pass


if __name__ == "__main__":
    # unittest.main()
    lo = Logger()
    logger = lo.get_logger()
    logger.debug('wlz')
