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
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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
        sleep(5)


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

    def test_B1_1(self):
        u'''test_B1_1'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)

    def test_B1_2(self):
        u'''test_B1_2'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_course_more()
        self.assertIn('公开课列表 - 慕学在线网', self.browser.title)
    # Fail 页面跳转到错误界面，无法返回
    # def test_B1_3(self):
    #     u'''test_B1_3'''
    #     home_page = BasePage.HomePage(self.browser)
    #     home_page.return_homePage()
    #     # now_handle = self.browser.current_window_handle
    #     home_page.click_course_se()
    #     self.assertTrue(home_page.is_element_exist('/html/body/section[2]/div/div/ul/li[3]'), 'ERROR')

    def test_B1_4(self):
            u'''test_B1_4'''
            home_page = BasePage.HomePage(self.browser)
            home_page.return_homePage()
            home_page.click_insti_more()
            self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)

    def test_B1_5(self):
        u'''test_B1_5'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_insti_hust()
        self.assertIn('机构首页', self.browser.title)

    def test_B1_6(self):
        u'''test_B1_6'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_sticky()
        # TODU 判断置顶功能是否生效，判断条件缺失

    def test_B1_7_1_01(self):
        u'''test_B1_7_1_01'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_course()
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)

    def test_B1_7_1_02(self):
        u'''test_B1_7_1_02'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_course()
        self.browser.find_element_by_id('search_keywords').send_keys('公开课')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('公开课列表 - 慕学在线网', self.browser.title)

    def test_B1_7_1_03(self):
        u'''test_B1_7_1_03'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_course()
        self.browser.find_element_by_id('search_keywords').send_keys('数据结构')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertTrue(home_page.is_element_exist(
            '/html/body/section[3]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/a/h2'), 'ERROR') # 数据结构

    def test_B1_7_1_04(self):
        u'''test_B1_7_1_04'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_course()
        self.browser.find_element_by_id('search_keywords').send_keys('武剑洁')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('公开课列表 - 慕学在线网', self.browser.title)

    def test_B1_7_1_05(self):
        u'''test_B1_7_1_05'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_course()
        self.browser.find_element_by_id('search_keywords').send_keys('华中科技大学')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('公开课列表 - 慕学在线网', self.browser.title)

    def test_B1_7_1_06(self):
        u'''test_B1_7_1_06'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_course()
        self.browser.find_element_by_id('search_keywords').send_keys('~!@#$%^&*()_+|{}:"<>?.,;\'[]\=-')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('公开课列表 - 慕学在线网', self.browser.title)

    def test_B1_7_1_07(self):
        u'''test_B1_7_1_07'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_course()
        self.browser.find_element_by_id('search_keywords').send_keys('<input type="text" id="txt" value="测试"/>')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('公开课列表 - 慕学在线网', self.browser.title)

    def test_B1_7_2_01(self):
        u'''test_B1_7_2_01'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_insti()
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)

    def test_B1_7_2_02(self):
        u'''test_B1_7_2_02'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_insti()
        self.browser.find_element_by_id('search_keywords').send_keys('公开课')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertTrue(home_page.is_element_exist(
            '/html/body/section[3]/div/div[2]/div'), 'ERROR')  # 我要学习

    def test_B1_7_2_03(self):
        u'''test_B1_7_2_03'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_insti()
        self.browser.find_element_by_id('search_keywords').send_keys('数据结构')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertTrue(home_page.is_element_exist(
            '/html/body/section[3]/div/div[2]/div'), 'ERROR')  # 我要学习

    def test_B1_7_2_04(self):
        u'''test_B1_7_2_04'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_insti()
        self.browser.find_element_by_id('search_keywords').send_keys('武剑洁')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertTrue(home_page.is_element_exist(
            '/html/body/section[3]/div/div[2]/div'), 'ERROR')  # 我要学习

    def test_B1_7_2_05(self):
        u'''test_B1_7_2_05'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_insti()
        self.browser.find_element_by_id('search_keywords').send_keys('华中科技')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertTrue(home_page.is_element_exist(
            '/html/body/section[3]/div/div[1]/div[3]/div[1]/dl[1]/dd/div/a/h1'), 'ERROR')  # 华中科技大学

    def test_B1_7_2_06(self):
        u'''test_B1_7_2_06'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_insti()
        self.browser.find_element_by_id('search_keywords').send_keys('~!@#$%^&*()_+|{}:"<>?.,;\'[]\=-')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertTrue(home_page.is_element_exist(
            '/html/body/section[3]/div/div[2]/div'), 'ERROR')  # 我要学习

    def test_B1_7_2_07(self):
        u'''test_B1_7_2_07'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_insti()
        self.browser.find_element_by_id('search_keywords').send_keys('<input type="text" id="txt" value="测试"/>')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertTrue(home_page.is_element_exist(
            '/html/body/section[3]/div/div[2]/div'), 'ERROR')  # 我要学习

    def test_B1_7_3_01(self):
        u'''test_B1_7_3_01'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_teacher()
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)

    def test_B1_7_3_02(self):
        u'''test_B1_7_3_02'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_teacher()
        self.browser.find_element_by_id('search_keywords').send_keys('公开课')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('课程讲师 - 慕学在线网', self.browser.title)

    def test_B1_7_3_03(self):
        u'''test_B1_7_3_03'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_teacher()
        self.browser.find_element_by_id('search_keywords').send_keys('数据结构')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('课程讲师 - 慕学在线网', self.browser.title)

    def test_B1_7_3_04(self):
        u'''test_B1_7_3_04'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_teacher()
        self.browser.find_element_by_id('search_keywords').send_keys('武剑洁')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertTrue(home_page.is_element_exist(
            '/html/body/section[3]/div/div[1]/div[1]/dl[1]/dd/a/h1'), 'ERROR')  # 武剑洁

    def test_B1_7_3_05(self):
        u'''test_B1_7_3_05'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_teacher()
        self.browser.find_element_by_id('search_keywords').send_keys('华中科技大学')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('课程讲师 - 慕学在线网', self.browser.title)

    def test_B1_7_3_06(self):
        u'''test_B1_7_3_06'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_teacher()
        self.browser.find_element_by_id('search_keywords').send_keys('~!@#$%^&*()_+|{}:"<>?.,;\'[]\=-')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('课程讲师 - 慕学在线网', self.browser.title)

    def test_B1_7_3_07(self):
        u'''test_B1_7_3_07'''
        home_page = BasePage.HomePage(self.browser)
        home_page.return_homePage()
        home_page.click_search_teacher()
        self.browser.find_element_by_id('search_keywords').send_keys('<input type="text" id="txt" value="测试"/>')
        self.browser.find_element_by_id('jsSearchBtn').click()
        self.assertIn('课程讲师 - 慕学在线网', self.browser.title)

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

    def test_B2_1(self):
        u'''test_B2_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        self.assertIn('公开课列表 - 慕学在线网', self.browser.title)

    def test_B2_2_1(self):
        u'''test_B2_2_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_new()
        course_page.click_course_ds()
        self.assertTrue(course_page.is_element_exist('/html/body/section[2]/div/div/ul/li[3]'), 'ERROR')

    def test_B2_2_1_1_1(self):
        u'''test_B2_2_1_1_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.log_out()
        course_page.click_course()
        course_page.click_sort_new()
        course_page.click_course_ds()
        course_page.click_start_learn()
        self.assertIn('慕学在线网登录', self.browser.title)
        course_page.log_in()

    def test_B2_2_1_1_2(self):
        u'''test_B2_2_1_1_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_new()
        course_page.click_course_ds()
        # course_page.click_start_learn()
        # TODU : 判断条件需要增加具体课程

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
        self.assertTrue(self.browser.find_element_by_id('jsLeftBtn').text == '已收藏', 'ERROR')

    def test_B2_2_1_2_3(self):
        u'''test_B2_2_1_2_3'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_new()
        course_page.click_course_ds()
        course_page.click_collection()
        self.assertTrue(self.browser.find_element_by_id('jsLeftBtn').text == '收藏', 'ERROR')

    def test_B2_2_1_3_1(self):
        u'''test_B2_2_1_3_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.log_out()
        course_page.click_course()
        course_page.click_sort_new()
        course_page.click_course_ds()
        course_page.click_insti_collection()
        self.assertIn('慕学在线网登录', self.browser.title)
        course_page.log_in()

    def test_B2_2_1_3_2(self):
        u'''test_B2_2_1_3_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_new()
        course_page.click_course_ds()
        course_page.click_insti_collection()
        self.assertTrue(self.browser.find_element_by_id('jsRightBtn').text == '已收藏', 'ERROR')

    def test_B2_2_1_3_3(self):
        u'''test_B2_2_1_3_3'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_new()
        course_page.click_course_ds()
        course_page.click_insti_collection()
        self.assertTrue(self.browser.find_element_by_id('jsRightBtn').text == '收藏', 'ERROR')

    def test_B2_2_2(self):
        u'''test_B2_2_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_new()
        course_page.click_course_se()
        self.assertTrue(course_page.is_element_exist('/html/body/section[2]/div/div/ul/li[3]'), 'ERROR')

    def test_B2_3_1(self):
        u'''test_B2_3_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_hot()
        course_page.click_course_ds()
        self.assertTrue(course_page.is_element_exist('/html/body/section[2]/div/div/ul/li[3]'), 'ERROR')

    def test_B2_3_1_1_1(self):
        u'''test_B2_3_1_1_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.log_out()
        course_page.click_course()
        course_page.click_sort_hot()
        course_page.click_course_ds()
        course_page.click_start_learn()
        self.assertIn('慕学在线网登录', self.browser.title)
        course_page.log_in()

    def test_B2_3_1_1_2(self):
        u'''test_B2_3_1_1_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_hot()
        course_page.click_course_ds()
        # course_page.click_start_learn()
        # TODU : 判断条件需要增加具体课程

    def test_B2_3_1_2_1(self):
        u'''test_B2_3_1_2_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.log_out()
        course_page.click_course()
        course_page.click_sort_hot()
        course_page.click_course_ds()
        course_page.click_collection()
        self.assertIn('慕学在线网登录', self.browser.title)
        course_page.log_in()

    def test_B2_3_1_2_2(self):
        u'''test_B2_3_1_2_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_hot()
        course_page.click_course_ds()
        course_page.click_collection()
        self.assertTrue(self.browser.find_element_by_id('jsLeftBtn').text == '已收藏', 'ERROR')

    def test_B2_3_1_2_3(self):
        u'''test_B2_3_1_2_3'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_hot()
        course_page.click_course_ds()
        course_page.click_collection()
        self.assertTrue(self.browser.find_element_by_id('jsLeftBtn').text == '收藏', 'ERROR')

    def test_B2_3_1_3_1(self):
        u'''test_B2_3_1_3_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.log_out()
        course_page.click_course()
        course_page.click_sort_hot()
        course_page.click_course_ds()
        course_page.click_insti_collection()
        self.assertIn('慕学在线网登录', self.browser.title)
        course_page.log_in()

    def test_B2_3_1_3_2(self):
        u'''test_B2_3_1_3_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_hot()
        course_page.click_course_ds()
        course_page.click_insti_collection()
        self.assertTrue(self.browser.find_element_by_id('jsRightBtn').text == '已收藏', 'ERROR')

    def test_B2_3_1_3_3(self):
        u'''test_B2_3_1_3_3'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_hot()
        course_page.click_course_ds()
        course_page.click_insti_collection()
        self.assertTrue(self.browser.find_element_by_id('jsRightBtn').text == '收藏', 'ERROR')

    def test_B2_3_2(self):
        u'''test_B2_3_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_hot()
        course_page.click_course_se()
        self.assertTrue(course_page.is_element_exist('/html/body/section[2]/div/div/ul/li[3]'), 'ERROR')

    def test_B2_4_1(self):
        u'''test_B2_4_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_num()
        course_page.click_course_ds()
        self.assertTrue(course_page.is_element_exist('/html/body/section[2]/div/div/ul/li[3]'), 'ERROR')

    def test_B2_4_1_1_1(self):
        u'''test_B2_4_1_1_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.log_out()
        course_page.click_course()
        course_page.click_sort_num()
        course_page.click_course_ds()
        course_page.click_start_learn()
        self.assertIn('慕学在线网登录', self.browser.title)
        course_page.log_in()

    def test_B2_4_1_1_2(self):
        u'''test_B2_4_1_1_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_num()
        course_page.click_course_ds()
        # course_page.click_start_learn()
        # TODU : 判断条件需要增加具体课程

    def test_B2_4_1_2_1(self):
        u'''test_B2_4_1_2_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.log_out()
        course_page.click_course()
        course_page.click_sort_num()
        course_page.click_course_ds()
        course_page.click_collection()
        self.assertIn('慕学在线网登录', self.browser.title)
        course_page.log_in()

    def test_B2_4_1_2_2(self):
        u'''test_B2_4_1_2_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_num()
        course_page.click_course_ds()
        course_page.click_collection()
        self.assertTrue(self.browser.find_element_by_id('jsLeftBtn').text == '已收藏', 'ERROR')

    def test_B2_4_1_2_3(self):
        u'''test_B2_4_1_2_3'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_num()
        course_page.click_course_ds()
        course_page.click_collection()
        self.assertTrue(self.browser.find_element_by_id('jsLeftBtn').text == '收藏', 'ERROR')

    def test_B2_4_1_3_1(self):
        u'''test_B2_4_1_3_1'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.log_out()
        course_page.click_course()
        course_page.click_sort_num()
        course_page.click_course_ds()
        course_page.click_insti_collection()
        self.assertIn('慕学在线网登录', self.browser.title)
        course_page.log_in()

    def test_B2_4_1_3_2(self):
        u'''test_B2_4_1_3_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_num()
        course_page.click_course_ds()
        course_page.click_insti_collection()
        self.assertTrue(self.browser.find_element_by_id('jsRightBtn').text == '已收藏', 'ERROR')

    def test_B2_4_1_3_3(self):
        u'''test_B2_4_1_3_3'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_num()
        course_page.click_course_ds()
        course_page.click_insti_collection()
        self.assertTrue(self.browser.find_element_by_id('jsRightBtn').text == '收藏', 'ERROR')

    def test_B2_4_2(self):
        u'''test_B2_4_2'''
        course_page = BasePage.CoursePage(self.browser)
        course_page.click_course()
        course_page.click_sort_num()
        course_page.click_course_se()
        self.assertTrue(course_page.is_element_exist('/html/body/section[2]/div/div/ul/li[3]'), 'ERROR')

class TeacherTestCase(unittest.TestCase):

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

    def test_B3_1(self):
        u'''test_B3_1'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        self.assertIn('课程讲师 - 慕学在线网', self.browser.title)

    def test_B3_2_1_1(self):
        u'''test_B3_2_1_1'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.log_out()
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_details()
        self.assertIn('讲师详情 - 慕学在线网', self.browser.title)
        self.browser.find_element_by_link_text("登录").click()
        teacher_page.log_in()

    def test_B3_2_1_2(self):
        u'''test_B3_2_1_2'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_details()
        self.assertIn('讲师详情 - 慕学在线网', self.browser.title)

    def test_B3_2_1_1_1(self):
        u'''test_B3_2_1_1_1'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.log_out()
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_details()
        teacher_page.click_detail_collection()
        self.assertIn('慕学在线网登录', self.browser.title)
        if self.browser.title != '慕学在线网登录':
            self.browser.find_element_by_link_text("登录").click()
        teacher_page.log_in()

    def test_B3_2_1_1_2(self):
        u'''test_B3_2_1_1_2'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_details()
        if teacher_page.judge_detail_collection():
            teacher_page.click_detail_collection()
        self.assertTrue(self.browser.find_element_by_id('jsLeftBtn').text == '已收藏', 'ERROR')

    def test_B3_2_1_1_3(self):
        u'''test_B3_2_1_1_3'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_details()
        if not teacher_page.judge_detail_collection():
            teacher_page.click_detail_collection()
        self.assertTrue(self.browser.find_element_by_id('jsLeftBtn').text == '收藏', 'ERROR')

    def test_B3_2_1_2_1(self):
        u'''test_B3_2_1_2_1'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_details()
        teacher_page.click_detail_share()
        self.assertTrue(self.browser.find_element_by_xpath(
            "/html/body/section[3]/div/div[1]/div[1]/div/dl/dt/div[2]/span[2]/a").text == '已分享', 'ERROR')

    def test_B3_2_1_3_1(self):
        u'''test_B3_2_1_3_1'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.log_out()
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_details()
        teacher_page.click_detail_insti_collection()
        self.assertIn('慕学在线网登录', self.browser.title)
        teacher_page.log_in()

    def test_B3_2_1_3_2(self):
        u'''test_B3_2_1_3_2'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_details()
        if teacher_page.judge_detail_insti_collection():
            teacher_page.click_detail_insti_collection()
        self.assertTrue(self.browser.find_element_by_id('jsRightBtn').text == '已收藏', 'ERROR')

    def test_B3_2_1_3_3(self):
        u'''test_B3_2_1_3_3'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_details()
        if not teacher_page.judge_detail_insti_collection():
            teacher_page.click_detail_insti_collection()
        self.assertTrue(self.browser.find_element_by_id('jsRightBtn').text == '收藏', 'ERROR')

    def test_B3_2_1_4(self):
        u'''test_B3_2_1_4'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_details()
        teacher_page.click_detail_course()
        self.assertIn('课程详情页 - 慕学在线网', self.browser.title)

    def test_B3_2_1_5(self):
        u'''test_B3_2_1_5'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_details()
        teacher_page.click_detail_ranklist_teacher()
        self.assertTrue(self.browser.find_element_by_xpath(
            "/html/body/section[3]/div/div[1]/div[1]/div/dl/dd/a/h1").text == '刘小峰金牌讲师', 'ERROR')

    def test_B3_2_2(self):
        u'''test_B3_2_2'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_all()
        teacher_page.click_ranklist_teacher()
        self.assertTrue(self.browser.find_element_by_xpath(
            "/html/body/section[3]/div/div[1]/div[1]/div/dl/dd/a/h1").text == '刘小峰金牌讲师', 'ERROR')

    def test_B3_3_1_1(self):
        u'''test_B3_3_1_1'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.log_out()
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_details()
        self.assertIn('讲师详情 - 慕学在线网', self.browser.title)
        self.browser.find_element_by_link_text("登录").click()
        teacher_page.log_in()

    def test_B3_3_1_2(self):
        u'''test_B3_3_1_2'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_details()
        self.assertIn('讲师详情 - 慕学在线网', self.browser.title)

    def test_B3_3_1_1_1(self):
        u'''test_B3_3_1_1_1'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.log_out()
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_details()
        teacher_page.click_detail_collection()
        self.assertIn('慕学在线网登录', self.browser.title)
        if self.browser.title != '慕学在线网登录':
            self.browser.find_element_by_link_text("登录").click()
        teacher_page.log_in()

    def test_B3_3_1_1_2(self):
        u'''test_B3_3_1_1_2'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_details()
        if teacher_page.judge_detail_collection():
            teacher_page.click_detail_collection()
        self.assertTrue(self.browser.find_element_by_id('jsLeftBtn').text == '已收藏', 'ERROR')

    def test_B3_3_1_1_3(self):
        u'''test_B3_3_1_1_3'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_details()
        if not teacher_page.judge_detail_collection():
            teacher_page.click_detail_collection()
        self.assertTrue(self.browser.find_element_by_id('jsLeftBtn').text == '收藏', 'ERROR')

    def test_B3_3_1_2_1(self):
        u'''test_B3_3_1_2_1'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_details()
        teacher_page.click_detail_share()
        self.assertTrue(self.browser.find_element_by_xpath(
            "/html/body/section[3]/div/div[1]/div[1]/div/dl/dt/div[2]/span[2]/a").text == '已分享', 'ERROR')

    def test_B3_3_1_3_1(self):
        u'''test_B3_3_1_3_1'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.log_out()
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_details()
        teacher_page.click_detail_insti_collection()
        self.assertIn('慕学在线网登录', self.browser.title)
        teacher_page.log_in()

    def test_B3_3_1_3_2(self):
        u'''test_B3_3_1_3_2'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_details()
        if teacher_page.judge_detail_insti_collection():
            teacher_page.click_detail_insti_collection()
        self.assertTrue(self.browser.find_element_by_id('jsRightBtn').text == '已收藏', 'ERROR')

    def test_B3_3_1_3_3(self):
        u'''test_B3_3_1_3_3'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_details()
        if not teacher_page.judge_detail_insti_collection():
            teacher_page.click_detail_insti_collection()
        self.assertTrue(self.browser.find_element_by_id('jsRightBtn').text == '收藏', 'ERROR')

    def test_B3_3_1_4(self):
        u'''test_B3_3_1_4'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_details()
        teacher_page.click_detail_course()
        self.assertIn('课程详情页 - 慕学在线网', self.browser.title)

    def test_B3_3_1_5(self):
        u'''test_B3_3_1_5'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_details()
        teacher_page.click_detail_ranklist_teacher()
        self.assertTrue(self.browser.find_element_by_xpath(
            "/html/body/section[3]/div/div[1]/div[1]/div/dl/dd/a/h1").text == '刘小峰金牌讲师', 'ERROR')

    def test_B3_3_2(self):
        u'''test_B3_3_2'''
        teacher_page = BasePage.TeacherPage(self.browser)
        teacher_page.click_teacher()
        teacher_page.click_polpularity()
        teacher_page.click_ranklist_teacher()
        self.assertTrue(self.browser.find_element_by_xpath(
            "/html/body/section[3]/div/div[1]/div[1]/div/dl/dd/a/h1").text == '刘小峰金牌讲师', 'ERROR')

class InstiTestCase(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("开始测试")
    #     cls.browser = webdriver.Firefox()
    #     cls.browser.get('http://111.230.45.33:3000/')
    #     login_page = BasePage.LoginPage(cls.browser)
    #     login_page.click_loginButton()
    #     login_page.set_username("yankai")
    #     login_page.set_password("abc123456")
    #     login_page.click_login()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("结束测试")
    #     cls.browser.quit()


    def setUp(self):
        print('开始')
        self.browser = webdriver.Firefox()
        self.browser.get('http://111.230.45.33:3000/')
        login_page = BasePage.LoginPage(self.browser)
        login_page.click_loginButton()
        login_page.set_username("yankai")
        login_page.set_password("abc123456")
        login_page.click_login()

    def tearDown(self):
        print('结束')
        self.browser.close()


    def test_B4_1(self):
        u'''test_B4_1'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        self.assertIn('课程机构列表 - 慕学在线网', self.browser.title)

    def test_B4_2_1_1(self):
        u'''test_B4_2_1_1'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_class_all()
        insti_page.click_province_all()
        insti_page.click_list_all()
        insti_page.click_contact()
        self.assertIn('机构首页', self.browser.title)

    def test_B4_2_1_2(self):
        u'''test_B4_2_1_2'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_class_all()
        insti_page.click_province_all()
        insti_page.click_list_learn()
        insti_page.click_contact()
        self.assertIn('机构首页', self.browser.title)

    def test_B4_2_1_3(self):
        u'''test_B4_2_1_3'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_class_all()
        insti_page.click_province_all()
        insti_page.click_list_course()
        insti_page.click_contact()
        self.assertIn('机构首页', self.browser.title)

    def test_B4_3_1_1(self):
        u'''test_B4_3_1_1'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name()
        insti_page.click_want_phone()
        insti_page.click_want_course()
        insti_page.click_want_contact()
        sleep(3)
        self.assertTrue(self.browser.find_element_by_id('jsCompanyTips').text == '添加出错', 'ERROR')

    def test_B4_3_1_2(self):
        u'''test_B4_3_1_2'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('tom')
        insti_page.click_want_phone()
        insti_page.click_want_course()
        insti_page.click_want_contact()
        sleep(3)
        self.assertTrue(self.browser.find_element_by_id('jsCompanyTips').text == '添加出错', 'ERROR')

    def test_B4_3_1_3(self):
        u'''test_B4_3_1_3'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name()
        insti_page.click_want_phone('13904367258')
        insti_page.click_want_course()
        insti_page.click_want_contact()
        sleep(3)
        self.assertTrue(self.browser.find_element_by_id('jsCompanyTips').text == '添加出错', 'ERROR')

    def test_B4_3_1_4(self):
        u'''test_B4_3_1_4'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name()
        insti_page.click_want_phone()
        insti_page.click_want_course('数据结构')
        insti_page.click_want_contact()
        sleep(3)
        self.assertTrue(self.browser.find_element_by_id('jsCompanyTips').text == '添加出错', 'ERROR')

    def test_B4_3_1_5(self):
        u'''test_B4_3_1_5'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('tom')
        insti_page.click_want_phone('13904367258')
        insti_page.click_want_course('数据结构')
        insti_page.click_want_contact()
        s = insti_page.click_alert()
        self.assertTrue(s == 1, 'ERROR')

    def test_B4_3_1_6(self):
        u'''test_B4_3_1_6'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('闫')
        insti_page.click_want_phone('13904367258')
        insti_page.click_want_course('数据结构')
        insti_page.click_want_contact()
        s = insti_page.click_alert()
        self.assertTrue(s == 1, 'ERROR')

    def test_B4_3_1_7(self):
        u'''test_B4_3_1_7'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('闫tom')
        insti_page.click_want_phone('13904367258')
        insti_page.click_want_course('数据结构')
        insti_page.click_want_contact()
        s = insti_page.click_alert()
        self.assertTrue(s == 1, 'ERROR')

    def test_B4_3_1_8(self):
        u'''test_B4_3_1_8'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('~!@#$%^&*()_+|{}:"<>?.,;\'[]\=-')
        insti_page.click_want_phone('13904367258')
        insti_page.click_want_course('数据结构')
        insti_page.click_want_contact()
        sleep(3)
        self.assertTrue(self.browser.find_element_by_id('jsCompanyTips').text == '添加出错', 'ERROR')

    def test_B4_3_1_9(self):
        u'''test_B4_3_1_9'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('闫')
        insti_page.click_want_phone('139043672581')
        insti_page.click_want_course('数据结构')
        insti_page.click_want_contact()
        sleep(3)
        self.assertTrue(self.browser.find_element_by_id('jsCompanyTips').text == '添加出错', 'ERROR')

    def test_B4_3_1_10(self):
        u'''test_B4_3_1_10'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('闫')
        insti_page.click_want_phone('12345678911')
        insti_page.click_want_course('数据结构')
        insti_page.click_want_contact()
        sleep(3)
        self.assertTrue(self.browser.find_element_by_id('jsCompanyTips').text == '添加出错', 'ERROR')

    def test_B4_3_1_11(self):
        u'''test_B4_3_1_11'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('闫')
        insti_page.click_want_phone('1234567')
        insti_page.click_want_course('数据结构')
        insti_page.click_want_contact()
        sleep(3)
        self.assertTrue(self.browser.find_element_by_id('jsCompanyTips').text == '添加出错', 'ERROR')

    def test_B4_3_1_12(self):
        u'''test_B4_3_1_12'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('闫')
        insti_page.click_want_phone('139@436！258')
        insti_page.click_want_course('数据结构')
        insti_page.click_want_contact()
        sleep(3)
        self.assertTrue(self.browser.find_element_by_id('jsCompanyTips').text == '添加出错', 'ERROR')

    def test_B4_3_1_13(self):
        u'''test_B4_3_1_13'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('闫')
        insti_page.click_want_phone('139abcd7258')
        insti_page.click_want_course('数据结构')
        insti_page.click_want_contact()
        sleep(3)
        self.assertTrue(self.browser.find_element_by_id('jsCompanyTips').text == '添加出错', 'ERROR')

    def test_B4_3_1_14(self):
        u'''test_B4_3_1_14'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('闫')
        insti_page.click_want_phone('1390436  58')
        insti_page.click_want_course('数据结构')
        insti_page.click_want_contact()
        sleep(3)
        self.assertTrue(self.browser.find_element_by_id('jsCompanyTips').text == '添加出错', 'ERROR')

    def test_B4_3_1_15(self):
        u'''test_B4_3_1_15'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('闫')
        insti_page.click_want_phone('13904367258')
        insti_page.click_want_course('复变函数')
        insti_page.click_want_contact()
        s = insti_page.click_alert()
        self.assertTrue(s == 1, 'ERROR')

    def test_B4_3_1_16(self):
        u'''test_B4_3_1_16'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_want_name('闫')
        insti_page.click_want_phone('13904367258')
        insti_page.click_want_course('~!@#$%^&*()_+|{}:"<>?.,;\'[]\=-')
        insti_page.click_want_contact()
        s = insti_page.click_alert()
        self.assertTrue(s == 1, 'ERROR')

    def test_B4_4(self):
        u'''test_B4_4'''
        insti_page = BasePage.InstiPage(self.browser)
        insti_page.click_insti()
        insti_page.click_ranklist_insti()
        self.assertIn('机构首页', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)