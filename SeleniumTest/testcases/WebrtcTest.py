import unittest
from selenium import webdriver
from SeleniumTest.pages import searchPage


class WebrtcTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testwebrtc(self):
        driver = self.driver
        driver.get('https://www.justalkcloud.com/webrtc/')
        username = driver.find_element_by_id('uid')
        username.send_keys('test')
        driver.find_element_by_id('confid').send_keys('confid')
        driver.find_element_by_id('confpwd').send_keys('123456')
        driver.find_element_by_id('appKey').send_keys('97346350260773bfd2544096')
        driver.find_element_by_id('connect').click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
