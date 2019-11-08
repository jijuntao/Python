# 5.1 编写一系列条件测试
car = 'aodi'
print("Is car == 'aodi'? I predict Ture.")
print(car.title() == 'Aodi')

print("Is car == 'bw'? I predict False.")
print(car == 'bw')

# 5.3 创建一个名为color的变量，并将其设置为'green','yellow',或'red'
#     编写一条if语句，检查是否为绿色。若是，则打印该玩家获得5个点
color = 'green'
if color == 'green':
    print('该玩家得到5个点')
else:
    if color == 'yellow':
        print('未通过')
# 5.4 设置变量，根据age的值判断人生处于哪个阶段
age = int(input('输入您的年龄：'))
if age < 2:
    print('婴儿')
elif 2 <= age < 4:
    print('学走路')
elif 4 <= age < 13:
    print('儿童')
elif 13 <= age < 20:
    print('青少年')
elif 20 <= age < 65:
    print('成年人')
else:
    print('老年人')

# 5.5 创建列表，写入3中水果，写5条if语句，如果包含在列表中，打印一条信息，如‘You rellary like bananas！’
favorite_fruit = ['apple','orange','bananas']
if 'a' in favorite_fruit:
    print('yes')
if 'b' in favorite_fruit:
    print('yes1')
if 'banans' in favorite_fruit:
    print('yes3')
if 'c' in favorite_fruit:
    print('yes4')
if 'd' in favorite_fruit:
    print('yes5')

# 5.6 创建一个至少包含5个用户的列表，且其中一个用户名为‘admin’，遍历列表，向每位用户打印问候消息
#     admin和普通用户问候消息不一致
names = ['A','B','C','admin','D']
for name in names:
    if name == 'admin':
        print('Hello admin,would you like to see report?')
    else:
        print('Hello'+' '+name+',''thank you for logging in again')

# 5.7 在5.6的基础上添加条if语句，检查用户名列表是否为空，若为空，就打印消息‘We need to find some users'
names = []
if names:                   # 判断列表是否为空
    for name in names:
        if name == 'admin':
            print('Hello admin,would you like to see report?')
        else:
            print('Hello'+' '+name+',''thank you for logging in again')
else:
    print('We need to find some users')

# 5.8 创建2个列表皆包含5个用户名，其中有2个是一样的，遍历列表，指出相同的用户名只可用一次，其他用户名可使用
users = ['zhao','qian','sun','li','zhou']
new_users = ['zhao','qian1','sun1','li','zhou1']
for new_user in new_users:
    if new_user in users:
        print(new_user+'已经被使用，请输入其他名字')
    else:
        print(new_user+'未被使用，此名字可使用')

# 5.9 在列表中存数字1~9,打印输出内容：1st,2nd,3rd,4th,5th,6th,7th,8th,9th
shu = [1,2,3,4,5,6,7,8,9]
for shu1 in shu:
    if shu1 == 1:
        print(str(shu1)+'st')    # 数字不能直接与字符串拼接，所以用str()转换下
    elif shu1 == 2:
        print(str(shu1)+'nd')
    elif shu1 == 3:
        print(str(shu1)+'rd')
    else:
        print(str(shu1)+'th')