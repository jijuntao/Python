# 安装python 3.7，百度教程
# 安装selenium，下载网址官网，最好适应64位，在selenium目录下按住shift+鼠标右键，打开cmd，输入pyhton setup.py install
#     验证是否安装成功输入pip list，若有selenium即成功
#     selenium下载地址：https://pypi.org/project/selenium/，在selenium安装文件下shift+右键，然后输入命令
#     python setup.py install安装
# 安装火狐、谷歌浏览器
# 安装火狐浏览器驱动geckodrive-64，浏览器驱动应放置在python安装目录下
# 了解前端知识html，js，css，json，
# 在python的IDLE编辑器中输入from selenium import webdriver即可使用火狐浏览器驱动
from selenium import webdrive
driver = webdrive.Firefox()
driver.get("https://baidu.com")


# from time import sleep
# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get("https://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("python")
# driver.find_element_by_id("su").click()
# sleep(3)
# driver.close()