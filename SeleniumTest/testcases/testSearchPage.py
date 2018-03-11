import unittest
from selenium import webdriver
from SeleniumTest.pages import searchPage


# 百度搜索测试
class TestSearchPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testSearch(self):
        driver = self.driver
        url = 'http://www.baidu.com'
        text = 'test'
        search_page = searchPage.SearchPage(driver, url)
        search_page.goto_baidu_home_page()
        search_page.input_search_text(text)
        search_page.click_search_btn()
        
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
