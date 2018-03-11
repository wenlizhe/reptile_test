from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from SeleniumTest.pages.BasePage import Page


# 百度搜索page
class SearchPage(Page):
    # 元素集

    # 搜索输入框
    search_input = (By.ID, u'kw')
    # 百度一下 按钮
    search_button = (By.ID, u'su')

    def __init__(self, driver, base_url="http://www.baidu.com"):
        Page.__init__(self, driver, base_url)
         
    def goto_baidu_home_page(self):
        self.driver.get(self.base_url)

    def input_search_text(self, text='test'):
        print('input keyword: test')
        self.input_text(self.search_input, text)

    def click_search_btn(self):
        print("点击 百度一下  按钮")
        self.click(self.search_button)
