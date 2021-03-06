# coding=utf-8
import unittest
# 导入测试文件
import TestPage
import HTMLTestRunner
import threading

testunit=unittest.TestSuite()

# 创建线程数组
threads = []
# 创建线程t1，并添加到线程数组
t1 = threading.Thread(target=testunit.addTest,args=(unittest.makeSuite(TestPage.HomeTestCase),))
threads.append(t1)
# 创建线程t2，并添加到线程数组
t2 = threading.Thread(target=testunit.addTest,args=(unittest.makeSuite(TestPage.CourseTestCase),))
threads.append(t2)
# 创建线程t3，并添加到线程数组
t3 = threading.Thread(target=testunit.addTest,args=(unittest.makeSuite(TestPage.TeacherTestCase),))
threads.append(t3)
# 创建线程t4，并添加到线程数组
t4 = threading.Thread(target=testunit.addTest,args=(unittest.makeSuite(TestPage.InstiTestCase),))
threads.append(t4)
for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()

# 将测试用例加入到测试容器(套件)中
# testunit.addTest(unittest.makeSuite(TestPage.HomeTestCase))
# testunit.addTest(unittest.makeSuite(TestPage.CourseTestCase))
# testunit.addTest(unittest.makeSuite(TestPage.TeacherTestCase))
# testunit.addTest(unittest.makeSuite(TestPage.InstiTestCase))
# 定义个报告存放路径，支持相对路径。
filename= "C:\\Users\\k\\PycharmProjects\\EducationWebTest\\"+"result.html"
# filename= "F:\\YK\\software\\PythonProjects\\"+"result.html"
fp = open(filename,"wb")
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
# 执行测试用例
runner.run(testunit)
