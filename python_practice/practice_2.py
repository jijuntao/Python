# 2-1 简单消息： 简单消息： 将一条消息存储到变量中，再将其打印出来。
my_mes = '你好'
print(my_mes)

# 2-2 多条简单消息：将一条消息存储到变量中，将其打印出来；再将变量的值修改为一条新消息，并将其打印出来。
my_mes = '你好'
print(my_mes)
my_mes = '世界'
print(my_mes)

# 2-3 个性化消息：将用户的姓名存到一个变量中，并向该用户显示一条消息。
#     显示的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”。
name_1 = 'eric'
print('Hello' +' '+ name_1.title() + ',' + 'would you like to learn some Python today?')

# 2-4 调整名字的大小写：将一个人名存储到一个变量中
#     再以小写、大写和首字母大写的方式显示这个人名。
name_2 = 'Ji jun tao'
print(name_2.lower())    # 小写显示
print(name_2.title())    # 首字母大写
print(name_2.upper())    # 大写显示

# 2-5 名言：找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：
#           Albert Einstein once said, “A person who never made a mistake never tried anything new.”
name_3 = 'li bai'
print(name_3.title() + ' ' + 'said' + ',' + '“举杯邀明月，对影成三人”')

# 2-6 重复练习2-5，但将名人的姓名存储在变量famous_person 中，再创建要显示的消息，并将其存储在变量message 中，然后打印这条消息。
famous_person = 'li bai'
message = famous_person.title() + ' ' + 'said' + ',' + '“举杯邀明月，对影成三人”'
print(message)

# 2-7 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。
# 打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来。
name_4 = '  ji  jun  tao  '
print('\t\n' + name_4)
print(name_4.lstrip())
print(name_4.rstrip())
print(name_4.strip())

# 2-8 编写4个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字8。
print(5+3)
print(2*4)
print(10-2)
print(16//2)