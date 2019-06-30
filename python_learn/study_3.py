# 笔记：
# 分支结构的应用场景 - 条件 / 缩进 / 代码块 / 流程图
# if语句 - 简单的if / if-else结构 / if-elif-else结构 / 嵌套的if
# 循环结构的应用场景 - 条件 / 缩进 / 代码块 / 流程图
# while循环 - 基本结构 / break语句 / continue语句
# for循环 - 基本结构 / range类型 / 循环中的分支结构 / 嵌套的循环 / 提前结束程序
#
# 分支结构：分支结构一共分为4类：单项分支、双项分支、多项分支和巢状分支
#    单项分支：if 条件表达式：           特征: 1.if条件表达式结果为真，则执行if之后所控制代码组，如果为假，则不执行后面的代码组
#                一条python语句...          2.:之后下一行的内容必须缩进，否则语法错误！
#                一条python语句...          3.若if之后的代码中缩进不一致，则不会if条件表达式受控制，也不是单项分支的内容，是顺序结构的一部分
#                ...                       4.if:后面的代码是在条件表达式结果为真的情况下执行，所以称之为真区间或者if区间
#    双项分支：if 条件表达式：           特征: 1.双项分支有2个区间：分别是Ture控制的if区间和False控制的else区间（假区间）
#                一条python语句...          2.if区间的内容在双项分支中必须都缩进，否则语法错误！
#                一条python语句...
#                ...
#             else：
#                一条python语句...
#                一条python语句...
#                ...
#    多相分支：if 条件表达式：            特征:1.多项分支可以添加无限个elif分支，无论如何只执行一个分支
#                一条python语句...          2.执行完一个分支后，分支结构就会结束，后面的分支都不会判断也不会执行
#                一条python语句...          3.多项分支的判断顺序自上而下逐个分支进行判断
#                ...                       4.在Python中没有switch—case语句
#           elif 条件表达式：
#                一条python语句...
#                一条python语句...
#                ...
#           elif 条件表达式：
#                一条python语句...
#                一条python语句...
#                ...
#           ...
#           else：
#                一条python语句...
#                一条python语句...
#                ...
#    巢状分支：巢状分支是其他分支结构的嵌套结构，无论哪个分支都可以嵌套，例如：
#            num = int(input('输入一个数字：'))
#            if num%2 == 0：
#                if num%3 == 0：
#                    print('你输入的数字可以整除2和3')
#                else：
#                    print('你输入的数字只可以整除2，不能整除3')
#            slse：
#                if num%3 == 0
#                    print('你输入的数字不能整除2，可以整除3')
#                else：
#                    print('你输入的数字不能整除2也不能整除3')
#
#      简单的if语句：只有一个测试和一个操作
#                  if 条件表达式式：         # if包含任何条件测试，紧跟在测试后面的缩进代码块，可执行任何操作
#                     一条print()语句       # 若条件测试的结果为Ture，执行print()语句，否则Python将忽略这行代码
#                     ...
#      if-else结构：if 条件表达式：
#                     一条python语句...     # 若if的条件测试通过，则执行if后面的语句，否则执行else后面的语句
#                     一条python语句...     # if-else结构中，Python总会执行李思南公馆操作中的一个

# 练习：
# 1.水仙花数
#   水仙花数是指一个三位数，其个数立方之和等于该数本身
# num = int(input('请输入一个正整数：'))
# if num != 0:
#     sum = ((num//100)**3) + ((num%100//10)**3) + ((num%100%10)**3)
# if sum == num:
#         print('该数为水仙花数')
# else:
#     print('该数不是水仙花数')

# 2.完美数
#   如果一个数恰好等于它的因子之和（除去其本身），则是完美数
#   例如6的因子是1、2、3、6，除去本身之和是1+2+3=6
num_1 = int(input('请输入一个正整数：'))
i = 0
for j in range(1,num_1):    # 遍历
    if num_1%j == 0:
        i+=j
if i == num_1:
    print('该数是完美数')
else:
    print('该数不是完美数')

# 3.Fibonacci数列
# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。
# 从第三项开始，每一项都等于前两项之和。
# 通项公式：如果设F(n)为该数列的第n项(n∈N+)。那么这句话可以写成如下形式：
# F(1)=F(2)=1,F(n)=F(n-1)+F(n-2) (n≥3)
fibs = [0,1]
num_3= int(input('请输入你要知道Fibonacci数列的个数：'))
for i in range(num_3-2):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)



