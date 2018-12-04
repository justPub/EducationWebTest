# coding=utf-8
import unittest
# 这里需要导入测试文件
import TestPage
import HTMLTestRunner
testunit=unittest.TestSuite()
# 将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(TestPage.HomeTestCase))
testunit.addTest(unittest.makeSuite(TestPage.CourseTestCase))
# 定义个报告存放路径，支持相对路径。
filename= "F:\\YK\\software\\PythonProjects\\EducationWebTest\\"+"result.html"
fp = open(filename,"wb")
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
# 执行测试用例
runner.run(testunit)