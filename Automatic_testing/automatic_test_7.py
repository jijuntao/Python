# 第八章、自动化测试selenium和unittest整合项目实战
#        1.小D课堂官网项目实战需求说明
#          简介：讲解小D课堂官方自动化测试需求场景和项目基础框架搭建
#          1.自动化测试里面的测试用例设计的一些方法
#             解耦、可以独立运行、需要灵活切换
#             设计思路：脚本功能分析（分步骤）和模块化分层（拆分为多个模块）
#          project
#               login_order.py # 登录下单测试用例
#               category.py # 菜单分类测试用例
#               all_test.py # 主入口
#
#        2.自动化测试实战之下单测试自动化测试
#          简介：使用unittest + selenium 下单测试用例编写
#          1.使用原先的资料 第5章第3集  第6章第4集

#        3.分类列表整合uniittest自动化测试
#          简介：使用unittest + selenium 菜单弹窗测试用例编写
#               1.使用资料  第5章第2集
# 登录测试用例 单独py文件：login.py
import unittest
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class LoginOrderTestCase(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.base_url = 'https://xdclass.net'
        self.driver.get(self.base_url)

    def tearDown(self):
        print('测试结束')
        pass
       # 单个测试用例结束
    def test_login_order(self):
        u'登录测试用例'
        driver = self.driver
        # 获取登录框
        login = driver.find_element_by_css_selector('.login > span:nth-child(2)')
        ActionChains(driver).click(login).perform()
        sleep(3)
        # 清除输入框里面的数据
        driver.find_element_by_css_selector('.mobienum > input:nth-child(1)')
        driver.find_element_by_css_selector('.psw > input:nth-child(1)')
        # 输入账号密码
        driver.find_element_by_css_selector('.mobienum > input:nth-child(1)').send_keys('18855532272')
        driver.find_element_by_css_selector('.psw > input:nth-child(1)').send_keys('jjt19950226')
        # 点击登录
        login_button = driver.find_element_by_css_selector('.btn')
        ActionChains(driver).click(login_button).perform()
        sleep(2)
        # 将鼠标移到头像
        photo = driver.find_element_by_css_selector('.avatar_img')
        ActionChains(driver).move_to_element(photo).perform()
        # 获取用户名
        user_name = driver.find_element_by_css_selector('.username')
        print('测试结果')
        print(user_name.text)
        if user_name.text = u'南风北巷':
            print('登录成功')
        else:
            print('登录失败')
        # 选择课程
        lesson = driver.find_element_by_css_selector('.hotcourse > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)')
        ActionChains(driver).move_to_element(lesson).perform()
        # 切换到新打开的窗口
        driver.switch_to_window(driver.window_handles[1])
        # 点击立即购买
        driver.find_element_by_css_selector('.buy_tolearn > a:nth-child(1)')
        print('进入下单页面')
if __name__ == '__main__':
        unittest.main()

# 下单测试用例 单独py文件：category.py
import unittest
import time
from selenium import webdriver
from time import sleep
from  selenium.webdriver.common.action_chains import ActionChains

class CategoryTestCase(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.base_url = 'https://xdclass.net'
        self.driver.get(self.base_url)
    def tearDown(self):
        print('测试结束')
    def test_menu(self):
        u'菜单分类测试用例'
        driver = self.driver
        sleep(2)
        menu = driver.find_element_by_css_selector('.hotcourse > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)')
        ActionChains(driver).click(menu).perform()
        sleep(3)
        # 切换到浏览器打开的新窗口
        driver.switch_to.window(driver.window_handles[1])
        # 在新窗口中定位：立即购买
        driver.find_element_by_css_selector(".buy_tolearn > a:nth-child(1)").click()
        print("进入下单页面")
        sleep(2)
if __name__ == '__main__':
    unittest.main()

# 登录下单测试用例
import unittest
import HTMLTestRunnerCN
import login,category
import time
# 创建容器，即测试集
def create_sutie():
    print('测试开始')
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(login.LoginOrderTestCase))
    suite.addTest(unittest.makeSuite(category.CategoryTestCase))
    return suite

if __name__ == '__main__':
    suite = create_sutie()
    # 测试报告文件名称中加入时间
    my_file = time.strftime('%Y-%m-%d',time.localtime())
    # 创建测试报告
    fp = open('./'+my_file+' result.html','wb')
    # stream定义一个测试报告写入的文件，title测试报告标题，description描述
    runner = HTMLTestRunnerCN.HTMLReportCN(stream=fp,title=u'小D课堂  测试报告',description='测试用例执行情况',verbosity=2)
    runner.run(suite)
    fp.close()

#        4.必备技能之发送测试报告邮件
#          简介：讲解发送邮件的基础知识
#          1.邮件发送的基本过程与概念
#             邮件服务器：类似于现实生活中的邮局，他主要负责接收用户投递过来的邮件，并把邮件投递到邮件接受者的电子邮箱中
#             点击邮箱：用户在邮件服务器上申请的一个账户
#             from:<xxx@xx.com>   -----邮件头
#             to<xxx@xx.com>      -----邮件头
#             subject：hello      -----邮件头
#          2.邮件传输协议
#             SMTP协议：全称为Simple Mail Transfer Protocol,简单邮件传输协议。它定义了邮件客户端软件和SMTP邮件服务器之间，
#                       以及两台SMTP邮件服务器之间的通信规则
#             POP3协议：全称为Post Office Protocol，邮局协议。它定义了邮件客户端软件和POP3邮件服务器的通信规则
#             IMAP协议：全称为Internet Message Access Protocol,Internet 消息访问协议，它是对POP3协议的一种扩展，也是定义
#                       了邮件客户端软件和IMAP邮件服务器的通信规则
#
#        5.使用python发送邮件实战
#          简介：讲解使用python发送邮件
#                导入依赖
#          1.使用163邮箱
#            A：18855532272@163.com
#            B：
#            SMTP地址：smtp163.com
# 依赖
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import  os,time,datetime
# 发件人
sender = " "
# 收件人
receiver = " "
# 不用客户端密码发送，用授权码发送
auth_code = "jjt19950226"
# 定义主题
subject = "自动化测试报告"
# 定义发送内容
msg = MIMEText("<html><h2>欢迎来到小D课堂</h2></html>",_subtype="html",_charset="utf-8")
msg["Subject"] = subject
msg["from"] = sender
msg["to"] = receiver

smtp = smtplib.SMTP()
smtp.connect("邮箱服务器")
smtp.login(sender,auth_code)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

#        6.使用python发送测试报告邮件和附件
#          简介：使用python发送测试报告邮件和附件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import  os,time,datetime
from email.mime.multipart import MIMEMultipart
# 发件人
sender = " "
# 收件人
receiver = " "
# 不用客户端密码发送，用授权码发送
auth_code = "jjt19950226"

subject = '自动化测试报告'
# 读取文件内容
f = open('测试报告地址','rb')
mail_body = f.read()
f.close()
# HTML形式的邮件内容
html = MIMEText(mail_body,_subtype='html',_charset='utf-8')
html['Subject'] = subject
html['from'] = sender
html['to'] = receiver

# HTML附件 将测试报告放在附件中发送
att = MIMEText(mail_body,'base64','gb2312')
att ['Content-Type'] = 'application/octet-stream'
att ['Content-Disposition'] = 'attachment;filename="XdclassTestReport.html"' # 这里的filename可以任意写

msg = MIMEMultipart()
msg['Subject'] = subject # 邮件标题
msg.attach(html)
msg.attach(att)

# 连接登录上smtp服务器
smtp = smtplib.SMTP()
smtp.connect('163邮箱服务器')
smtp.login(sender,auth_code)
# 发送邮件
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

#        7.自动化测试项目实践整合发送测试报告邮件
#          简介：抽取发送邮件的代码，整合自动化测试
# 发送邮件单独py文件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import  os,time,datetime
from email.mime.multipart import MIMEMultipart

class MailUtils():
    # 表示一个类方法，不需要实例化，可以直接调用
    @classmethod
    def send_tste_report(cls):
        # 发件人
        sender = " "
        # 收件人
        receiver = " "
        # 不用客户端密码发送，用授权码发送
        auth_code = "jjt19950226"

        subject = '自动化测试报告'
        # 读取文件内容
        f = open('测试报告地址', 'rb')
        mail_body = f.read()
        f.close()
        # HTML形式的邮件内容
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        html['Subject'] = subject
        html['from'] = sender
        html['to'] = receiver

        # HTML附件 将测试报告放在附件中发送
        att = MIMEText(mail_body, 'base64', 'gb2312')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename="XdclassTestReport.html"'  # 这里的filename可以任意写

        msg = MIMEMultipart()
        msg['Subject'] = subject  # 邮件标题
        msg.attach(html)
        msg.attach(att)

        # 连接登录上smtp服务器
        smtp = smtplib.SMTP()
        smtp.connect('163邮箱服务器')
        smtp.login(sender, auth_code)
        # 发送邮件
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()

# 登录下单用例
# 登录下单测试用例
import unittest
import HTMLTestRunnerCN
import login,category
import time

from mail import MailUtils
# 创建容器，即测试集
def create_sutie():
    print('测试开始')
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(login.LoginOrderTestCase))
    suite.addTest(unittest.makeSuite(category.CategoryTestCase))
    return suite

if __name__ == '__main__':
    suite = create_sutie()
    # 测试报告文件名称中加入时间
    # my_file = time.strftime('%Y-%m-%d',time.localtime())
    # 创建测试报告
    fp = open('./ result.html','wb')
    # stream定义一个测试报告写入的文件，title测试报告标题，description描述
    runner = HTMLTestRunnerCN.HTMLReportCN(stream=fp,title=u'小D课堂  测试报告',description='测试用例执行情况',verbosity=2)
    runner.run(suite)
    fp.close()
    MailUtils.send_tste_report()

# 第九章 课程总结
#        1.课程总结和常见问题处理
#          简介：课程总结和讲解常见的问题处理
#          必备：
#               初级：html/css/js/http
#               中级：Linux/mysql/jmeter
#               python + request 网络库去开发接口自动化测试
#               高级：jenkins/git (管理项目质量、搭建所有基础组件)
