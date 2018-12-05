# coding=utf-8
from time import sleep
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 判断元素是否存在
    def is_element_exist(self, xpath):
        s = self.driver.find_elements_by_xpath(xpath)
        if len(s) == 0:
            return False
        elif len(s) == 1:
            return True
        else:
            return False

    # 退出登录
    def log_out(self):
        s = self.driver.find_elements_by_xpath("/html/body/section[1]/header/div/div[1]/div/div[2]/dl/dd")
        flag = len(s)
        if flag == 1:
            print('woshicuode')
        self.driver.find_element_by_xpath(
            "/html/body/section[1]/header/div/div[1]/div/div[2]/dl/dd").click()  # 个人信息
        # self.driver.find_element_by_css_selector('.btn>a[2]').click() # 退出
        sleep(8)
        q = self.driver.find_elements_by_xpath("/html/body/section[1]/header/div/div[1]/div/div[2]/div/div/a[2]")
        bool = len(q)
        if bool == False:
            print('woshicuode')
        self.driver.find_element_by_css_selector('.fr').click() # 退出
        # self.driver.find_element_by_xpath(
        #     "/html/body/section[1]/header/div/div[1]/div/div[2]/div/div/a[2]").click()  # 退出

    # 登录
    def log_in(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("account_l").send_keys('yankai')
        self.driver.find_element_by_id("password_l").send_keys('abc123456' + Keys.RETURN)
        self.driver.find_element_by_id("jsLoginBtn").click()
        sleep(5)

    # 返回首页
    def return_homePage(self):
        self.driver.find_element_by_link_text("首页").click()

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
        sleep(5)

    # 点击登录
    def click_login(self):
        self.driver.find_element_by_id("jsLoginBtn").click()
        sleep(5)

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
        sleep(8)
        self.driver.find_element_by_xpath("/html/body/section[4]/div/div/div/div[2]/ul/li[1]/a/p/span").click()

    # 点击置顶按钮
    def click_sticky(self):
        self.driver.find_element_by_xpath("/html/body/section[5]/ul/li[2]").click()

    # 搜索栏中点击公开课
    def click_search_course(self):
        self.driver.find_element_by_xpath("//*[@id='jsSelectOption']").click() # 下拉菜单
        self.driver.find_element_by_xpath(
            "/html/body/section[1]/header/div/div[2]/div/div/div/ul/li[1]").click() # 公开课

    # 搜索栏中点击课程机构
    def click_search_insti(self):
        self.driver.find_element_by_xpath("//*[@id='jsSelectOption']").click() # 下拉菜单
        self.driver.find_element_by_xpath(
            "/html/body/section[1]/header/div/div[2]/div/div/div/ul/li[2]").click() # 课程机构

    # 搜索栏中点击授课老师
    def click_search_teacher(self):
        self.driver.find_element_by_xpath("//*[@id='jsSelectOption']").click() # 下拉菜单
        self.driver.find_element_by_xpath(
            "/html/body/section[1]/header/div/div[2]/div/div/div/ul/li[3]").click() # 授课老师

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

    # 点击某一个具体的课程【数据结构】
    def click_course_ds(self):
        self.driver.find_element_by_xpath(
            "/html/body/section[3]/div/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/a/h2").click() # 数据结构

    # 点击某一个热门推荐中的课程【软件工程】
    def click_course_se(self):
        self.driver.find_element_by_xpath(
            "/html/body/section[3]/div/div/div[2]/div[2]/dl[1]/dd/a/h2").click()  # 软件工程

    # 点击开始学习
    def click_start_learn(self):
        self.driver.find_element_by_xpath(
        "/html/body/section[3]/div/div/div/div[1]/div[2]/div[2]/div[2]/a").click()  # 开始学习

    # 点击收藏
    def click_collection(self):
        self.driver.find_element_by_xpath("//*[@id=\"jsLeftBtn\"]").click()  # 收藏

    # 点击授课机构中的收藏
    def click_insti_collection(self):
        self.driver.find_element_by_xpath("//*[@id=\"jsRightBtn\"]").click()  # 授课机构中的收藏

class TeacherPage(BasePage):
    # 点击授课教师
    def click_teacher(self):
        self.driver.find_element_by_link_text("授课教师").click()

    # 点击全部
    def click_all(self):
        self.driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div[1]/div/ul/li[1]/a").click()  # 全部

    # 点击人气
    def click_polpularity(self):
        self.driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div[1]/div/ul/li[2]/a").click()  # 人气

    # 点击查看详情【武剑洁】
    def click_details(self):
        self.driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div[1]/dl[1]/a").click()  # 查看详情

    # 点击讲师排行榜中的讲师【刘小峰】
    def click_ranklist_teacher(self):
        self.driver.find_element_by_xpath(
            '/html/body/section[3]/div/div[2]/dl[2]/dd/a/h1').click()  # 【刘小峰】

    # 点击详情中收藏
    def click_detail_collection(self):
        self.driver.find_element_by_xpath("//*[@id=\"jsLeftBtn\"]").click()  # 收藏

    # 点击详情中分享
    def click_detail_share(self):
        self.driver.find_element_by_xpath(
            "/html/body/section[3]/div/div[1]/div[1]/div/dl/dt/div[2]/span[2]/a").click()  # 分享

    # 点击详情中对应机构中的收藏
    def click_detail_insti_collection(self):
        self.driver.find_element_by_xpath("//*[@id=\"jsRightBtn\"]").click()  # 对应机构中的收藏

    # 点击详情中具体课程【武剑洁->数据结构】
    def click_detail_course(self):
        self.driver.find_element_by_xpath(
            '/html/body/section[3]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/a/h2').click() # 【武剑洁->数据结构】

    # 点击详情中讲师排行榜中的讲师【刘小峰】
    def click_detail_ranklist_teacher(self):
        self.driver.find_element_by_xpath(
            '/html/body/section[3]/div/div[2]/div[2]/div/div/dl[2]/dd/a/h1').click()  # 【刘小峰】

