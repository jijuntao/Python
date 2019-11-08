# 新建字典
alien = {'color':'green','points':5}
# 访问字典中的值
alien = {'color':'green','points':5}
print(alien['color'])
# 添加字典键-值对
alien['x'] = 12
alien['y'] = 15
# 修改字典值
alien['color'] = 'yellow'
# 删除字典键-值对
del alien['points']
print(alien)
# 遍历字典,使用方法.items()
shuzi = {'zhao':1,'qian':2,'sun':3,'li':4,'zhou':5}
for k,v in shuzi.items():
    print('\n'+k)
    print(str(v))
# 遍历字典中的所有键，使用方法.keys()
shuzi = {'zhao':1,'qian':2,'sun':3,'li':4,'zhou':5}
for k in shuzi.keys():
    print(k)
# 遍历字典中的所有值，使用方法.values()
shuzi = {'zhao':1,'qian':2,'sun':3,'li':4,'zhou':5}
for v in shuzi.values():
    print(v)
# 遍历列表所有值时剔除重复值使用set()
shuzi = {'zhao':1,'qian':3,'sun':3,'li':4,'zhou':5}
for v in set(shuzi.values()):
    print(v)

# 6-1 使用字典存储一个熟人的信息，包括姓，名，年龄，居住城市，包含键first_name,last_name,age,city
person = {
    'first_name':'juntao',
    'last_name':'ji',
    'age':24,
    'city':'Hangzhou'
}

# 6-2 想出5个人的名字作为字典的键，在分配5个数字，打印每个人喜欢的数字
shuzi = {'zhao':1,'qian':2,'sun':3,'li':4,'zhou':5}
print('The zhao favourite shuizi is'+' '+ str(shuzi['zhao'])+'.')
print('The qian favourite shuizi is'+' '+ str(shuzi['qian'])+'.')
print('The sun favourite shuizi is'+' '+ str(shuzi['sun'])+'.')
print('The li favourite shuizi is'+' '+ str(shuzi['li'])+'.')
print('The zhou favourite shuizi is'+' '+ str(shuzi['zhou'])+'.')

# 6-3 存储三条河流及其经过的国家，其中一个键-值为'nile':'egypt'
#     循环每条河流打印信息
#     使用循环把河流名字打印出来
#     使用循环把国家名字打印出来
num = {'nile':'egypt','changjiang':'China','huanghe':'china'}
for k,v in num.items():
    print('The'+' '+k.title()+' '+ 'runs through' +' '+v.title())
for k in num.keys():
    print(k)
for v in num.values():
    print(v)

# 6-4 创建3个字典，将三个字点存储到列表中，遍历列表，打印每个人人所有信息
P1 = {
    'first_name':'俊涛',
    'last_name':'计',
    'age':24,
    'city':'杭州'
}
P2 = {
    'first_name': '俊',
    'last_name': '孙',
    'age': 23,
    'city': '武汉'
}
P3 = {
    'first_name': '建',
    'last_name': '陈',
    'age': 23,
    'city': '合肥'
}
P = [P1,P2,P3]
for p in P:
    print(p)

# 6-5 创建多个宠物字典，再将字典存储在名为pets的列表中，遍历列表，打印信息
Dogs = {'type':'金毛','host':'cc'}
Cats = {'type':'蓝猫','host':'zz'}
pets = [Dogs,Cats]
for information in pets:
    print(information)

# 6-6 创建一个名为favorite_places 的字典。将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个地方.
favorite_places = {
    'jen':['uk','usa'],
    'sarah':['china','shanghai','hangzhou'],
    'phill':['taishang','hengshang','huangshang']
}
for name,places in favorite_places.items():
    print('\n'+name.title()+"'s favorite_place is :")
    print(places[0].title())

# 6-7 创建一个字典，三个城市名为键，没坐城市在创建字典，包括所属省份，人口，人物
cities = {
    '合肥':{'province':'anhui','population':'65','person':'包青天'},
    '南京':{'province':'jiangsu','population':'55','person':'孙中山'},
    '成都':{'province':'sichuan','population':'96','person':''}
}
for city,details in cities.items():
    print(details)
    for k,v, in details.items():
        print(k+':'+v)
