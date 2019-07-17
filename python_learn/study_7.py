# 读文件 - 读取整个文件 / 逐行读取 / 文件路径
# 写文件 - 覆盖写入 / 追加写入 / 文本文件 / 二进制文件
# 异常处理 - 异常机制的重要性 / try-except代码块 / else代码块 / finally代码块 / 内置异常类型 / 异常栈 / raise语句
# 数据持久化 - CSV文件概述 / csv模块的应用 / JSON数据格式 / json模块的应用


# I/O编程：IO在计算机中指Input/Output，也就是输入和输出。IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，
#         数据就是水管里的水，但是只能单向流动。Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。
#         对于浏览网页来说，浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。由于CPU和内存的速度远远高于外设的速度，
#         所以，在IO编程中，就存在速度严重不匹配的问题。举个例子来说，比如要把100M的数据写入磁盘，CPU输出100M的数据只需要0.01秒，可是磁盘
#         要接收这100M数据可能需要10秒，怎么办呢？有两种办法：
#         1.第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO；
#         2.CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行，这种模式称为异步IO
#     异步I/O编程比同步I/O编程复杂。这次先学习同步I/O编程

# 读文件 - 读取整个文件 / 逐行读取 / 文件路径
# 读文件：要以读文件的模式打开一个文件对象，使用Python内置函数open()函数，传入文件名和提示符：
f = open('文件路径.txt','r')
#       'r'表示读，这样就成功打开了一个文件
#       如果文件打开成功，接下来调用read()方法可以一次性读取文件内容，Python把内容读到内存，用一个str对象表示：
f.read()
#       最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，且操作系统同一时间打开的文件数量是有限的：
f.close()
#       由于文件读写时可能产生TOError，一旦出错，后面的f.close()就不会调用。为了保证无论是否出错都能正确的关闭文件，可以用try...finally
try:
    f = open('文件路径','r')
    print(f.read())
finally:
    if f:
        f.close()
#       但每次都这么写太繁琐，所以，Python引入with语句来自动帮我们调用close()方法：
with open('文件路径','r') as f:
    print(f.read())
#       这和前面的try...finally一样的，但代码更加简洁，并且不必调用f.close()

#    逐行读取：调用read()会一次性读取文件内容，如何逐行读取内容呢？
#            1.readline函数
f = open('文件路径','r')
line = f.readline()
while line:
    print(line,end='')
    line = f.readline()
f.close()
# 优点：节省内存，不需要一次性把文件内容放入内存中
# 缺点：速度相对较慢
#            2.一次读取多行数据
f = open('文件路径','r')
while 1:
    lines = f.read(1000)
    if not lines:
        break
    for line in lines:
        print(line)
f.close()
# 一次性读取多行，可以提升读取速度，但内存使用稍大，可根据情况调整一次读取的行数
#            3.直接for循环
for line in open('文件路径','r'):
    print(line)
#            4.使用fileinput模块
import fileinput
for line in fileinput.input('文件路径'):
    print(line)
# 使用简单，但速度慢（file.open）

# 写文件 - 覆盖写入 / 追加写入 / 文本文件 / 二进制文件
#    写文件：写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
# 1.覆盖写入：
f = open('文件路径','w') # 清空文件内容再写
f.write('aaa') # 只能写字符串
f.write('\n') # 换行
f.writelines(['123','\n','345','\n']) # 写入多行
# 2.追加写入
f = open('文件路径','a+') # 可读可写文件，文件不存在时就创建一个文件
f.seek(0) # 先把游标放到文件开始处，否则f.read()为空
print(f.read()) # 读取整个文件内容
f.seek(0)
for line in f:
    print(line)
f.close()
#         0:表示文件开头
#         1:表示当前位置
#         2:表示文件末尾
# 3.以'r+'或'w+'方式打开文件
f = open('文件路径','r+') # 读写模式r+，不会清空文件，但写入的内容会替换原有的内容，从文件起始位置进行替换：覆盖写入
f = open('文件路径','w+') # 写读模式w+，请求文件，光标在写入文件的末尾

# 二进制文件：
#     前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片，视频等等，用'rb'模式打开文件即可
f = open('文本路径','rb')
print(f.read())
# r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
#
# r+：打开一个文件用于读写。文件指针将会放在文件的开头。
#
# w：打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
#
# w+:打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
#
# a:打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#
# a+：打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。


# 异常处理 - 异常机制的重要性 / try-except代码块 / else代码块 / finally代码块 / 内置异常类型 / 异常栈 / raise语句
#    异常：异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。一般情况下，在Python无法正常处理程序时就会发生一个异常。
#         异常是Python对象，表示一个错误，如果你编写了处理异常的代码，程序将继续运行。
print(5/0) # 不能将一个数字除以0，所以报错:ZeroDivisionError: division by zero

#    使用try-except：
#         当你认为发生错误时，可编写一个try-except代码块来处理可能引发的异常。
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero!")
#         如果try代码块中的代码运行起来没有问题，Python将跳过except代码块；如果try代码块中的代码导致了错误，Python运行except中的代码。

#    else代码块：
#         在上述例子中还包含一个else代码块；依赖于try代码块成功执行的代码都应放到else代码块中：
print('Give me two numbers,and I will divide them')
print('Enter q to quit')
while True:
    first_number = input('\nFirst number:')
    if first_number == 'q':
        break
    second_number = input('Second number:')
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you can't divide by zero!")
    else:
        print(answer)
#         这表示如果try代码块中运行成功，则执行else代码块中的内容，如try代码块运行不成功，则执行except中的内容

#    finally代码块：
#            无论try语句中是否抛出异常，finally中的语句都会被执行
try：
    f = open('文件路径','w')
    f.write('hello')
finally:
print('closing file')
f.close()
#           不论try中写文件的过程是否异常，finally中关闭文件的操作一定会执行。由于finally的这个特性，finally经常被用来做一些清理工作

#    内置异常內型：
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
# 读文件 - 读取整个文件 / 逐行读取 / 文件路径
# 写文件 - 覆盖写入 / 追加写入 / 文本文件 / 二进制文件
# 异常处理 - 异常机制的重要性 / try-except代码块 / else代码块 / finally代码块 / 内置异常类型 / 异常栈 / raise语句
# 数据持久化 - CSV文件概述 / csv模块的应用 / JSON数据格式 / json模块的应用


# I/O编程：IO在计算机中指Input/Output，也就是输入和输出。IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，
#         数据就是水管里的水，但是只能单向流动。Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。
#         对于浏览网页来说，浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。由于CPU和内存的速度远远高于外设的速度，
#         所以，在IO编程中，就存在速度严重不匹配的问题。举个例子来说，比如要把100M的数据写入磁盘，CPU输出100M的数据只需要0.01秒，可是磁盘
#         要接收这100M数据可能需要10秒，怎么办呢？有两种办法：
#         1.第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO；
#         2.CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行，这种模式称为异步IO
#     异步I/O编程比同步I/O编程复杂。这次先学习同步I/O编程

# 读文件 - 读取整个文件 / 逐行读取 / 文件路径
# 读文件：要以读文件的模式打开一个文件对象，使用Python内置函数open()函数，传入文件名和提示符：
f = open('文件路径.txt','r')
#       'r'表示读，这样就成功打开了一个文件
#       如果文件打开成功，接下来调用read()方法可以一次性读取文件内容，Python把内容读到内存，用一个str对象表示：
f.read()
#       最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，且操作系统同一时间打开的文件数量是有限的：
f.close()
#       由于文件读写时可能产生TOError，一旦出错，后面的f.close()就不会调用。为了保证无论是否出错都能正确的关闭文件，可以用try...finally
try:
    f = open('文件路径','r')
    print(f.read())
finally:
    if f:
        f.close()
#       但每次都这么写太繁琐，所以，Python引入with语句来自动帮我们调用close()方法：
with open('文件路径','r') as f:
    print(f.read())
#       这和前面的try...finally一样的，但代码更加简洁，并且不必调用f.close()

#    逐行读取：调用read()会一次性读取文件内容，如何逐行读取内容呢？
#            1.readline函数
f = open('文件路径','r')
line = f.readline()
while line:
    print(line,end='')
    line = f.readline()
f.close()
# 优点：节省内存，不需要一次性把文件内容放入内存中
# 缺点：速度相对较慢
#            2.一次读取多行数据
f = open('文件路径','r')
while 1:
    lines = f.read(1000)
    if not lines:
        break
    for line in lines:
        print(line)
f.close()
# 一次性读取多行，可以提升读取速度，但内存使用稍大，可根据情况调整一次读取的行数
#            3.直接for循环
for line in open('文件路径','r'):
    print(line)
#            4.使用fileinput模块
import fileinput
for line in fileinput.input('文件路径'):
    print(line)
# 使用简单，但速度慢（file.open）

# 写文件 - 覆盖写入 / 追加写入 / 文本文件 / 二进制文件
#    写文件：写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
# 1.覆盖写入：
f = open('文件路径','w') # 清空文件内容再写
f.write('aaa') # 只能写字符串
f.write('\n') # 换行
f.writelines(['123','\n','345','\n']) # 写入多行
# 2.追加写入
f = open('文件路径','a+') # 可读可写文件，文件不存在时就创建一个文件
f.seek(0) # 先把游标放到文件开始处，否则f.read()为空
print(f.read()) # 读取整个文件内容
f.seek(0)
for line in f:
    print(line)
f.close()
#         0:表示文件开头
#         1:表示当前位置
#         2:表示文件末尾
# 3.以'r+'或'w+'方式打开文件
f = open('文件路径','r+') # 读写模式r+，不会清空文件，但写入的内容会替换原有的内容，从文件起始位置进行替换：覆盖写入
f = open('文件路径','w+') # 写读模式w+，请求文件，光标在写入文件的末尾

# 二进制文件：
#     前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片，视频等等，用'rb'模式打开文件即可
f = open('文本路径','rb')
print(f.read())
# r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
#
# r+：打开一个文件用于读写。文件指针将会放在文件的开头。
#
# w：打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
#
# w+:打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
#
# a:打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#
# a+：打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。


# 异常处理 - 异常机制的重要性 / try-except代码块 / else代码块 / finally代码块 / 内置异常类型 / 异常栈 / raise语句
#    异常：异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。一般情况下，在Python无法正常处理程序时就会发生一个异常。
#         异常是Python对象，表示一个错误，如果你编写了处理异常的代码，程序将继续运行。
print(5/0) # 不能将一个数字除以0，所以报错:ZeroDivisionError: division by zero

#    使用try-except：
#         当你认为发生错误时，可编写一个try-except代码块来处理可能引发的异常。
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero!")
#         如果try代码块中的代码运行起来没有问题，Python将跳过except代码块；如果try代码块中的代码导致了错误，Python运行except中的代码。

#    else代码块：
#         在上述例子中还包含一个else代码块；依赖于try代码块成功执行的代码都应放到else代码块中：
print('Give me two numbers,and I will divide them')
print('Enter q to quit')
while True:
    first_number = input('\nFirst number:')
    if first_number == 'q':
        break
    second_number = input('Second number:')
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you can't divide by zero!")
    else:
        print(answer)
#         这表示如果try代码块中运行成功，则执行else代码块中的内容，如try代码块运行不成功，则执行except中的内容

#    finally代码块：
#            无论try语句中是否抛出异常，finally中的语句都会被执行
try：
    f = open('文件路径','w')
    f.write('hello')
finally:
print('closing file')
f.close()
#           不论try中写文件的过程是否异常，finally中关闭文件的操作一定会执行。由于finally的这个特性，finally经常被用来做一些清理工作

#    内置异常內型：
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning

#    异常栈：当代码运行错误的时候，python解释器会自动打印错误的堆栈，但是程序也会戛然而止。我们可以选择把错误堆栈打印出来，同时程序继续执行下去
#           怎么操作呢？python内置的logging模块可以非常清楚的记录错误信息
import logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('最后执行了……')
# 执行结果：
# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "err_logging.py", line 8, in main
#     bar('0')
#   File "err_logging.py", line 5, in bar
#     return foo(s)*2
#   File "err_logging.py", line 3, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# 最后执行了……
# 同样出错了，但是程序处理完错误信息后会继续执行

#     raise语句：
#          程序出现错误时，系统会自动引发异常。除此之外，Python 也允许程序自行引发异常，自行引发异常使用 raise 语句来完成。
#          很多时候，系统是否要引发异常，可能需要根据应用的业务需求来决定，如果程序中的数据、执行与既定的业务需求不符，这就是一种异常。
#          由于与业务需求不符而产生的异常，必须由程序员来决定引发，系统无法引发这种异常
#      如果需要在程序中自行引发异常，则应使用 raise 语句。raise 语句有如下三种常用的用法：
#          1.raise：单独一个 raise。该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常。
#          2.raise 异常类：raise 后带一个异常类。该语句引发指定异常类的默认实例。
#          3.raise 异常对象：引发指定的异常对象。
try :
    #将用户输入的字符串以逗号（ ，）作为分隔符，分隔成两个字符串
    x_str, y_str = inputStr.split(sep =",")
# 如果要下棋的点不为空
    if board[int(y_str) - 1] [int(x_str) - 1] != "+":
# 引发默认的RuntimeError异常
    raise
    #把对应的列表元素赋为”●”
    board [int(y_str) - 1] [int(x_str) - 1] = ”●”
except Exception as e:
    print (type(e))
    inputStr = input("您输入的坐标不合法，请重新输入，下棋坐标应以x,y 的格式\n")
    continue
# 上面程序中raise代码使用raise语句来自行引发异常，程序认为当用户试图向一个已有棋子的坐标点下棋时就是异常。当 Python 解释器接收到开发者
# 自行引发的异常时，同样会中止当前的执行流，跳到该异常对应的 except 块，由该 except 块来处理该异常。也就是说，不管是系统自动引发的异常，
# 还是程序员于动引发的异常，Python 解释器对异常的处理没有任何差别

# 自定义异常类
#    很多时候，程序可选择引发自定义异常，因为异常的类名通常也包含了该异常的有用信息。所以在引发异常时，应该选择合适的异常类，
#    从而可以明确地描述该异常情况。在这种情形下，应用程序常常需要引发自定义异常。
#    用户自定义异常都应该继承 Exception 基类或 Exception 的子类，在自定义异常类时基本不需要书写更多的代码，只要指定自定义异常类的父类即可
class AuctionException(Exception):
    pass
#    上面程序创建了 AuctionException 异常类，该异常类不需要类体定义，因此使用 pass 语句作为占位符即可。在大部分情况下，
#    创建自定义异常类都可采用与程序一相似的代码来完成，只需改变 AuctionException 异常的类名即可，让该异常的类名可以准确地描述该异常。

# 数据持久化 - CSV文件概述 / csv模块的应用 / JSON数据格式 / json模块的应用
#    CVS文件概述：
#              csv是Comma-Separated Values的缩写，是用文本文件形式储存的表格数据
#    CVS模块应用：
#   读文件：
#     1.使用reader函数，接收一个可迭代的对象（比如csv文件），能返回一个生成器，就可以从其中解析出csv的内容：
#       比如下面的代码可以读取csv的全部内容，以行为单位
import csv
with open("test.csv","r",encoding="utf-8")as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
print(rows)
# 要提取其中某一列，可以用下面的代码
with open("test.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    column = [row[1] for row in reader]
print(column)
# 注意从csv读出的都是str类型
#     2.使用DictReader，和reader函数类似，接收一个可迭代的对象，能返回一个生成器，但是返回的每一个单元格都放在一个字典的值内，
#       而这个字典的键则是这个单元格的标题（即列头）。用下面的代码可以看到DictReader的结构
with open("test.csv", "r", encoding = "utf-8") as f:
    reader = csv.DictReader(f)
    column = [row for row in reader]
print(column)
# 如果我们想用DictReader读取csv的某一列，就可以用列的标题查询
with open("test.csv", "r", encoding = "utf-8") as f:
    reader = csv.DictReader(f)
    column = [row['Name'] for row in reader]
print(column)

#   写文件
#     追加
row = ['5','hanmeimei','23','81']
out = open("test.csv","a",newline="")
csv_writer = csv.writer(out,dialect="excel")
csv_writer.writerow(row)

# python 中的json
"""
JSON 的全称是 JavaScript Object Notation，即 JavaScript 对象符号，它是一种轻量级的数据交换格式。JSON 的数据格式既适合人来读写，也适合计算机本身解析和生成。最早的时候，JSON 是 JavaScript 语言的数据交换格式，后来慢慢发展成一种语言无关的数据交换格式，这一点非常类似于 XML。
JSON 主要有如下两种数据结构：
由 key-value 对组成的数据结构。这种数据结构在不同的语言中有不同的实现。例如，在 JavaScript 中是一个对象；在 Python 中是一种 dict 对象；在 C 语言中是一个 struct；在其他语言中，则可能是 record、dictionary、hash table 等。
有序集合。这种数据结构在 Python 中对应于列表；在其他语言中，可能对应于 list、vector、数组和序列等。
JSON 类型	Python 类型
对象（object）	字典（dict）
数组（array）	列表（list）
字符串（string）	字符串（str）
整数（number(int)） 	整数（int）
实数（number(real)）	浮点数（float）
true	True
false	False
null 	None
"""
# 常用有2个方法，也是最基本的使用方法：
import codecs
import json
test_dict = {'a':1, 'b':2}
# 把字典转成json字符串
json_text = json.dumps(test_dict)
# 把json字符串保存到文件
# 因为可能json有unicode编码，最好用codecs保存utf-8文件
with codecs.open('1.json', 'w', 'utf-8') as f:
    f.write(json_text)

import json
import codecs
# 从文件中读取内容
with codecs.open('1.json', 'r', 'utf-8') as f:
    json_text = f.read()
# 把字符串转成字典
json_dict = json.loads(json_text)

# 1、dumps：把字典转成json字符串import json
import json
import codecs
text_dict = {'a':1,'b':2}
#把字典转成json字符串并写入到文件
with codecs.open("1.json",'w','utf-8')as f:
    json.dump(text_dict,f)

# 2、loads： 把json字符串转成字典
import json
import codecs
# 从json文件读取json字符串到字典
with codecs.open('1.json', 'r', 'utf-8') as f:
    json_dict = json.load(f)