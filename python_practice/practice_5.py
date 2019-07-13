# if语句
cars = ['audi','bmw','subaru','toyato']
for car in cars:
    if car == 'bmw':
        print(car.title())
    else:
        print(car.upper())
# 条件测试：
#           每条if语句的核心都是一个值为Ture或False的表达式，这种表达式被称为条件测试
# 检查多个条件
#   使用and检查多个条件
#     两个条件都满足则是Tuer，若有一个没满足则返回False
#   使用or检查多个条件
#     至少满足一个条件则是Ture，若都不满足则返回False
# 使用if-else语句
#     if-else结构：if 条件表达式：
#                     一条python语句...     # 若if的条件测试通过，则执行if后面的语句，否则执行else后面的语句
#                     一条python语句...     # if-else结构中，Python总会执行李思南公馆操作中的一个
#                     ...
#                   else：
#                     一条python语句...
#                     一条python语句...
#                     ...
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
# 使用if-elif-else 语句
# 年龄段收费的游乐场：4岁一下免费，4-18岁收5美元，18岁（含）以上收10美元
age = 12
if age <= 4:
    print('免费')
elif age < 18:
    print('收5美元')
else:
    print('收10美元')
# 使用多个elif代码块
#    可使用多个elif代码块，假设游乐场给老年人打折
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print('你要花费' + price + '美元')
# 5-3 假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其设置为'green' 、'yellow' 或'red' 。
#     编写一条if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。
#     编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
alien_color = ['green','red','yellow']
if 'green' in alien_color:
    print('你可以获得5个点')

