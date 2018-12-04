'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
'''
import BasePage
import unittest
from time import sleep
from selenium import webdriver
# mutex_lock = 0
class HomeTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("开始测试")
        cls.browser = webdriver.Firefox()
        cls.browser.get('http://111.230.45.33:3000/')
        login_page = BasePage.LoginPage(cls.browser)
        login_page.click_loginButton()
        login_page.set_username("yankai")
        login_page.set_password("abc123456")
        login_page.click_login()

    @classmethod
    def tearDownClass(cls):
        print("结束测试")
        cls.browser.quit()

    # def setUp(self):
    #     global mutex_lock
    #     while mutex_lock == 0:
    #         print('开始')
    #         self.browser = webdriver.Firefox()
    #         self.browser.get('http://111.230.45.33:3000/')
    #         login_page = BasePage.LoginPage(self.browser)
    #         login_page.click_loginButton()
    #         login_page.set_username("yankai")
    #         login_page.set_password("abc123456")
    #         login_page.click_login()
    #         mutex_lock = 1
    #
    # # def tearDown(self):
    # #     while self.clock == 0:
    # #         print('结束')
    # #         self.browser.close()
    # #         self.clock = 1

    # def test_B1_1(self):
    #     u'''test_B1_1'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)
    #
    # def test_B1_2(self):
    #     u'''test_B1_2'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_course_more()
    #     self.assertIn('公开课列表 - 慕学在线网', self.browser.title)
    #
    # def test_B1_3(self):
    #     u'''test_B1_3'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_course_se()
    #     self.assertTrue(self.browser.find_element_by_xpath("/html/body/section[2]/div/div/ul/li[3]"), '首页中点击课程出错')
    #
    # def test_B1_4(self):
    #     u'''test_B1_4'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_insti_more()
    #     self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)
    #
    # def test_B1_5(self):
    #     u'''test_B1_5'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_insti_hust()
    #     self.assertIn('机构首页', self.browser.title)

    def test_B1_6(self):
        u'''test_B1_6'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_sticky()
        # ActionChains(self.browser).move_to_element(result).perform()
        sleep(5)

    # # 登录之后对公开课模块进行测试
    # def testCourse(self):
    #     print('对公开课模块进行测试')
    #     self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)
    #     course_page = BasePage.CoursePage(self.browser)
    #     course_page.click_course()
    #     self.assertIn('公开课列表 - 慕学在线网', self.browser.title)
    #     course_page.click_sort_new()
    #     # TODU
    #     self.assertTrue(self.browser.find_element_by_css_selector(".active>a[href='?sort=']"),'当前sort不是最新')
    #     course_page.click_sort_hot()
    #     course_page.return_homePage()

if __name__ == '__main__':
    unittest.main(verbosity=2)