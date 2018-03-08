from selenium import webdriver
from selenium.webdriver.common.keys import Keys


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http:www.python.org')
    print(driver.title)
    print(driver.page_source)
    assert 'Python' in driver.title
    # elem = driver.find_element_by_name('q')
    elem = driver.find_element_by_id('id-search-field')
    elem.clear()
    elem.send_keys('pycon')
    elem.send_keys(Keys.RETURN)
    assert 'NO result found' not in driver.page_source
    # driver.close()
