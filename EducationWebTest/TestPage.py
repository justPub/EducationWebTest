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

    '''
        def setUp(self):
        global mutex_lock
        while mutex_lock == 0:
            print('开始')
            self.browser = webdriver.Firefox()
            self.browser.get('http://111.230.45.33:3000/')
            login_page = BasePage.LoginPage(self.browser)
            login_page.click_loginButton()
            login_page.set_username("yankai")
            login_page.set_password("abc123456")
            login_page.click_login()
            mutex_lock = 1

    def tearDown(self):
        while self.clock == 0:
            print('结束')
            self.browser.close()
            self.clock = 1
    '''

    # def test_B1_1(self):
    #     u'''test_B1_1'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)

    # def test_B1_2(self):
    #     u'''test_B1_2'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_course_more()
    #     self.assertIn('公开课列表 - 慕学在线网', self.browser.title)
    #
    # # TODU : test_B1_3 RETURN ERROR
    # def test_B1_3(self):
    #     u'''test_B1_3'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_course_se()
    #     self.assertIn('软件工程', self.browser.title)
    #
    # def test_B1_4(self):
    #     u'''test_B1_4'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_insti_more()
    #     self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)

    # def test_B1_5(self):
    #     u'''test_B1_5'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_insti_hust()
    #     self.assertIn('机构首页', self.browser.title)
    #
    # def test_B1_6(self):
    #     u'''test_B1_6'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_sticky()
    #     # TODU 判断置顶功能是否生效，判断条件缺失
    #
    # def test_B1_7_1_01(self):
    #     u'''test_B1_7_1_01'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_course()
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_1_02(self):
    #     u'''test_B1_7_1_02'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_course()
    #     self.browser.find_element_by_id('search_keywords').send_keys('公开课')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('公开课列表 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_1_03(self):
    #     u'''test_B1_7_1_03'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_course()
    #     self.browser.find_element_by_id('search_keywords').send_keys('数据结构')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.browser.find_element_by_xpath(
    #         "/html/body/section[3]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/a/h2") # 数据结构
    #
    # def test_B1_7_1_04(self):
    #     u'''test_B1_7_1_04'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_course()
    #     self.browser.find_element_by_id('search_keywords').send_keys('武剑洁')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('公开课列表 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_1_05(self):
    #     u'''test_B1_7_1_05'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_course()
    #     self.browser.find_element_by_id('search_keywords').send_keys('华中科技大学')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('公开课列表 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_1_06(self):
    #     u'''test_B1_7_1_06'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_course()
    #     self.browser.find_element_by_id('search_keywords').send_keys('~!@#$%^&*()_+|{}:"<>?.,;\'[]\=-')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('公开课列表 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_1_07(self):
    #     u'''test_B1_7_1_07'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_course()
    #     self.browser.find_element_by_id('search_keywords').send_keys('<input type="text" id="txt" value="测试"/>')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('公开课列表 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_2_01(self):
    #     u'''test_B1_7_2_01'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_insti()
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_2_02(self):
    #     u'''test_B1_7_2_02'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_insti()
    #     self.browser.find_element_by_id('search_keywords').send_keys('公开课')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.browser.find_element_by_xpath("/html/body/section[3]/div/div[2]/div")  # 我要学习
    #
    # def test_B1_7_2_03(self):
    #     u'''test_B1_7_2_03'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_insti()
    #     self.browser.find_element_by_id('search_keywords').send_keys('数据结构')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.browser.find_element_by_xpath("/html/body/section[3]/div/div[2]/div") # 我要学习
    #
    # def test_B1_7_2_04(self):
    #     u'''test_B1_7_2_04'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_insti()
    #     self.browser.find_element_by_id('search_keywords').send_keys('武剑洁')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.browser.find_element_by_xpath("/html/body/section[3]/div/div[2]/div")  # 我要学习
    #
    # def test_B1_7_2_05(self):
    #     u'''test_B1_7_2_05'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_insti()
    #     self.browser.find_element_by_id('search_keywords').send_keys('华中科技')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.browser.find_element_by_xpath(
    #         "/html/body/section[3]/div/div[1]/div[3]/div[1]/dl[1]/dd/div/a/h1") # 华中科技大学
    #
    # def test_B1_7_2_06(self):
    #     u'''test_B1_7_2_06'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_insti()
    #     self.browser.find_element_by_id('search_keywords').send_keys('~!@#$%^&*()_+|{}:"<>?.,;\'[]\=-')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.browser.find_element_by_xpath("/html/body/section[3]/div/div[2]/div")  # 我要学习
    #
    # def test_B1_7_2_07(self):
    #     u'''test_B1_7_2_07'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_insti()
    #     self.browser.find_element_by_id('search_keywords').send_keys('<input type="text" id="txt" value="测试"/>')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.browser.find_element_by_xpath("/html/body/section[3]/div/div[2]/div")  # 我要学习
    #
    # def test_B1_7_3_01(self):
    #     u'''test_B1_7_3_01'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_teacher()
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_3_02(self):
    #     u'''test_B1_7_3_02'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_teacher()
    #     self.browser.find_element_by_id('search_keywords').send_keys('公开课')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('课程讲师 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_3_03(self):
    #     u'''test_B1_7_3_03'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_teacher()
    #     self.browser.find_element_by_id('search_keywords').send_keys('数据结构')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('课程讲师 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_3_04(self):
    #     u'''test_B1_7_3_04'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_teacher()
    #     self.browser.find_element_by_id('search_keywords').send_keys('武剑洁')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.browser.find_element_by_xpath(
    #         "/html/body/section[3]/div/div[1]/div[1]/dl[1]/dd/a/h1")  # 武剑洁
    #
    # def test_B1_7_3_05(self):
    #     u'''test_B1_7_3_05'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_teacher()
    #     self.browser.find_element_by_id('search_keywords').send_keys('华中科技大学')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('课程讲师 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_3_06(self):
    #     u'''test_B1_7_3_06'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_teacher()
    #     self.browser.find_element_by_id('search_keywords').send_keys('~!@#$%^&*()_+|{}:"<>?.,;\'[]\=-')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('课程讲师 - 慕学在线网', self.browser.title)
    #
    # def test_B1_7_3_07(self):
    #     u'''test_B1_7_3_07'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     home_page.click_search_teacher()
    #     self.browser.find_element_by_id('search_keywords').send_keys('<input type="text" id="txt" value="测试"/>')
    #     self.browser.find_element_by_id('jsSearchBtn').click()
    #     self.assertIn('课程讲师 - 慕学在线网', self.browser.title)

class CourseTestCase(unittest.TestCase):

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

    '''
        def setUp(self):
        global mutex_lock
        while mutex_lock == 0:
            print('开始')
            self.browser = webdriver.Firefox()
            self.browser.get('http://111.230.45.33:3000/')
            login_page = BasePage.LoginPage(self.browser)
            login_page.click_loginButton()
            login_page.set_username("yankai")
            login_page.set_password("abc123456")
            login_page.click_login()
            mutex_lock = 1

    def tearDown(self):
        while self.clock == 0:
            print('结束')
            self.browser.close()
            self.clock = 1
    '''

    # def test_B2_1(self):
    #     u'''test_B2_1'''
    #     course_page = BasePage.CoursePage(self.browser)
    #     course_page.click_course()
    #     self.assertIn('公开课列表 - 慕学在线网', self.browser.title)
    #
    # def test_B2_2_1(self):
    #     u'''test_B2_2_1'''
    #     course_page = BasePage.CoursePage(self.browser)
    #     course_page.click_course()
    #     course_page.click_sort_new()
    #     course_page.click_course_ds()
    #     self.browser.find_element_by_xpath('/html/body/section[2]/div/div/ul/li[3]') # 课程详情

    # def test_B2_2_1_1_1(self):
    #     u'''test_B2_2_1_1_1'''
    #     course_page = BasePage.CoursePage(self.browser)
    #     course_page.log_out()
    #     course_page.click_course()
    #     course_page.click_sort_new()
    #     course_page.click_course_ds()
    #     course_page.click_start_learn()
    #     self.assertIn('慕学在线网登录', self.browser.title)
    #     course_page.log_in()
    #
    # def test_B2_2_1_1_2(self):
    #     u'''test_B2_2_1_1_2'''
    #     course_page = BasePage.CoursePage(self.browser)
    #     course_page.click_course()
    #     course_page.click_sort_new()
    #     course_page.click_course_ds()
    #     course_page.click_start_learn()
    #     # TODU : 判断条件需要增加具体课程

    def test_B2_2_1_2_1(self):
        u'''test_B2_2_1_2_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.log_out()
        course_page.click_course()
        course_page.click_sort_new()
        course_page.click_course_ds()
        course_page.click_collection()
        self.assertIn('慕学在线网登录', self.browser.title)
        course_page.log_in()

    def test_B2_2_1_2_2(self):
        u'''test_B2_2_1_2_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_new()
        course_page.click_course_ds()
        course_page.click_collection()
        self.assertIn('')

    def test_B2_2_1_2_3(self):
        u'''test_B2_2_1_2_3'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_new()
        course_page.click_course_ds()
        course_page.click_collection()



if __name__ == '__main__':
    unittest.main(verbosity=2)