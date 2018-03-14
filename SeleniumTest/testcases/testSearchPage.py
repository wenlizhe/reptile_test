import unittest
from selenium import webdriver
from SeleniumTest.pages import searchPage
from ..common.log import logger
from selenium.webdriver.common.by import By


# 百度搜索测试
class TestSearchPage(unittest.TestCase):

    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testSearch(self):
        driver = self.driver
        url = 'http://www.baidu.com'
        text = 'Python selenum'
        search_page = searchPage.SearchPage(driver, url)
        search_page.goto_baidu_home_page()
        search_page.input_search_text(text)
        search_page.click_search_btn()
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)
            print(link.text)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
