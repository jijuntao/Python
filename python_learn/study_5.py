# 字符串的使用 - 计算长度 / 下标运算 / 切片 / 常用方法
# 列表基本用法 - 定义列表 / 用下表访问元素 / 下标越界 / 添加元素 / 删除元素 / 修改元素 / 切片 / 循环遍历
# 列表常用操作 - 连接 / 复制(复制元素和复制数组) / 长度 / 排序 / 倒转 / 查找
# 生成列表 - 使用range创建数字列表 / 生成表达式 / 生成器
# 元组的使用 - 定义元组 / 使用元组中的值 / 修改元组变量 / 元组和列表转换
# 集合基本用法 - 集合和列表的区别 / 创建集合 / 添加元素 / 删除元素 / 清空
# 集合常用操作 - 交集 / 并集 / 差集 / 对称差 / 子集 / 超集
# 字典的基本用法 - 字典的特点 / 创建字典 / 添加元素 / 删除元素 / 取值 / 清空
# 字典常用操作 - keys()方法 / values()方法 / items()方法 / setdefault()方法

# 字符串使用：
#    计算长度：len()函数
a = 'hello'
print(len(a))
#     下标运算：即索引，从0开始计算。如：
i = 'bick'
print(i[0])
#      切片：指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。
#      切片语法：[起始:结束:步长]
#         注意：选取的区间属于“左闭右开型”，不包含结束位本事
# 取下标为1、2、3的字符
name = 'abcdefg'
print(name[1:4]) # 输出：bcd
# 取下标为2开始到最后的字符
print(name[2:])  # 输出：cdefg
# 取从开始到下标为5的字符
print(name[:6])  # 输出：abcdef
# 取下标为1开始 到 最后第二个(包括第二个) 之间的字符
print(name[1:-1]) # 输出：bcdef
# 从开始到结束，每两个截取
print(name[::2])  # 输出：acdeg
# 从开始到下标4，每两个截取
print(name[:5:2]) # 输出：ace
# 从开始到结束，倒序排列
print(name[::-1]) # 输出：gfedcba


# 列表基本用法：
#    列表定义：列表 列表 由一系列按特定顺序排列的元素组成。在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素，如：
list = ['trek', 'cannondale', 'redline', 'specialized']
print(list)
# 访问列表元素:使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
print(list[0]) # 输出：trek
# 访问列表最后一个元素
print(list[-1])
# 添加列表元素：
#    在末尾添加：方法append() 将元素'ducati' 添加到了列表末尾，而不影响列表中的其他所有元素
list.append('bike')
#    在中间插入：使用方法insert() 可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。
list.insert(1,'bus')
# 删除列表元素：
#    使用del 语句将值从列表中删除后，你就无法再访问它了。
del list[0]
#    方法pop() 可删除列表末尾的元素，并让你能够接着使用它。pop()可根据下标弹出，默认末尾元素
my_list = list.pop()
print(my_list)
#    根据值删除元素：
#        如果你只知道要删除的元素的值，可使用方法remove()，删除后可继续使用该值
#        若列表中出现多个相同的值，remove()默认删除第一个值
my_list1 = 'redline'
list.remove(my_list1)
print(list)
# 切边：与字符串用法相同
# 循环遍历：
#     使用for循环语句
for lists in list:
    print(lists)

# 列表常用操作：
#    列表的连接：合并2个列表
a = [1,2,3] # 列表a
b = ['x','y','z'] #列表b
c = a + b     # a列表和b列表连接
print(c) # 输出：[1,2,3,'a','b','c']
#          使用函数extend()连接
a.extend(b) # 把b列表添加至a列表末尾
print(a)
#    列表的复制：有深浅拷贝区别
#        非拷贝方法——直接赋值：结果一致
old = [0,1,2,3,4,5,]
new = old
old.append(6)
new.append(7)
print(old) # 输出：[0,1,2,3,4,5,6,7]
print(new) # 输出：[0,1,2,3,4,5,6,7]
# old和new实则指向同一个对象，所以同时改变
#         浅拷贝的几种方法：
#             1.copy()方法
#               复制此列表(只复制一层，不会复制深层对象) 等同于 L[:]
a = [1,2,3]
b = [4,5,a]
c = b.copy()
a[0] = 7
print(b) # 输出：[4,5,[7,2,3]]
print(c) # 输出：[4,5,[7,2,3]]
#              2.使用列表生成式
#                使用列表生成式产生新列表也是一个浅拷贝方法，只对第一层实现深拷贝
d = [1,2,[4,5,6,],3]
d_1 = [i for i in d]
print(d)     # 输出：[1,2,[4,5,6],3]
print(d_1)
d_1[0] = 7   # 输出：[1,2,[4,5,6],3]
d_1[2][0] = 8
print(d)     # 输出：[1,2,[4,5,6],3]
print(d_1)   # 输出：[7,2,[8,5,6],3]
#              3.用for循环遍历
#                通过for循环遍历，将元素一个个添加到新列表中。这也是一个浅拷贝方法，只对第一层实现深拷贝。
a = [1, [1, 2, 3], 3]
b = []
for i in range(len(a)):
    b.append(a[i])
print(a)      # 输出：[1, [1, 2, 3], 3]
print(b)      # 输出：[1, [1, 2, 3], 3]
b[0] = 3
b[1][0] = 3
print(a)      # 输出：[1, [3, 2, 3], 3]
print(b)      # 输出：[3, [3, 2, 3]，3]
#              4.使用切片
#                通过使用[:]切片，可以浅拷贝整个列表。同样的，只对第一层实现深拷贝
old = [1, [1, 2, 3], 3]
new = old[:]
print(old)    # 输出：[1, [1, 2, 3], 3]
print(new)    # 输出：[1, [1, 2, 3], 3]
new[0] = 3
new[1][0] = 3
print(old)    # 输出：[1, [3, 2, 3], 3]
print(new)    # 输出：[3, [3, 2, 3]，3]
#           深拷贝：
#               如果用deepcopy()方法，则无论多少层，无论怎样的形式，得到的新列表都是和原来无关的，这是最安全最清爽最有效的方法。
#               使用时，要导入copy
import copy
old = [1, [1, 2, 3], 3]
new = copy.deepcopy(old)
print(old)    # 输出：[1, [1, 2, 3], 3]
print(new)    # 输出：[1, [1, 2, 3], 3]
new[0] = 3
new[1][0] = 3
print(old)    # 输出：[1, [1, 2, 3], 3]
print(new)    # 输出：[1, [3, 2, 3], 3]
#    列表的长度：len()函数
cars = ['bmw', 'audi', 'benz']
# 输出列表长度
print('列表长度是:')
print(len(cars))
#    列表的排序：
#       使用方法sort() 对列表首字母进行永久性排序，再也无法恢复到原来的排列顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # 输出：['audi', 'bmw', 'subaru', 'toyota']
#       使用方法sort()传递参数reverse=True 对列表首字母进行永久性排序(倒序)，再也无法恢复到原来的排列顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars) # 输出：['toyota', 'subaru', 'bmw', 'audi']
#       使用函数sorted() 对列表进行临时排序 对列表进行临时排序
# 用法同sort()
#       倒着打印列表：
#          要反转列表元素的排列顺序，可使用方法reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)   # 输出：['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)   # 输出：['subaru', 'toyota', 'audi', 'bmw']
#    列表的查找：
#       五种方式：in、not in、count、index，find 前两种方法是保留字，后两种方式是列表的方法。
#       1.判断值是否在列表中，in操作符
list = ['a',1,2,'b','hello']
print('a' in list) # 输出True
#       2.判断值是否不在列表中，not in操作符
print('b' not in list) # 输出：False
#       3.统计指定值在列表中出现的次数，count方法
print(list.count('a'))
#       4.查看指定值在列表中的位置。index方法
list.index('a')
list.index('a',0,3) # 在指定切片内第一次出现的位置
#       5.string类型的话可用find方法去查找字符串位置
#          如果找到则返回第一个匹配的位置，如果没找到则返回-1，而如果通过index方法去查找的话，没找到的话会报错
print(list.find('a'))
#    列表的生成：
#       使用rang()创建数字列表
num = list(range(1,6))
print(num)
#       指定步长创建数字列表
num = list(range(1,11,2))
print(num)
#       使用for循环创建列表的平方
num = [a**2 for a in range(1,4)]
print(num) # 输出：[1,4,9]


# 元组的使用：
#    定义元组：元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
s = (100,200)
print(s(0)) # 输出：100
#    修改元组：元组中的元素值是不允许修改的，可重新赋值，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2;
print (tup3) # 输出：(12, 34.56, 'abc', 'xyz')
#    删除元组：元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('Google', 'Runoob', 1997, 2000)
del tup
#    元组和列表转换:元组比列表的运算速度快，而且元组的数据比较安全。元组是不可改变的
a = [1,2,3]
tupl = tuple(a)
print(tupl)       # 输出：(1,2,3)
list = list(tupl)
print(list)       # 输出：[1,2,3]


# 集合基本用法：
#    集合和列表的区别：列表是一组任意类型的值，按照一定顺序组合而成的
#                   集合（set）是一个无序的不重复元素序列
#                   列表使用[]符号创建
#                   可以使用大括号{ }或者 set()函数创建集合，注意：创建一个空集合必须用set()而不是{ }，因为{ }是用来创建一个空字典
gather = {1,2,3,'hello',2,3}
#或者
set = {1,2,3,'hello',2,3}
print(gather) # 输出：{1,2,3,'hello'}，集合具有去重功能
#    添加集合元素：
#               s.add(),将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作
gather.add(4)
print(gather)
#               还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下
#               s.update( x )
#    删除集合元素：
#               s.remove( x )，将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误
gather.remove(1)
print(gather)
#               还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
#               s.discard( x )
#               设置随机删除集合中的一个元素，语法格式如下：
#               s.pop()
gather.pop()
print(gather)
#   清空集合元素：
#              s.clear()
gather.clear()
print(gather) # 返回set(),表示空集合
# 集合常用操作：
#            交集：
#                两个集合A和B的交集是含有所有既属于A又属于B的元素，而没有其他元素的集合。
#                使用&操作符执行交集操作，同样地，也可使用方法intersection()完成
A = {'a','b','c','d'}
B = {'c','d','e','f'}
print(A & B) # 输出:{'c','d'}
#            并集：
#                一组集合的并集是这些集合的所有元素构成的集合，而不包含其他元素
#                使用操作符 | 执行并集操作，同样地，也可使用方法 union() 完成。
print(A | B) # 输出：{'c','a','b','d','f','e'}
# 或者
print(A.union(B))
#            差集：
#                A 与 B 的差集是所有属于 A 且不属于 B 的元素构成的集合
#                使用操作符 - 执行差集操作，同样地，也可使用方法 difference() 完成
print(A - B) # 输出{'b','a'}
# 或者
print(A.difference(B))
#            子集：
#                子集，为某个集合中一部分的集合，故亦称部分集合。
#                使用操作符 < 执行子集操作，同样地，也可使用方法 issubset() 完成。
C = {'a','b'}
print(C < A) # 输出：True
print(C < B) # 输出：False
# 或者
print(C.issubset(A))
#            超集：
#                一个集合包含另一个集合的全部为超集
#                使用操作符 > 执行子集操作，当两个集合相同时，互为超集
print(A > C) # 输出：True
print(B > C) # 输出：False
#           对称差：
#                 两个集合的对称差是只属于其中一个集合，而不属于另一个集合的元素组成的集合。即两个集合不同部分组成的集合为两个集合的对称差
#                 使用 ^ 操作符执行差集操作，同样地，也可使用方法 symmetric_difference() 完成
print(A ^ B) #输出：{'f','b','e','a'}
#或者
print(A.symmetric_difference(B))


# 字典的基本用法：
#    字典的特点：
#            1.字典是另 一种可变容器模型，且可存储任意类型对象。具有极快的查找速度。
#            2.是一个无序、以键值对存储的数据类型，数据关联性强、唯一一个映射数据类型
#            3.整个字典包括在花括号({})，键必须是唯一的，但值则不必。
#            4.值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组
#   字典键的特性：
#            1.不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print("dict['Name']: ", dict['Name']) # 输出：小菜鸟
#            2.键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
dict = {['Name']: 'Runoob', 'Age': 7}
print("dict['Name']: ", dict['Name']) # 报错
#    创建字典值：
d = {'key1':'values1','key2':'values2'}
# 或者
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }
#    访问字典值：
print(dict1['abc']) # 输出：456
#    添加字典值：
#             1.直接添加，若该键已存在，则会覆盖之前的值
dict1['abc'] = 'hello'
print(dict1) # 输出：hello
# 或者使用update()
dict1.update(sss=666)
print(dict1) # 输出：{'abc': hello, 'sss': 666}
#    删除字典值：
#             1.使用pop()方法
x = {'a':123,2:'hello',4:8,'b':'name'}
x.pop('a')
print(x) # 输出:{2: 'hello', 4: 8, 'b': 'name'}
#             2.del dict语句，执行 del 操作后字典不再存在：
del x[4] # 删除键为4的值
print(x) # 输出：{2: 'hello', 'b': 'name'}
#             3.使用clear清空字典
x.clear()
print(x) # 输出：{}空字典
# 字典常用操作：
#    keys()方法：
#              返回字典中的键
c = {'a':123,2:'hello',4:8,'b':'name'}
print(c.keys()) # 输出字典所有键：dict_keys(['a', 4, 2, 'b'])
#    values()方法：
#                返回字典中的键
print(c.values()) # 输出字典所有值：dict_values([8, 'hello', 123, 'name'])
#     items()方法：
#                返回可遍历的(键, 值) 元组数组
print(c.items()) # 输出字典元组数组：dict_items([('b', 'name'), (2, 'hello'), (4, 8), ('a', 123)])
# setdefault()方法：
#                 如果该键存在字典中则打印该键的值，如该键不存在字典中，则打印添加键并将值设为默认值，对原字典不造成影响
print(c.setdefault(2,None)) # 输出：hello
print(c.setdefault(3,9))    # 输出：9