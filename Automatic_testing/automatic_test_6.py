# 自动化测试必备框架 unittest 单元测试框架实战
#    1.什么是单元测试 unittest
#      简介：讲解什么是单元测试，使用场景和unittest介绍
#      1.单元测试：
#        是指对软件的最小可测试单元进行检查和验证，对于单元测试中单元的含义
#        要根据实际情况去判定其具体含义，如C语言中单元指一个函数
#        Java单元指一个类，图形化的软件中可以指一个窗口或一个菜单等
#        总的来说单元就是人为规定的最小的被测功能模块。单元测试是软件开发中
#        要进行的最低级别的测试活动

#      2.unittest测试框架是python的单元测试框架
#        官网：https://docs.python.org/2/library/unittest.html

#      3.unitest = TestCase + TestResult 执行用例+结果
#
#    2.单元测试框架unittest入门
#      简介：讲解单元测试框架unittest的使用
#      1.用import语句引入unittest模块
#      2.测试的类都继承于TestCase类
#      3.setup()测试前的初始化工作；tearDown()测试后的清楚工作
#      注意：
#          1.所有类中方法的入参为self，定义方法的变量也要“self.变量”
#          2.定义测试用例，已“test”开头命名的方法，方法的入参为self
#          3.unitest.main()方法会搜索该模块下所有以test开头的测试用例方法并自动执行他
#          4.自己写的py文件不能用unittest.py命名，不然会找不到TestCase
#      成功输出 . 失败输出F
import unittest
class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.name = '小D课堂'
        self.age = 28
# 用例名称
    def test_name(self):
        # 判断名字是否相同
        self.assertEqual(self.name,'小F课堂',msg = '名字不对')
# 用例名称
    def test_age(self):
        # 判断年龄是否一致
        self.assertEqual(self.age,28,msg='年龄正确')
# 用例名称
    def test_isupper(self):
        # 判断括号里面的内容是否为错，若是则返回点(.),若不是，则返回msg
        self.assertFalse('xdclass'.isupper(),msg='不是大写')
    def tearDown(self):
        print('测试结束')
# 调用测试用例脚本
if __name__ == '__main__':
    unittest.main()

#    3.测试套件TestSuite介绍
#         简介:讲解测试套件TestSuite的基本介绍和使用场景
#         需求:
#             1.利用unittest执行流程测试而非单元测试
#             2.控制unittest的执行顺序
#      1.unittest.TestSuite()类来表示一个测试用例集
#        1.用来确定测试用例的顺序,哪个先执行,哪个后执行
#        2.如果一个class中有四个test开头的方法,则加载到suite中时则有四个测试用例
#        3.由一个TestLoder加载TestCase到TestSuite
#        4.verbosity参数可以控制执行结果的输出,0 是简单报告,1 是一般报告,2 是详细报告
#      2.TextTestRunner() 文本测试用例运行器
#      3.run()方法是运行测试套件的测试用例，入参为suite测试套件
import unittest
class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.name = '小D课堂'
        self.age = 28
    def tearDown(self):
        print('测试结束')
# 用例名称
    def test_name(self):
        # 判断名字是否相同
        self.assertEqual(self.name,'小F课堂',msg = '名字不对')
# 用例名称
    def test_age(self):
        # 判断年龄是否一致
        self.assertEqual(self.age,28,msg='年龄正确')
# 用例名称
    def test_isupper(self):
        # 判断括号里面的内容是否为错，若是则返回点(.),若不是，则返回msg
        self.assertFalse('xdclass'.upper(),msg='不是大写')
    # 调用TestSuite控制用例顺序
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UserTestCase("test_age"))
    suite.addTest(UserTestCase("test_isupper"))
    suite.addTest(UserTestCase("test_age"))
    # TextTestRunner() 文本测试用例运行器,参数verbosity生成报告
    runner = unittest.TextTestRunner(verbosity=2)
    #run()方法是运行测试套件的测试用例，入参为suite测试套件
    runner.run(suite)

#    4.高级实战系列之测试套件TestSuite生成测试报告 上集
#       简介:HTMLTestRunner介绍
#       1.HTMLTestRunner介绍
#         HTMLTestRunner是Python标准库的unittest模块的一个扩展,他可以生成HTML的测试报告,无法通过
#         pip安装,首先要下HTMLTestRunner.py文件,将下载的文件放入...\python\Lib目录下(或者同个路径)
#         注意点：
#             python2和python3语法不一样，导致HTMLTestRunner在python3不兼容
#         解决办法：导入网上修改好的HTMLTestRunner.py,安装HTMLTestRunner

#    5.高级实战系列之测试套件TestSuite生成测试报告 上集
#       简介：讲解使用测试套件TestSuite生成测试报告

#    6.unitest中HTML测试报告优化
#       简介：为每个测试用例添加需求说明,那么将会使报告更加易读懂，是工作中汇报数据技巧
#       u""   "引号中间写说明文字"
import unittest
import HTMLTestRunnerCN
import time
class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.name = '小D课堂'
        self.age = 28
    def tearDown(self):
        print('测试结束')
# 用例名称
    def test_name(self):
        # 判断名字是否相同
        self.assertEqual(self.name,'小F课堂',msg = '名字不对')
# 用例名称
    def test_age(self):
        # 判断年龄是否一致
        self.assertEqual(self.age,28,msg='年龄正确')
# 用例名称
    def test_isupper(self):
        # 判断括号里面的内容是否为错，若是则返回点(.),若不是，则返回msg
        self.assertFalse('xdclass'.isupper(),msg='不是大写')
    # 调用TestSuite控制用例顺序
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UserTestCase("test_age"))
    suite.addTest(UserTestCase("test_isupper"))
    suite.addTest(UserTestCase("test_name"))
    # TextTestRunner() 文本测试用例运行器,参数verbosity生成报告
#    runner = unittest.TextTestRunner(verbosity=2)
    #run()方法是运行测试套件的测试用例，入参为suite测试套件
#    runner.run(suite)
# 在文件名加入时间，防止文件被覆盖
file = time.strftime("%Y-%m-%d",time.localtime())
# 创建测试报告文件，此时文件为空
# wb以二进制格式打开的一个文件，用于写入，若文件存在则覆盖，不存在则创建
fp = open("./"+file+".html","wb")
# stream定义报告写入的文件，title是测试报告标题，description是测试报告描述
runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp,title=u"小D课堂 测试报告",description="测试用例执行情况")
# 写入测试报告
runner.run(suite)
fp.close()