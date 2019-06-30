# 列表

# 3-1 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
name = ['孙俊','计俊涛','董鹏','赵权']
print(name[0] + '，' + '你好！')
print(name[1] + '，' + '你好！')
print(name[2] + '，' + '你好！')
print(name[3] + '，' + '你好！')

# 3-3  想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。
car = ['bick','bus','plane','moto',]
print('I would liake to own a' + ' ' +  car[2].title() + '.')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
del motorcycles[0]    #根据索引删除列表中的元素，删除的元素不可用
print(motorcycles)
last_owned = motorcycles.pop()    #.pop()根据索引弹出列表中的元素(默认最后一位)，弹出的元素可用
print(motorcycles)
print("The last motorcycle I owned was a " + last_owned.title() + ".")
motorcycles.remove('moto')    #.remove()根据值移除列表中的元素
print(motorcycles)
my_motorcycles = 'moto'    #.remove()根据索引弹出列表中的元素，弹出的元素可用
motorcycles.remove(my_motorcycles)
print(motorcycles)
print('A' +' ' + my_motorcycles.title() +' '+ 'is too small.' )

# 3-4 请创建一个列表，其中包含至少3个你想邀请的人；使用这个列表打印消息，邀请这些人来与你共进晚餐。
# from typing import List
#
people = ['孙俊','程婷婷','陈建']  # type: List[str]
print('I invite' +' '+ people[0] +'、'+ people[1] +'、'+ people[2] +' '+ 'to dinner.')

# 3-5 你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# 以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
my_people = '陈建'
people.remove(my_people)
print('The' +' '+ my_people + ' ' + 'do not come.')   # 指出哪位嘉宾无法赴约
people[2] = '我'  # 替换列表中的元素
print(people)
print('I invite' +' '+ people[0] +'、'+ people[1] +'、'+ people[2] +' '+ 'to dinner.')

# 3-6 请想想你还想邀请哪三位嘉宾。
# 使用insert() 将一位新嘉宾添加到名单开头。
# 使用insert() 将另一位新嘉宾添加到名单中间。
# 使用append() 将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息，向名单中的每位嘉宾发出邀请。
people.insert(0,'张')
people.insert(1,'韩')
people.append('李')
print(people)

# 3-7 只能邀请两位嘉宾.
# 使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进 晚餐。
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
new1_people = people.pop(3)
print('I am sorry I can*t invite' +' '+ new1_people +' '+ 'to dinner.')
new2_people = people.pop(4)
print('I am sorry I can*t invite' +' '+ new2_people +' '+ 'to dinner.')
new3_people = people.pop(0)
print('I am sorry I can*t invite' +' '+ new3_people +' '+ 'to dinner.')
new4_people = people.pop(1)
print('I am sorry I can*t invite' +' '+ new4_people +' '+ 'to dinner.')
print('I invite' +' '+ people[0] +'、'+ people[1] +' '+ 'to dinner.')
print(people)
del people[0]
del people[0]
print(people)

# 3-8 想出至少5个你渴望去旅游的地方。
# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
# 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
# 使用sorted() 按字母顺序打印这个列表，同时不要修改它。
# 再次打印该列表，核实排列顺序未变。
# 使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
# 再次打印该列表，核实排列顺序未变。
# 使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
# 使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
# 使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
# 使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
travel = ['beijing','shanghai','xiamen','qingdao','zhoushan']
print(travel)
print(sorted(travel))
print(travel)
travel.sort(reverse = True)
print(travel)
travel.reverse()
print(travel)
travel.reverse()
print(travel)
travel.sort()
print(travel)
travel.sort(reverse=True)
print(travel)
print(len(travel))
