# coding=utf-8
from time import sleep
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    # 从输入的username获取用户名
    def set_username(self, username):
        self.driver.find_element_by_id("account_l").send_keys(username)

    # 从输入的password获取密码
    def set_password(self, password):
        self.driver.find_element_by_id("password_l").send_keys(password + Keys.RETURN)

    # 点击登录按钮
    def click_loginButton(self):
        self.driver.find_element_by_link_text("登录").click()
        sleep(1)

    # 点击登录
    def click_login(self):
        self.driver.find_element_by_id("jsLoginBtn").click()
        sleep(3)

class HomePage(BasePage):
    # 点击更多课程
    def click_course_more(self):
        self.driver.find_element_by_link_text('查看更多课程 >').click()

    # 点击某一门课程【软件工程15人】
    def click_course_se(self):
        # self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div/div[2]/div[4]').click()
        self.driver.find_element_by_xpath("//*/a[contains(@href,'/course/detail/3/')]").click()
        # self.driver.find_element_by_css_selector('div.module1_5 box') .click()

    # 查看更多机构
    def click_insti_more(self):
        self.driver.find_element_by_link_text('查看更多机构 >').click()

    # 查看具体机构【华中科技大学】
    def click_insti_hust(self):
        self.driver.find_element_by_link_text('华中科技大学').click()

    # 滚动条定位在查看更多机构的上面
    def click_sticky(self):
        self.driver.find_element_by_xpath("/html/body/section[5]/ul/li[2]").click()

    # 返回首页
    def return_homePage(self):
        self.driver.find_element_by_link_text("首页").click()
class CoursePage(BasePage):
    # 点击公开课
    def click_course(self):
        self.driver.find_element_by_link_text("公开课").click()

    # 点击最新
    def click_sort_new(self):
        self.driver.find_element_by_link_text("最新").click()

    # 点击最热门
    def click_sort_hot(self):
        self.driver.find_element_by_link_text('最热门').click()

    # 点击参与人数
    def click_sort_num(self):
        self.driver.find_element_by_link_text('参与人数').click()

    # 返回首页
    def return_homePage(self):
        self.driver.find_element_by_link_text("首页").click()

