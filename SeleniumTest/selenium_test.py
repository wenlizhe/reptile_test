import os
import unittest
from SeleniumTest.testcases.testSearchPage import TestSearchPage
from SeleniumTest.common import HTMLTestRunner


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestSearchPage('testSearch'))
    fp = open('./page_demo_Report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, title=u'my unit test', description=u'This is a report test')
    runner.run(testunit)
