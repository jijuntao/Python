# 1.selenium基础实战之定位网页元素技巧
#   简介：讲解使用selenium定位网页元素
#   find_element_by_id,find_element_by_name,find_element_by_class_name
#
#   1.打开浏览器
#     brower = webdriver。Firefox()
#   2.打开网页
#     brower.get("http://www.baidu.com")
#     使用python判断是否正确
#     brower.title 或者 brower.current_url

#   3.定位元素的8种方法,(一定要唯一！！！)
#     id：find_element_by_id()  采用id属性进行定位
#     name：find_element_by_name()  定位方式和id类似，id，name和class一般在网页中至少会有其中一种
#     class name：find_element_by_class_name() 定位方式和id类似，id，name和class一般在网页中至少会有其中一种
#     (了解)tag name: find_element_by_tag_name()  通过标签名去定位，用的少，如find_element_by_tag_nmae("div")
#     link test: find_element_by_link_text() 超链接定位
#     partial link text：find_element_by_partial_link_text() 超链接定位模糊查询，和link text查询类似
#     难点：
#     css selector：find_element_by_css_selector()
#     根据css定位属性，class用.标记，id用#标记，定位方式也会比xpath快
#     如 find_element_by_css_selecctor("复制css选择器的内容")
#     技巧：通过查看元素拷贝css路径
#     路径：鼠标右键——>审查元素——>右键——>复制——>css选择器
#     xpath语法：
#     注意：“//”是全部的意思，“/”是相邻的意思，“*”所有元素，“..”元素的父节点，“.”当前节点
#       xpath：find_element_by_xpath()  xpath是XML路径语言，通过元素路径查找元素，HTML是XML的一种实现
#              绝对路径定位：从<html>标签开始依次往下进行查找
#              相对路径定位：利用元素属性进行xpath定位
#       技巧：通过查看元素拷贝css路径
#       绝对路径：鼠标右键——>审查元素——>右键——>复制——>xpath

#   4.定位到元素后的方法
#     clear()  清空
#     send_keys()  输入
#     back()  后退页面
#     maximize_window  最大化窗口
#     click()  点击事件 点击按钮，超链接
#     submit  提交表单

#   5.定位到元素后的属性
#     tag_name  标签名
#     text  文本内容
#     title  标题

#   6.定位元素报错，原因如下：
#       1.根据定位取不到
#       2.多个元素下标超出范围，没有0，从1开始
#       解决办法：换其他定位方法

# 第一种：id定位
from selenium import webdriver
# 拿到driver
driver = webdriver.Firefox()
# 打开百度网页
driver.get("http://www.baidu.com")
print(driver.title)
# 选中输入框，输入关键词：小D课堂
driver.find_element_by_id("kw").send_keys("小D课堂")
# 选中“百度一下”按钮，触发点击事件
driver.find_element_by_id("su").click()

# 第二种：name定位
from selenium import webdriver
# 拿到driver
driver = webdriver.Firefox()
# 打开百度网页
driver.get("http://www.baidu.com")
print(driver.title)
# 选中输入框，输入关键词：小D课堂
driver.find_element_by_name("wd").send_keys("小D课堂")
# 选中“百度一下”按钮，触发点击事件
driver.find_element_by_name("su").click()

# 第三种：class定位
from selenium import webdriver
# 拿到driver
driver = webdriver.Firefox()
# 打开百度网页
driver.get("http://www.baidu.com")
print(driver.title)
# 选中输入框，输入关键词：小D课堂
driver.find_element_by_class_name("s_ipt").send_keys("小D课堂")
# 选中“百度一下”按钮，触发点击事件
driver.find_element_by_id("su").click()

# 第四种：link text 超链接定位
from selenium import webdriver
from time import sleep
# 拿到driver
driver = webdriver.Firefox()
# 打开百度网页
driver.get("https://www.xdclass.net")
print(driver.title)
# 睡眠5秒，加载页面
sleep(5)
# 选中输入框，点击超链接：视频学习
driver.find_element_by_link_text("视频学习").click()

# 第五种：partial link text 超链接定位
from selenium import webdriver
from time import sleep
# 拿到driver
driver = webdriver.Firefox()
# 打开百度网页
driver.get("https://www.xdclass.net")
print(driver.title)
# 睡眠5秒，加载页面
sleep(5)
# 选中输入框，模糊查询：学习，进行点击
driver.find_element_by_partial_link_text("学习").click()

# 第六种：css定位
from selenium import webdriver
from time import sleep
# 拿到driver
driver = webdriver.Firefox()
# 打开百度网页
driver.get("https://www.xdclass.net")
print(driver.title)
# 睡眠5秒，加载页面
sleep(5)
# 使用css定位，用css选择器
driver.find_element_by_css_selector(".hotcourse > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)").click()

# 第七种：xpath 绝对路径定位
from selenium import webdriver
from time import sleep
# 拿到driver
driver = webdriver.Firefox()
# 打开百度网页
driver.get("https://www.xdclass.net")
print(driver.title)
# 睡眠5秒，加载页面
sleep(5)
# xpath定位，复制xpath内容
driver.find_element_by_xpath("复制的xpath内容").click()

