# selenium实战之模拟事件处理
# 1.自动化测试实战之ActionChains模拟用户行为
#   简介：讲解使用selenium里面的ActionChains模拟用户行为
#   需求：
#       模拟鼠标操作才能进行的情况，比如单击、双击、点击鼠标右键，拖拽
#   解决：
#       selenium提供了一个类来处理这类事件
#       selenium.webdriver.common.action_chains.ActionChains(driver)
#   执行脚本：
#       from selenium.webdriver.common.action_chains import ActionChains
#   执行原理：
#       调用ActionChains的方法时不会立即执行，会将所有的操作按顺序存放在一个队列里，当调用perform()时，队列中的事件会依次执行
#   支持链式写法或者分步写法：
#       ActionChains(driver).click(ele).perform()
#   鼠标和键盘方法列表：
#       perform()  执行链中的所有操作
#       click(on_element=None)  单击鼠标左键
#       context_click(on_element=None)  单击鼠标右键
#       double_click(on_element=None)  双击鼠标左键
#       move_to_element(to_element)  鼠标移动到某个元素
#       ele.send_keys(keys_to_send)  发送某个词到当前焦点的元素
#       不常用的：
#       click_and_hold(on_element=None)  点击鼠标左键不松开
#       release(on_element=None)  在某个元素位置松开鼠标左键
#       key_down(value,element=None)  按下某个键盘上的键
#       key_up(value,element=None)  松开某个键
#       drag_and_drop(source,target)  拖拽到某个元素然后松开
#       drag_and_drop_by_offsrt(source,xoffset,yoffset)  拖拽到某个坐标点后松开
#       move_by_offset(xoffset,yoffset)  鼠标从当前位置移动到某个坐标
#       move_to_element_with_offset(to_element,xoffset,yoffset)  移动到某个元素多少距离的位置

# 2.鼠标事件实战之hover菜单栏弹出
#      简介：鼠标事件之菜单栏hover弹出
#   1.#引入ActionChains类
#     from selenium.webdriver.common.action_chains import ActionChains
#   2.move_toelement(to_element)  鼠标移动到某个元素
#     #对定位到的元素执行鼠标移动到上面的操作
#     ActionChains(driver).move_to_element(ele1).perform()

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# 拿到driver
driver = webdriver.Chrome()
# 跳转到小D课堂网页
driver.get("https://xdclass.net")
# 打开网页缓冲5秒时间
sleep(5)
# 定位鼠标移动到上面的元素
menu_ele = driver.find_element_by_css_selector(".list_item > li:nth-child(1)")
# 调用移动鼠标事件
ActionChains(driver).move_to_element(menu_ele).perform()
# 选中子菜单
sub_menu_ele = driver.find_element_by_css_selector(".base > div:nth-child(3) > a:nth-child(1)")
# 停留5秒看效果
sleep(3)
# 调用点击子菜单事件
ActionChains(driver).click(sub_menu_ele).perform() #或者
# sub_menu_ele.click()

# 3.多知识综合实战之模拟用户登录
#      简介：讲解使用selenium模拟登录小D课堂，并选择课程
#   1.多知识点实战
#   2.查找登录框——>输入用户名和密码——>触发登录——>判断登录是否成功——>打印结果

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
# 打开浏览器
driver = webdriver.Firefox()
# 跳转网页
driver.get("https://xdclass.net")
# 隐性等待6秒
driver.implicitly_wait(6)
# 点击登录
driver.find_element_by_css_selector(".login > span:nth-child(2)").click()
# 清理账号密码输入框并输入账号密码
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("18855532272")
driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("jjt19950226")
# 点击登录
driver.find_element_by_css_selector(".btn").click()
# 鼠标移动到头像
sleep(5)
move_mouse = driver.find_element_by_css_selector(".avatar_img")
ActionChains(driver).move_to_element(move_mouse).perform()
# 查看用户名
username = driver.find_element_by_css_selector(".username")
# 打印用户名
print("测试结果是：")
print(username.text)
name = username.text
# 验证是否成功
if name == '南风北巷':
    print('登录成功')
else:
    print('登录失败')
driver.quit()

# 4.自动化测试实战之网页等待时间
#      简介：讲解自动化测试的等待时间
#   1.为什么需要等待时间——>等系统稳定
#     网页需要加载对应的资源文件，页面渲染，窗口处理等等
#   2.自动化测试常用的等待时间
#     强制等待：(开发调试代码是常用)
#          from time import sleep
#          sleep(5)  # 强制等待5秒再执行下一步，缺点是不管资源是否完成，都必须等待
#   隐性等待：(一般工作中使用隐形等待)
#           driver.implicitly_wait(10)  # 隐性等待，最长等10秒
#           设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步否则一直等待时间截止，然后执行下一步
#           缺点是程序会一直等待整个页面加载完成，到浏览器标签栏那个加载圈不在转
#           注意：对driver起作用，所以设置一次即可，不用导出设置
#   显性等待：(在元素出现时间较短，难以定位时使用)
#           WebDriverWait 需要配合

#           until和until_not 程序每隔N秒检查一次，如果成功，则执行下一步，否则继续等待，直到超过设置的最长时间
#           from selenium.webdriver.support.wait import WebDriverWait
#           语法：WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
#                                     最长时间  每隔时间检查一次     忽略异常(非必须的)
#                from selenium.webdriver.common.by import By
#                from selenium.webdriver.support.ui import WebDriverWait
#                from  selenium.webdriver.support import expected_conditions as EC
#    结论：隐性等待和显性等待可以同时使用，等待的最长时间取两者之中的较大者

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
# 拿到driver
driver = webdriver.Firefox()
# 跳转网页
driver.get("https://baidu.com")

try:
# 显性等待
    xian_time = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
# 输入框输入小D课堂
    xian_time.send_keys("小D课堂")
    print("资源加载成功")
except:
    print("资源加载失败")
# 不管有没有成功，都打印下，用于资源清理
finally:
    print("清理资源")
# 退出浏览器
    driver.quit()