# 函数的作用 - 代码的坏味道 / 用函数封装功能模块
# 定义函数 - def语句 / 函数名 / 参数列表 / return语句 / 调用自定义函数
# 调用函数 - Python内置函数 / 导入模块和函数
# 函数的参数 - 默认参数 / 可变参数 / 关键字参数 / 命名关键字参数
# 函数的返回值 - 没有返回值 / 返回单个值 / 返回多个值
# 作用域问题 - 局部作用域 / 嵌套作用域 / 全局作用域 / 内置作用域 / 和作用域相关的关键字
# 用模块管理函数 - 模块的概念 / 用自定义模块管理函数 / 命名冲突的时候会怎样（同一个模块和不同的模块）

# 函数：
#    python系统中自带的一些函数叫做内置函数，比如dir(),type()等，不需要我们自己编写。还有一种第三方函数，就是其他程序员编好的一些函数，给大家使用
# 以上两种函数都可以直接拿来使用，最后一种是自己编写的方便自己工作学习用的函数，叫做自定义函数。
#    函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。函数能提高应用的模块性，和代码的重复利用率。
# 空函数：
#    如果想定义一个什么事也不做的空函数，可以用pass语句，pass可以用来作为占位符，比如现在还没怎么想好写函数代码，
# 先放一个pass，让其他代码能运行起来，缺少了pass，代码运行就会有语法错误，比如：
#     def age >= 18:
#          pass

# 定义函数：
#       函数代码块以def关键词开头，后接函数标识符名称和圆括号(),后面再接上冒号
#       任何传入的参数和自变量必须放在圆括号内，圆括号之间可以用于定义参数
#       函数名必须以下划线或者字母开头，可以包含数字、字母、下划线等组合，不可以包含标点符号
#       函数名称不能一样，如果一样那么后面的函数定义覆盖前面的定义
#       函数名如果一样，但是大小写不一样，是可以的，算作两个不同的函数
#       函数名能不能使用保留字，同样会将内置函数覆盖掉
#       定义函数的时候，如果对函数进行注释，使用三个引号的注释方式
#       函数的第一行语句可以选择性地使用文档字符串——用于存放函数说明
#       函数内容以冒号起始，并且缩进
#       return[表达式]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回None,函数执行完毕也没有return语句时,自动return None
#  语法：
def functionname(parameters):
       '''函数_文档说明'''
      #  function_suite
      # return[expression]
#  实例：以下是一个简单的python函数，它将一个字符数串作为传入参数，再打印到显示设备上
#      def greet_user():           # 定义函数
#        '''显示简单的问候语'''     # 函数说明文档
#         print('hello!')
#      greet_user()                # 调用自定义函数

# 调用函数：
#    Python内置函数：
#    数学运算(15个): abs(x)                # 求绝对值:参数可以是整型，也可以是复数,若参数是复数，则返回复数的模
#                 complex([real[,imag]]) # 创建一个复数
#                 divmod(a,b)                # 分别取商和余数,注意：整型、浮点型都可以
#                 float([x])             # 将一个字符串或数转换为浮点数。如果无参数将返回0.0
#                 int([x[,base]])        #    将一个字符转换为int类型，base表示进制
#                 long([x[,base]])       # 将一个字符转换为long类型
#                 pow(x, y[,z])          # 返回x的y次幂
#                 range([start],stop[,step]) # 产生一个序列，默认从0开始
#                 round(x[,n])          # 四舍五入
#                 sum(iterable[,start])  # 对集合求和
#                 oct(x)                # 将一个数字转化为8进制
#                 hex(x)                # 将整数x转换为16进制字符串
#                 chr(i)                # 返回整数i对应的ASCII字符
#                 bin(x)                # 将整数x转换为二进制字符串
#                 bool([x])             # 将x转换为Boolean类型
#  集合类操作(15个):basestring()                   # str和unicode的超类，不能直接调用，可以用作isinstance判断
#                   format(value [, format_spec])      # 格式化输出字符串，格式化的参数顺序从0开始，如“I am {0},I like {1}”
#                   unichr(i)                          # 返回给定int类型的unicode
#                   enumerate(sequence [, start = 0])    # 返回一个可枚举的对象,该对象的next()方法将返回一个tuple
#                   iter(o[, sentinel])            # 生成一个对象的迭代器，第二个参数表示分隔符
#                   max(iterable[, args...][key])   # 返回集合中的最大值
#                   min(iterable[, args...][key])      # 返回集合中的最小值
#                   dict([arg])                    # 创建数据字典
#                   list([iterable])                   # 将一个集合类转换为另外一个集合类
#                   set()                              # set 对象实例化
#                   frozenset([iterable])              # 产生一个不可变的set
#                   str([object])                  # 转换为string类型
#                   sorted(iterable[, cmp[, key[, reverse]]])    # 队集合排序
#                   tuple([iterable])              # 生成一个tuple类型
#                   xrange([start], stop[, step])   # xrange()函数与range()类似,但xrnage()并不创建列表,而是返回一个xrange对象,
                                                  # 它的行为与列表相似,但是只在需要时才计算列表值,当列表很大时,这个特性能为我们节省内存
#   逻辑判断(3个):all(iterable) # 集合中的元素都为真的时候为真,特别的，若为空串返回为True
#                any(iterable)   # 集合中的元素有一个为真的时候为真,特别的，若为空串返回为False
#                cmp(x, y)       # 如果x < y ,返回负数；x == y, 返回0；x > y,返回正数
#   反射(33个)：callable(object)   # 检查对象object是否可调用
                                # 1、类是可以被调用的
                                # 2、实例是不可以被调用的，除非类中声明了__call__方法
              # classmethod()        # 1、注解，用来说明这个方式是个类方法
              #                   # 2、类方法即可被类调用，也可以被实例调用
              #                   # 3、类方法类似于Java中的static方法
              #                   # 4、类方法中不需要有self参数
              # compile(source,filename,mode[,flags[,dont_inherit]])
              #                   # 将source编译为代码或者AST对象。代码对象能够通过exec语句来执行或者eval()进行求值。
              #                   # 1、参数source：字符串或者AST（Abstract Syntax Trees）对象。
              #                   # 2、参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
              #                   # 3、参数model：指定编译代码的种类。可以指定为 ‘exec’,’eval’,’single’。
              #                   # 4、参数flag和dont_inherit：这两个参数暂不介绍
              # dir([object])        # 1、不带参数时，返回当前范围内的变量、方法和定义的类型列表；
              #                   # 2、带参数时，返回参数的属性、方法列表。
              #                   # 3、如果参数包含方法__dir__()，该方法将被调用。当参数为实例时。
              #                   # 4、如果参数不包含__dir__()，该方法将最大限度地收集参数信息
              # delattr(object, name)    # 删除object对象名为name的属性
              # eval(expression [,globals [,locals]])    # 计算表达式expression的值
              # execfile(filename [,globals [,locals]])  # 用法类似exec()，不同的是execfile的参数filename为文件名，而exec的参数为字符串。
              # filter(function,iterable)    # 构造一个序列，等价于[ item for item in iterable if function(item)]
              #                  # 1、参数function：返回值为True或False的函数，可以为None
              #                  # 2、参数iterable：序列或可迭代对象
              # getattr(object, name [, defalut]) # 获取一个类的属性
              # globals()          # 返回一个描述当前全局符号表的字典
              # hasattr(object, name)    # 判断对象object是否包含名为name的特性
              # hash(object)    # 如果对象object为哈希表类型，返回对象object的哈希值
              # id(object)      # 返回对象的唯一标识
              # isinstance(object, classinfo)    # 判断object是否是class的实例
              # issubclass(class, classinfo) # 判断是否是子类
              # len(s)          # 返回集合长度
              # locals()            # 返回当前的变量列表
              # map(function, iterable, ...)     # 遍历每个元素，执行function操作
              # memoryview(obj)  # 返回一个内存镜像类型的对象
              # next(iterator[, default])    # 类似于iterator.next()
              # object()            # 基类
              # property([fget[, fset[, fdel[, doc]]]])  # 属性访问的包装类，设置后可以通过c.x=value等来访问setter和getter
              # reduce(function, iterable[, initializer])    # 合并操作，从第一个开始是前两个参数，然后是前两个的结果与第三个合并进行处理，以此类推
              # reload(module)   # 重新加载模块
              # setattr(object, name, value) # 设置属性值
              # repr(object)        # 将一个对象变幻为可打印的格式
              # slice（）  　
              # staticmethod    # 声明静态方法，是个注解
              # super(type[, object-or-type])    # 引用父类
              # type(object)     # 返回该object的类型
              # vars([object])   # 返回对象的变量，若无参数与dict()方法类似
              # bytearray([source [, encoding [, errors]]])  # 返回一个byte数组
                               # 1、如果source为整数，则返回一个长度为source的初始化数组；
                               # 2、如果source为字符串，则按照指定的encoding将字符串转换为字节序列；
                               # 3、如果source为可迭代类型，则元素必须为[0 ,255]中的整数；
              #                  # 4、如果source为与buffer接口一致的对象，则此对象也可以被用于初始化bytearray.
              # zip([iterable, ...]) # 实在是没有看懂，只是看到了矩阵的变幻方面
#   I/O操作(5个)：file(filename [, mode [, bufsize]])  # file类型的构造函数，作用为打开一个文件，如果文件不存在且mode为写或追加时，文件将被创建。添加‘b’到mode参数中，将对文件以二进制形式操作。添加‘+’到mode参数中，将允许对文件同时进行读写操作
                                                   # 1、参数filename：文件名称。
                                                   # 2、参数mode：'r'（读）、'w'（写）、'a'（追加）。
                #                                    # 3、参数bufsize：如果为0表示不进行缓冲，如果为1表示进行行缓冲，如果是一个大于1的数表示缓冲区的大小 。
                # input([prompt])    # 获取用户输入，推荐使用raw_input，因为该函数将不会捕获用户的错误输入
                # open(name[, mode[, buffering]])    # 打开文件，与file有什么不同？推荐使用open
                # print  # 打印函数
                # raw_input([prompt])    # 设置输入，输入都是作为字符串处理
# 函数的参数：
#   位置参数：
def y(x):
  return x*x
# 对于y(x)函数，参数x就是一个位置参数，当我们调用y函数时，必须传入有且仅有的一个参数x
#   现在如果要计算x的n次方怎么办？
def y(x,n):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
        return s
#            修改后的y(x,n)函数，有了两个参数：x和n，都是位置参数，调用函数时，传入的两个值按位置顺序依次赋给参数x和n
#   默认参数：新的y(x,n)没问题，但是旧的调用代码失败了，原因是我们增加了一个函数，导致旧代码因为缺少一个参数而无法正常调用：
#            这时候默认参数就派上用场了，由于我们计算x的平方，所以，可以把第二个参数n的默认值设定为2：
def y(x,n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
        return s
#            默认参数可以简化函数的调用，设置默认参数时，有几点要注意：
#            1.必选参数在前，默认参数在后，否则Python的解释器会报错
#           2.如何设置默认参数，当有多个参数时，把变化最大的参数放前面，变化小的参数放后面。变化小的参数可以作为默认参数
#            3.默认参数必须指向不变对象
#   关键字参数：可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数
#             这些关键字参数在函数内部自动组装为一个dict。如：
def person(name,age,**kw):
    print('name',name,'age',age,'other',kw)
person('jijuntao',30)              # 函数person()除了必选参数name和age外，还接受关键字参数kw
person('jijuntao',30,city='beijing') # 传入任意个数的关键字参数
#  命名关键字参数：对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
#                如果要限制关键字的名字，就可以用命名关键字参数，例如，只接受city和job作为关键字参数：
def person(name,age,*,city,job):
    print(name,age,city,job)
#                命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#                如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不在需要一个特殊分割符*了：
def person(name,age,*args,city,job):
    print(name,age,city,job)
#                命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
#    组合参数：在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#            但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#    *args是可变参数
#    **kw是关键字参数
# 函数的返回值：1.函数返回值可以是任意数据类型
#             2.如果有返回值：必须要用变量接受才会有效果
#   没有返回值：函数可以没有返回值，默认返回None，函数的返回值为None有三种情况：
#             1.不写返回值
#             2.只写一个return
#             3.return None（几乎不用）
#  retuern的作用：结束一个函数的执行
#  返回一个值(一个变量)
#  返回多个值(多个变量)，多个值之间用逗号区分
#  接收：可以用一个变量接收，以元组的形式返回
#        也可以用多个变量接收，返回几个就用几个变量去接收
def func6():   # 返回一个值
    a = 123
    return a
    def func7():   # 返回多个值
        a = 123
        b = 'abc'
        return a,b

# 作用域：函数的四个作用域顺序为局部作用域-嵌套作用域-全局作用域-内置作用域
#    局部作用域：在函数中定义的变量，包括参数，都被成为局部变量。每个函数执行时，系统都会为该函数分配一块“临时内存空间”，
# 所有的局部变量都被保存在这块临时空间内，当函数执行完成后，这块内存空间就被释放了，这些全局变量也就失效了，因此离开函数之后就不能访问局部变量了。
#    全局作用域：定义在函数外的拥有全局作用域，可以在整个范围内访问
total = 0                     # 这是一个全局变量
def sum(arg1,arg2):           # 定义2个参数
    total= arg1 + arg2       # total在这里是局部变量
    print('函数内是局部变量') # 返回的结果是30
    print('函数内是全局变量') # 返回的结果是0
sum(10,20)                    # 调用sum函数
#   内置作用域：查看相关内置函数
#   嵌套作用域：在函数里面还可以定义函数，可以嵌套多层，执行需要被调用
name = 'hanke'
def change_name():
    def change_name2():
        name = 'hanke2'
        print('第二次打印')
    change_name2()      # 调用内层函数
    print('第一次打印')   # 结果：hanke
change_name()             # 结果：hanke
print(name)               # 结果：hanke
#   闭包：在Python中一个内嵌的函数可以访问它外部的变量，且外部函数返回内嵌函数的调用，这样就形成了一个闭包函数
def foo():
    num=1
    def add(n):
        nonlocal  num
        num += n
        return num
    return add
f=foo()
print(f(1))  #2
print(f(2))  #4
#   作用域关键字：当局部变量域想修改全局变量时，就要用到global和nonlocal关键字
#       nonlocal关键字：内层函数改变外层函数变量用nonlocal，nonlocal不能定义新的外层函数变量，只能改变已有的外层函数变量
#                      同时nonlocal不能改变全局变量，只能用于嵌套函数中
#           二者区别：1.两者功能不同。global关键字修饰变量后标识该变量是全局变量，对该变量进行修改就是修改全局变量，而nonlocal关键字修饰
#           变量后标识该变量是上一级函数中的局部变量，如果上一级函数中不存在该局部变量，nonlocal位置会发生错误
#          （最上层的函数使用nonlocal修饰变量必定会报错）。
#                   2.两者使用的范围不同。global关键字可以用在任何地方，包括最上层函数中和嵌套函数中，即使之前未定义该变量，
#          global修饰后也可以直接使用，而nonlocal关键字只能用于嵌套函数中，并且外层函数中定义了相应的局部变量，否则会发生错误
#       一、global关键字：
#           1.用于在局部作用域中修改全局变量
a = 10  # a1 当前模块全局变量
def outer():
    a = 9  # a2 当前outter作用域局部变量
    def inner():
        global a
        a = 8  # a3 既是全局变量a1，又是inner局部变量
        print(a)  # a3 8,在inner的局部作用域中找到了a3       结果：8
    inner()  # inner()函数结束，a3作为全局变量被保留下来成为a1
    print(a)  # a2 9,在outer局部作用域中找到a2，             结果：9
outer()  # outer()函数结束，a2作为outer局部变量被释放
print(a)  # a1 8, 在当前模块全局作用域中找到了a1              结果：8
#        此时a1=a3=8，都是全局变量
#            2.若没有在外部定义全局变量a，在局部作用域中加global关键字依然能声明一个变量为全局变量
def outer():
    a = 9  # a2 当前outter作用域局部变量
    def inner():
        global a
        a = 8  # a3  既是inner局部变量，又是模块全局变量
        print(a)  # a3 8 在inner的局部作用域中找到了a3    结果：8
    inner()  # inner()函数结束，a3作为全局变量被保留下来
    print(a)  # a2 9,在outer局部作用域中找到a2           结果：9
outer()  # outer()函数结束，a2作为outer局部变量被释放
print(a)  # a3 8在当前模块全局作用域中找到了a3             结果：8
#           3.outer()没有局部变量a，则往上使用全局变量a
def outer():
    def inner():
        global a
        a = 8  # a3  既是inner局部变量，又是模块全局变量
        print(a)  # a3 8，在inner的局部作用域中找到了a3    结果：8
    inner()  # inner()函数结束，a3作为inner局部变量被释放
    print(a)  # a3 9,在outer局部作用域中没找到a，往上在全局作用域中找到了全局变量a3  结果：8
outer()  # outer()函数结束，a2作为outer局部变量被释放
print(a)  # a3 8，在当前模块全局作用域中找到了a3           结果：8
#       二、nonlocal关键字：声明此变量与外层同名变量为相同变量
#           1.用于内存函数中改变外层函数
a = 10  # a1 当前模块全局变量
def outer():
    a = 9 # a2 outer局部变量
    def inner():
        nonlocal a   # a2 outer局部变量改变为a3局部变量
        a = 8  # a3  既是inner局部变量，又是外层outer局部变量
        print(a)  # a3 8，在inner的局部作用域中找到了a3                  结果：8
    inner()  # inner()函数结束，a3作为外层变量(outer局部变量)被保留成为a2
    print(a)  # a2 8,在outer局部作用域中找到a2（在inner中被改变）         结果：8
outer()  # outer()函数结束，a2作为outer局部变量被释放
print(a)  # a1 10，在当前模块全局作用域中找到了a1                         结果：10
#       此时a2、a3为同一变量
#           2.如果在外层没有找到变量a，则会继续向外层找，直至到全局变量作用域的下一层为止
a = 10  # a1 当前模块全局变量
def outer2():
    a = 9 # a2 outer2作用域局部变量
    print(a) # a2 9,还未被a3改变
    def outer1():
        print(a) # a2 9,在outer1中没找到局部变量a，则寻找外层(outer2)变量a2(还未被a3改变)
        def inner():
            nonlocal a
            a = 0  # a3 既是inner局部变量，又是再外层outer2作用域变量
            print(a)  # a3 0, 找到inner局部变量a3                                 结果：0
        inner()  # inner()函数结束，a3作为外层变量(outer2局部变量)被保留成为a2
        print(a)  # a2 0,在outer1中没找到局部变量a，则寻找外层(outer2)变量a2(被a3改变) 结果：0
    outer1()
    print(a) # a2 0, 在outer1中找到outer1局部变量a2(被a3改变)                       结果：0
outer2()
print(a)  # a1 10，在当前模块全局作用域中找到了a1                                    结果：10
#           3.全局变量不是外层变量，不被nonlocal寻找
a = 10  # a1 当前模块全局变量
def outer():
    def inner():
        nonlocal a  # 在当前作用域外层即outer局部作用域中没找到outer局部变量a，outer外层为全局作用域，nonlocal不继续寻找，报错
        a = 8
        print(a)
    inner()
    print(a)
outer()
print(a)  # a1 10，在当前模块全局作用域中找到了a1

# 用模块管理函数：
#     概念：Python模块(Module)，是一个Python文件，以.py结尾，包含了Python对象定义和Python语句。
#          模块让你能够有逻辑地组织你的Python代码段
#          把相关的代码分配到一个模块里能让你的代码更好用，更易懂
#          模块能定义函数，类和变量，模块里也能包含可执行的代码
#     导入模块：1.import语句
#             模块定义好后，我们可以使用import语句来引入模块，语法如下：
#               import module
#             比如要引用模块 math，就可以在文件最开始的地方用 import math 来引入。在调用 math 模块中的函数时，必须这样引用：模块名.函数名
#               import support       # 导入模块
#               support.print('你好') # 调用模块里包含的函数
#             一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
#             2.from...import语句
#             Python的from语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
#               from modname import name
#             比如要导入模块fib的fibonacci函数，使用如下语句：
#               from fib import fibonacci
#             这个声明不会把整个fib模块导入到当前命名空间，只会将fib里的fibonacci单个引入到这个声明的模块的全局符号表
#             可在当前空间直接使用fibonacci，无需加前缀fib.
#             3.from...import * 语句
#             把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
#               from modname import *
#             这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。
#     使用as给函数指定别名：
#             如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名 别名 ——函数的另一个名称，类似于外号。
#               下面给函数make_pizza() 指定了别名mp() 。这是在import 语句中使用make_pizza as mp 实现的，关键字as 将函数重命名为你提供的别名：
#               from pizza import make_pizza as mp
#              通用语法：
#               from module_name import function_name as fn
#      使用as给模块指定别名：
#              如给模块pizza 指定别名p：
#               import pizza as p
#              上述import 语句给模块pizza指定了别名p，但该模块中所有函数的名称都没变。调用函数make_pizza() 时，
#              编写代码p.make_pizza()而不是pizza.make_pizza()，这样不仅能使代码更简洁，还可以让你不再关注模块名，而专注于描述性的函数名。
#              通用语法：
#               import module_name as mn

