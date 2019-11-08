# 7-1 询问用户要租赁什么样的汽车，并打印一条消息，如“Let me see if I can find you a Subaru”。
print('What kind of bike do you want to rent ?')
car = input('I want to rent :')
print('Let me see if I can find you a '+car)

# 7-2 询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌
print('How many people want to dinner?')
p = int(input('people:'))
if p > 8:
    print('No table')
else:
    print('have a table')

# 7-3 让用户输入一个数字，并指出这个数字是否是10的整数倍。
num = int(input('请输入一个数字'))
if num % 10 == 0:
    print('该数字是10的倍数')
else:
    print('该数字不是10的倍数')

# 7-4 让用户输入配料，打印信息我们会添加此配料，用户输入'quit'时退出循环
meg = input('请输入配料：')
while True:
    msg = input(meg)
    if msg == 'quit':
        break
    else:
        print('我们会添加：'+ msg)

# 7-5 电影院的票价：0-3免费，3-12为10美元，大于12岁为15美元，编写循环，询问年龄指出票价
ages = '输入年龄：'
while True:
    age = input(ages)
    if 'quit' in age:
        print('已退出')
    elif 0 <= int(age) < 3:
        print('免费')
    elif 3 <= int(age) <12:
        print('10美元')
    elif int(age) >= 12:
        print('15美元')

# 7-6 编一个无限循环的编程
a = 1
while a <= 2:
    print(a)

# 7-7 创建一个列表food，包含3种食物，创建一个空列表foods，遍历food打印信息，把food移到foods中，列出来
food = ['apple','banana','orange']
foods = []
z = True
while z:
   for make_food in food:
       print('I made your '+ make_food)
       ac = food.pop()
       foods.append(ac)
   print(foods)
   if int(len(food)) == 0:
       z = False
print('I finished ' + foods[0]+','+foods[1]+','+foods[2])