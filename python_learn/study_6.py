# 类和对象 - 什么是类 / 什么是对象 / 面向对象其他相关概念
# 定义类 - 基本结构 / 属性和方法 / 构造器 / 析构器 / __str__方法
# 使用对象 - 创建对象 / 给对象发消息
# 面向对象的四大支柱 - 抽象 / 封装 / 继承 / 多态
# 属性 - 类属性 / 实例属性 / 属性访问器 / 属性修改器 / 属性删除器 / 使用__slots__
# 类中的方法 - 实例方法 / 类方法 / 静态方法
# 继承和多态 - 什么是继承 / 继承的语法 / 调用父类方法 / 方法重写 / 类型判定 / 多重继承 /

# 类和对象 - 什么是类 / 什么是对象 / 面向对象其他相关概念
#    类：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例
#    对象：通过类定义的数据结构实例。对象包括两个数据成员(类变量和实例变量)和方法
#    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
#   实例变量：在类的声明中，属性是用变量来表示的。这种变量称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的

# 定义类 - 基本结构 / 属性和方法 / 构造器 / 析构器 / __str__方法
#    定义类：在Python中，定义类是通过class关键字，class后面紧接着是类名，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类
#           继承下来的，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类，最后以冒号结尾。例如：
class Student(object):
    pass
#           定义好类后，可以根据Student类创建Student的实例，创建实例是通过类名+()实现的：
bart = Student()
print(bart) # 输出：<__main__.Student object at 0x000001BF92FCD160>
# 可以看到，变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类
#     属性：可以使用点好.来访问对象的实例。如给bart实例变量绑定name属性
bart.name = 'keety'
print(bart.name) # 输出：keety
#       由于类可以起到模板的作用，因此，在创建类实例的时候，把一些我们认为必须绑的属性强制填写进去。通过定义一个特殊的_init_方法，在创建
#       实例的时候，就把name，age，weight等属性绑上去：
class People(object):
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
#  注意到_init_方法的第一个参数永远是self，表示创建的实例本身，因此，在_init_方法内部就可以把各种属性绑定到self，因为self指向创建的实例本身
bart = People('kety',19,'52kg')
print(bart.name) # 输出：kety
print(bart.age) # 输出：19
print(bart.weight) # 输出：52kg
#  和普通函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且调用时，不用传递参数。除此之外，类的方法和普通函数
#  没什么区别，仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
#     方法：既然People实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在People类的内部定义访问数据的函数，
#          这样，就把“数据”给封装起来了。这些封装数据的函数是和People类本身是关联起来的，我们称之为类的方法：
class Worker(object):
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def lss(self):
        print(self.name,self.age,self.weight)
less = Worker('jijuntao', 19, '52kg')
less.lss()
#     类的构造：_init_构造函数，在生成对象是调用
#             由于类可以起到模板的作用，因此，可以再创建实例的时候，把一些我们认为必须绑定的属性强制填写进去
#             通过定义一个特殊的_init_方法，可以再创建实例的时候，就把name和sex等属性绑上去
#             类的方法与普通函数只有一个特别的区别——他们必须有一个额外的第一个参数名称，按惯例他的名称是self
#             有了_init_方法后，创建实例的时候，传入参数便不能为空，必须传入与_init_中方法匹配的参数
#             而self代表的是累的实例，该参数不需要另外进行传入
class Ren():
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def people(self):
        print('你好：',self.name,self.sex)
peo = Ren('mike','man')
peo.people()
#     类的析构：当一个对象（实例）的引用次数为0时，会被自动调用_del_释放方法
#             此方法一般无需定义，因为python是一门高级语言，可自动触发执行
#             析构函数的调用是由解释器在进行垃圾回收时自动触发执行的
class Ren():
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def people(self):
        print('你好：',self.name,self.sex)
peo = Ren('mike','man')
peo.people()
del peo # 删除对象，才会触发
#    _str_用法：如果要把一个类的实例变成字符串(str)，就需要实现特殊方法_str_():,不使用_str_，print打印出来是个对象，使用了就是字符串
#                python定义了_str_()和_repr_()两种方法，_str_()用于显示给用户，而_repr_()用于显示给开发人员
class Qick(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return '名字:%s 年龄：%d' % (self.name,self.age)
b = Qick('cc',16)
print(b)


# 使用对象 - 创建对象 / 给对象发消息
# 创建对象的根本途径是构造方法，调用某个类的构造方法即可创建这个类的对象
class Person(object):             # 定义Person类
    hair = 'black'                # 定义个类变量hair
    def __init__(self,name,age):  # 定义2个实例变量
        self.name = name
        self.age = age
    def say(self,content):        # 定义一个say方法
        print(content)
p = Person('mike',18)             # 调用类的构造方法，创建Person对象，赋值给p变量
print(p.name,p.age)  # 输出：mike，18
p.name = '李刚'                   #访问p的name实例变量，直接给该实例变量重新复制
print(p.name,p.age)  # 输出：李刚，18


# 面向对象的四大支柱 - 抽象 / 封装 / 继承 / 多态
#     抽象类：抽象类是一个特殊的类，它的特殊之处在于只能被继承，不能被实例化，需要借助模块实现
#    为什么要抽象：如果类是从一堆对象中抽取相同的内容而来，那么抽象就是从一堆类中抽取相同的内容而来，内容包含数据属性和函数属性
#               比如我们有香蕉类，有苹果类，从这些类抽取相同的内容就是水果这个类，我们无法迟到叫水果这种东西
#    类是从现实对象抽象而来，抽象类就是基于类抽象而来
import abc                           # 利用模块实现抽象类
class file(metaclass=abc.ABCMeta):
    all_type = 'file'
    def read(self):                  # 定义抽象类方法，子类必须继承读功能
        pass
    def write(self):                 # 定义抽象类方法，子类必须继承写功能
        pass

class Txt(file):                     # 子类继承抽象类，但必须定义read和write方法，否则报错
    def read(self):
        print('文档读取方法')          # 继承read方法
    def write(self):                 # 继承write方法
        print('文档的读取方法')
qwer = Txt
print(qwer.all_type)                 # 输出：file
#    封装：我们在看待一个类时，只需要给出所需的属性数据，而如何打印这些数据都是在类中定义好的，这样调用容易，却不知道内部函数的细节
#         这个过程就是封装。比如
class Ren(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return '姓名：%s 年龄：%d' % (self.name,self.age)
# 以上过程称作封装
ren =Ren('hello',18) # 调用
print(ren)
#    继承：继承就是实现代码复用的方法之一。可以理解成类之间的类型和子类型关系，需要注意的是：继承语法 class 派生类名（基类名）
#       优点：如果需要定义好几个类，而类与类之间有一些公共的属性和方法，这时就可以把相同的属性和方法作为基类的成员，而特殊的方法及属性则
#            在本类中定义，这样只需要继承基类这个动作，就可以访问到基类的属性和方法，提高代码的可扩展性
#       缺点：可能特殊的本类又有其他特殊的地方，又会定义一个类，其下也可能在定义类，这样就会造成继承的那条线越来越长，使用继承的话，任何一点
#            小的变化也需要重新定义一个类，很容易引起爆炸式增长，所以尽可能遵守“多用组合少用继承”的原则
#       特点：1.在继承中基类的构造_init_()方法不会被自动调用，它需要在其派生类的构造中亲自专门调用
#            2.在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数并不需要带上self参数
#            3.python总是先查找对应类的方法，如果在派生类中找不到，就到基类中逐个查找。
class Animal:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def eat(self):
        print('吃饭')
class Dogs(Animal):                        # 定义子类
    def __init__(self,name,age,sex,color): # 继承父类的属性以及自己特有属性color
        super().__init__(name,age,sex)
        self.color = color
    def drink(self):
        print('喝水')
class Dog(Dogs):                            # 定义子类的子类
    def run(self):
        print('跑步')
        super().drink()                     # 在需要的位置调用父类的方法，用super().父类方法名
        print('柯基喝水')
    def drink(self):
        print('柯基柯基')

keji = Dog('柯基',10,'man','yellow')
keji.eat()                                   # 调用父类的父类方法，输出：吃饭
keji.drink()                                 # 调用父类方法，输出：喝水
keji.run()                                   # 调用本类方法，输出：跑步，喝水，柯基喝水
#如果在开发中，子类的方法实现，包含了父类的方法实现，即原本父类封装的方法是子类方法的一部分，这时候就可以使用子类扩写父类的方法
#扩写方式：
# 1.在子类中重写父类的方法；
# 2.在需要的位置，调用父类的方法，用super().父类方法名
# 3.编写子类方法其他的代码

#     多态：让具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容（功能）的函数
#        特点：1.只关心对象的实例方法是否同名，不关心对象所属的类型
#             2.对象所属的类之间，继承关系可有可无
#             3.多态的好处可以增加代码的外部调用灵活度，让代码更加通用，兼容性比较强
#             4.多态是调用方法的技巧，不会影响到类的内部设计
class Animal(object):
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(self.name,'叫')
    def animal_talk(self):           # 多态
        self.talk()
class Cat(Animal):
    def talk(self):
        print('%s:喵喵喵' % self.name) # 重写talk方法
class Dog(Animal):
    def talk(self):
        print('%s:汪汪汪' % self.name)
a = Dog('柯基')
Animal.animal_talk(a)                 # 调用多态
#      如何实现多态：写一个方法，它只接收父类作为参数，编写的代码只与父类打交道。调用这个方法时，实例化不同的子类对象（new 一个对象）。
# 更具体的说：
#（1）子类重写父类的方法。使子类具有不同的方法实现。
#（2）把父类类型作为参数类型，该父类及其子类对象作为参数转入。
#（3）运行时，根据实际创建的对象类型动态决定使用那个方法。


# 属性 - 类属性 / 实例属性 / 属性访问器 / 属性修改器 / 属性删除器 / 使用__slots__
# 类属性：类属性是声明在类型的内部，方法的外部的属性
# 实例属性：_init_内定义的属性，通过self声明的属性，是实例对象所特有的属性，而实例对象是类创建的对象
#         类属性可以用类名访问，具有读写权限，也可以用实例名访问，但实例访问时只能读。当实例访问类不存在的属性时，会在实例中新建属性。
# 注意：实例属性优先级比类属性优先级高，若使用相同的名字，实例属性将屏蔽类属性
#      类不能调用实例属性，实例可以调用类的属性
class Tenent():
    i = 10  # 此处i是类属性
    def __init__(self,name,age):
        self.name = name
        self.age = age   # 此处name，age为实例属性
    def function(self):  # 实例方法
        print(self.name)
        print(self.age)
a = Tenent(100,200)
print(a.i) # 实例调用类属性，输出：10
print(a.name) # 实例调用实例属性，输出：100
print(Tenent.i) # 类调用类属性，输出：10
print(Tenent.name) # 类调用实例属性，报错，类无法调用实例属性
Tenent.i += 1  # 此时i = 11
print(a.i)     # 输出：11
print(Tenent.i) # 输出：11
a.i += 1  # 使用实例修改类属性时，修改后的属性只对该类有效果i=11，不改变原类属性i=10，相当于创建了个副本
print(a.i) # 因是实例调用类的属性，所以使用修改后的类属性值，输出：11
print(Tenent.i) # 使用类调用类属性，所以类属性值未改变，输出：10
# 总的来说，类和实例对于属性的修改权限其实有作用域的问题，类有权限修改属性，而实例没有，于是实例就在自己的内存范围内创建一个实例名+属性名的副本
# 调用的时候就是用这个。

# __slots__：当一个类需要创建大量实例时，可以通过_slots_声明实例所需要的属性。
# 假如只允许向class中添加name属性和age属性，就可以在定义class的时候，定义一个_slots_变量来限制class能添加的属性
class Student:
    pass
s1 = Student # 创建实例
s1.name = 'jijuntao' # 定义实例属性
s1.age = '23'
s1.sex = '男'
print(s1.name,s1.age,s1.sex) # 输出：jijuntao，23，男
class Student():
    __slots__ = ('name','age')
    pass
s1 = Student() # 创建实例
s1.name = 'jijuntao' # 定义实例属性
s1.age = '23'
s1.sex = '男'
print(s1.name,s1.age,s1.sex) # 报错，'Student' object has no attribute 'sex'，因为限制Student类只能添加name和age属性
# 注意：_slots_定义的属性仅仅对当前类起作用，对继承的子类不起作用


# 类中的方法 - 实例方法 / 类方法 / 静态方法
#  实例方法：
#     定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可传递类的属性和方法）
#     调用：只能由实例对象调用
#  类方法：
#     定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定“cls”，通过它来传递类的属性和方法（不可传递实例属性和方法）
#     调用：实例对象和类对象都可调用
#   静态方法：
#     定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法
#     调用：实例对象和类对象都可以调用
#  实例方法：
#   就是类的实例能够使用的方法
#  类方法：
#    使用装饰器@classmethod，原则上，类方法是将类本身作为对象进行操作的方法，假设有个方法，在逻辑上采用类本身作为对象来调用更合理，那么这个
#    方法就可以定义为类方法。
#  静态方法：
#    使用装饰器@staticmethod，静态方法是类中的函数，不需要实例，不涉及类中的属性和方法操作。静态方法是独立的、单纯的。
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def ren(self): # 只可通过对象调用该方法，无法通过类调用该方法，如People.ren()会报错
        print(self.name,self.age)
    @classmethod # 装饰器，类方法
    def ren1(cls): # 类方法，cls代表类本身
        print('这是一个类方法')
    @staticmethod # 装饰器，静态方法
    def ren2(): # 静态方法，不含参数
        print('这是一个静态方法')
p = People('jijuntao',28)
p.ren() # 对象调用ren()方法，输出：jijuntao 28
People.ren() # 报错
p.ren1() # 对象调用类方法ren1(),输出：这是一个类方法
People.ren1() # 类调用类方法ren1()，输出：这是一个类方法
p.ren2() # 对象调用静态方法ren2()，输出：这是一个静态方法
People.ren2() # 类调用静态方法ren2()，输出：这是一个静态方法


# 继承和多态 - 什么是继承 / 继承的语法 / 调用父类方法 / 方法重写 / 类型判定 / 多重继承 /
#    继承定义：继承就是实现代码复用的方法之一。可以理解成类之间的类型和子类型关系
#    继承语法：class 派生类名（基类名）
#    调用父类：1.可直接调用
#            2.可使用super().调用
class Dogs():
    def heshui(self):
        print('小狗喝水')
class Dog(Dogs):
    pass
bomei = Dog()
bomei.heshui() # 直接调用，输出：小狗喝水
# 或者
class Dogs():
    def heshui(self):
        print('小狗喝水')
class Dog(Dogs):
    def heshui(self):
        super().heshui() # 使用super调用
bomei = Dog()
bomei.heshui()

#     方法重写：直接重写，在子类中定义和父类相同名称的方法名
class Dogs():
    def heshui(self):
        print('小狗喝水')
class Dog(Dogs):
    def heshui(self):
        print('小猫喝水') # 直接重写
bomei = Dog()
bomei.heshui()

#    多重继承：
class Human(object):            # 定义父类Human
    def __init__(self,sex):
        self.sex = sex
    def p(self):
        print('这是Human类的方法')
class People(object):           # 定义父类People
    def __init__(self,name):
        self.name = name
    def p(self):
        print('这是People类方法')
    def people(self):
        print('这是people特有的方法')
class Teather(People):          # 定义Teather子类继承People父类
    def __init__(self,name,age):
        super(Teather,self).__init__(name)  # 调用父类People中name属性
        self.age = age
class Student(Human,People):    # 定义Student同时类继承Human类和People类
    def __init__(self,sex,name,grade):
      # super().__init__(sex)   注意：多于多继承来说，使用super智慧调用第一个父类属性
      # super().__init__(name)       要想调用特定父类构造器只能使用父类名.__init__()方式。如下：
        Human.__init__(self,sex)
        People.__init__(self,name)
        self.grade = grade
class peo(Human,Teather):       # 定义peo类同时继承Human类和Teather类
    def __init__(self,sex,name,age,fan):
        Human.__init__(self,sex)
        Teather.__init__(self,name,age)
        self.fan = fan
stu = Student('tom','man',100)  # 创建Student类的对象stu
print(stu.name,stu.sex,stu.grade) # 输出：tom，man，100
stu.p() # 虽然Student的父类Human和People中都有p()方法，但调用的是父类Human的方法。按照括号中继承的父类顺序调用
        # 输出：这是Human类的方法
peo1 = peo('woman','jerry',20,'打球')
peo1.people() # 因Human类中无people()方法，所以调用Teather类，Teather类继承People类，Peopler类中有people()方法，按继承顺序查找
              # 输出：这是people特有的方法
peo1.p() # Human类和People皆有p()方法，因需按继承查找，先查找Human类，如无，在查找People类，若Human类有p()方法，则查找终止
         # 输出：这是Human类方法
# 总结：1.需要注意圆括号中继承父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索
#        即方法在子类中未找到时，从左到右查找父类中是否包含方法。
#      2.支持多层父类继承，子类会继承父类所有的属性和方法，包括父类的父类的所有属性 和 方法。
#      3.不使用super调用父类方法，使用父类名.__init__(self,父类属性)

class Human:                   # 定义父类Human
    def __init__(self, sex):
        self.sex = sex
    def p(self):
        print("这是Human的方法")
    def str1(self):
        print("this si" + str(self.sex))
class Person:                 # 定义父类Person类
    def __init__(self, name):
        self.name = name
    def p(self):
        print("这是Person的方法")
    def person(self):
        print("这是我person特有的方法")
    def str2(self):
        print("this is:" + str(self.name))
class Student(Human, Person):  # 注意子类如果没有构造方法时，按括号内父类的继承顺序去继承父类构造方法，只继承一个
    def prin(self):
        print("student")
stu1=Student("男","tom") # 报错。因为子类Student没有构造方法，括号中哪个父类在最前面且它又有自己的构造函数，就继承它的构造函数
                        # HUman类只有sex属性，无name属性，所以报错
stu = Student("sex")  # 这里继承的是Huma的构造方法。
stu.p()
stu.str1()
stu.str2() # 报错，因为即使human和person都是一个参数的构造方法，但是这里继承调用的是第一个Human的构造方法
# 因为Human类有自己的构造方法，所有以上代码中Person类无用；若Human类没有自己的构造方法，则使用Person类中的构造方法
# 总结：子类从多个父类派生，而子类又没有自己的构造函数时，
#     （1）按顺序继承，哪个父类在最前面且它又有自己的构造函数，就继承它的构造函数；
#     （2）如果最前面第一个父类没有构造函数，则继承第2个的构造函数，第2个没有的话，再往后找，以此类推
