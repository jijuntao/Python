# for 循环

# 4-1 想出至少三种你喜欢的水果，将其名称存储在一个列表中，再使用for循环将每种水果的名称都打印出来。
#     修改这个for循环，使其打印包含水果名称的句子，而不仅仅是水果的名称。对于每种水果，都显示一行输出，如“I like pepperoni fruits”。
#     在程序末尾添加一行代码，它不在for循环中，指出你有多喜欢水果。输出应包含针对每种水果的消息，还有一个总结性句子，如“I really love fruits!”。
fruits = ['apple','orange','banana','tomato','pear']
for fruit in fruits:
    print(fruit)
    print('This is a' + fruit)
    print('I like' + fruit)
print('I really love fruits')

# 4-2想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for 循环将每种动物的名称都打印出来。
#    修改这个程序，使其针对每种动物都打印一个句子，如“A dog would make a great pet”。
#    在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any of these animals would make a great pet!”这样的句子
animals = ['dog','cat','tiger']
for animal in animals:
    print(animal)
    print('A dog would make a great pet')
print('Any of these animals would make a great pet')

# 4-3 使用一个for 循环打印数字1~20（含）。
for a in range(1,21):                    # 函数range()从你指定的第一个值开始数，并在到达你指定的第二个值后停止，值得区间闭右开。
    print(a)

# 4-4 创建一个列表，其中包含数字1~1000000.
#     再使用一个for循环将这些数字打印出来（如果输出的时间太长，按Ctrl + C停止输出，或关闭输出窗口）。
list_1 = [1,1000001]                     # 创建包含数字1~1000000的列表
for num in range(1,1000001):             # 打印列表
    print(num)

# 4-5 创建一个列表，其中包含数字1~1000000，
#     再使用min()和max()核实该列表确实是从1开始，到1000000结束的。
#     对这个列表调用函数sum(), 看看Python将一百万个数字相加需要多长时间。
list_2 = [a*1for a in range(1,1000001)]  # 创建包含数字1~1000000的列表
print(list_2)                            #打印列表
print(min(list_2))                       #打印列表最小值
print(max(list_2))                       #打印列表最大值
print(sum(list_2))                       #打印列表中的数字相加之和

# 4-6 通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数再使用一个for 循环将这些数字都打印出来。
list_4 = [a*1for a in range(1,21,2)]     # 每隔2个数创建列表
print(list_4)
for b in list_4:                         # 把列表中的数字打印出来
    print(b)

# 4-7 创建一个列表，其中包含3~30内能被3整除的数字；
#     再使用一个for循环将这个列表中的数字都打印出来。
list_5 =[a*1for a in range(3,31,3)]      # 每隔3个数创建列表
print(list_5)
for list_5 in list_5:                    # 把列表中的数字打印出来
    print(list_5)

# 4-8 请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循 环将这些立方数都打印出来。
list_6 = [a**3for a in range(1,11)]        # 创建前10个整数（即1~10）的立方的列表
print(list_6)
for list_6 in list_6:                      # 把列表中的数字打印出来
    print(list_6)

# 4-9 使用列表解析生成一个列表，其中包含前10个整数的立方
list_7 = [a**3for a in range(1,11)]        # 创建前10个整数（即1~10）的立方的列表
print(list_7)

# 切片 利用索引截取列表中的片段，生产子集

# 4-10 编写的一个程序，以完成如下任务。
ball = ['football','basketball','soccer','shot','pingbang']
# 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
print('The first three items in the list are:')
print(ball[0:3])
# 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
print('Three items from the middle of the list are:')
print(ball[1:4])
# 打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素
print('The last three items in the list are:')
print(ball[-3:])

# 复制列表  在列表名字加[:]即可复制整个列表
my_food = ['pizza','cake','rice']
friend_food = my_food[:]
print(my_food)
print(friend_food)        # 打印出来的结果一致
my_food.append('apple')
friend_food.append('ice cream')
print(my_food)            # 打印的列表内容多出apple
print(friend_food)        # 打印的列表内容多出ice cream
# my_food和friend_food为独立列表，各无关系
# 倘若我们只是简单地将my_foods 赋给friend_foods ，就不能得到两个列表
my_food = ['pizza','cake','rice']
friend_food = my_food     # 把my_food列表赋给friend_food
my_food.append('apple')
friend_food.append('ice cream')
print(my_food)            # 打印的列表内容多出apple
print(friend_food)        # 打印的列表内容多出apple
# my_food和friend_food实则指向同一个对象，所以同时改变

# 4-11 创建水果列表，创建此列表的副本
fruit = ['apple','orange','banana']
my_fruit = fruit[:]
#     在原来的比萨列表中添加一种比萨
fruit.append('tomato')
#     在列表my_fruit中添加另一种水果
my_fruit.append('pineapple')
#     核实你有两个不同的列表。再使用一个for 循环来打印第一个列表；
print(fruit)
print(my_fruit)
for fruits in fruit:
    print(fruits)
#     再使用一个for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
for my_fruits in  my_fruit:
    print(my_fruits)

# 元组(tuple)  元组是不可变的列表，是用圆括号()来标识而不是方括号[]，可以用索引来访问。
# 遍历元组
tuple = (500,100,200)
for tuples in tuple:
    print(tuples)
# 修改元组变量
tuple_1 = (500,200,200)
print(tuple_1)
tuple_1 = (400,100,100)
print(tuple_1)

# 4-13 请想出五种简单的食品，并将其存储在一个元组中。
#      使用一个for 循环将该餐馆提供的五种食品都打印出来
food = ('rice','noodle','dumplings','wonton','rice flour')
for foods in food:
    print(foods)
# 替换了它提供的其中两种食品，并使用一个for 循环将新元组的每个元素都打印出来
food = ('rice','noodle','dumplings','apple','banana')
for foods in food:
    print(foods)

# 设置代码格式
#        进很重要


