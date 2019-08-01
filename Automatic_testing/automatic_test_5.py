# 自动化测试进阶实战篇
#     1.自动化测试实战之网页单选性别资料资料实战
#       简介：讲解使用selenium修改input输入框和单选框
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('C:\\Users\\Administrator\\Desktop\\Sublime\\HTML\\index.html')
print(driver.title)
print('默认选中男，2秒后选中女')
sleep(2)
driver.find_element_by_id('femal').click()

#     2.自动化测试之页面常见弹窗处理
#       简介：讲解使用selenium处理页面弹窗，alert和comfirm
#           弹窗常用方法：需要先切换到窗口再操作，语法：switch_to_alert()
#               accept()  表示接受
#               dismiss()  表示取消
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('C:\\Users\\Administrator\\Desktop\\Sublime\\HTML\\index1.html')
driver.implicitly_wait(2)
#点击alert按钮
driver.find_element_by_id('alert').click()
sleep(2)
#切换到alert弹窗窗口
btn1=driver.switch_to.alert
btn1.accept()
#点击confirm按钮
driver.find_element_by_id('confirm').click()
sleep(3)
#切换到confirm弹窗窗口点击取消
btn2=driver.switch_to.alert
btn2.dismiss()

#     3.自动化测试之验证码常见解决方案
#        简介：自动化测试之常见验证码解决方案
#        1.破解验证码
#          OCR识别：tesseract-ocr
#          AI机器学习：TensorFlow
#        2.绕过
#          1.让开发人员临时关闭验证码
#          2.提供万能的验证码（开发测试环境使用）
#          3.使用cookie（登录主要是为了拿cookie，获取登录凭证）
#
#     4.自动化测试实战进阶之cookie操作
#       简介：讲解自动化测试实战进阶操作cookie和使用场景
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("https://xdclass.net")
sleep(3)
# 传入cookie值
driver.add_cookie({"name":"name","value":"jack"})
driver.add_cookie({"name":"token","value":"xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMS5qcGVnIiwiaWQiOjExNjkwLCJuYW1lIjoi5Y2X6aOO5YyX5be3IiwiaWF0IjoxNTY0NTcyNDEyLCJleHAiOjE1NjUxNzcyMTJ9.3Mx6UKLMyYJk018uw3QtJgrsmseo80L5fwI2Q4yDZ6M"})
# 选择视频课程
driver.find_element_by_css_selector(".hotcourse > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)").click()
sleep(3)
# 切换到浏览器打开的新窗口
driver.switch_to.window(driver.window_handles[1])
# 在新窗口中定位：立即购买
driver.find_element_by_css_selector(".buy_tolearn > a:nth-child(1)").click()
print("进入下单页面")

#     5.实战系列之自动化测试错误截图
#       简介：讲解使用webdriver自动截图
#       driver.get_screenshot_as_file()
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("https://xdclass.net")
sleep(3)
# 点击登录框
driver.find_element_by_css_selector(".login > span:nth-child(2)").click()
# 捕捉找不到元素异常
try:
    driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("18855532272")
    driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("jjt19950227")
    driver.find_element_by_css_selector(".btn").click()
except:
    driver.get_screenshot_as_file("C:/360极速浏览器下载/vuejs/error.png")