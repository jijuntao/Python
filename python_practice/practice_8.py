# 定义函数 def
def greet_user():
    print('hello')
greet_user()
# 向函数传递信息
def function(name):
    print('hello '+name.title())
function('jesse')
# 实参与形参：
# 一般定义函数时传入形参，调用函数时传入实参
# 实参-位置参数：调用函数传入的实参与定义函数的形参位置顺序应一致
def describe_prt(animal_type,pet_name):
    print('I have a ' + animal_type + ' .'+'\nMy '+animal_type+"'s name is "+pet_name.title()+' .')
describe_prt('dog','sanyue')
# 实参-关键字参数：在调用函数中把实参指定给定义函数中的形参，不用考虑顺序
def describe_prt(animal_type,pet_name):
    print('I have a ' + animal_type + ' .'+'\nMy '+animal_type+"'s name is "+pet_name.title()+' .')
describe_prt(animal_type='dog',pet_name='sanyue')
# 实参-默认值：在定义函数形参的同时赋值，调用函数时可重新赋值，也可使用默认值
def describe_prt(animal_type,pet_name= 'sanyue'):
    print('I have a ' + animal_type + ' .'+'\nMy '+animal_type+"'s name is "+pet_name.title()+' .')
describe_prt(animal_type='dog')
# 返回值：return语句把不需要直接输出的数据返回一个或一组值
# 让实参变成可选的
def name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()
a = name('jami','hendrix')
print(a)
# 返回字典
def bulid_person(first_name,last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name,'last':last_name}
    return person
b = bulid_person('jimi','hendrix')
print(b)
# 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
      print("\nPlease tell me your name:")
      print("(enter 'q' at any time to quit)")
      f_name = input("First name: ")
      if f_name == 'q':
         break
      l_name = input("Last name: ")
      if l_name == 'q':
         break
      formatted_name = get_formatted_name(f_name, l_name)
      print("\nHello, " + formatted_name + "!")
# 传递列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
      """ 模拟打印每个设计，直到没有未打印的设计为止
          打印每个设计后，都将其移到列表completed_models中
      """
      while unprinted_designs:
            current_design = unprinted_designs.pop()
# 模拟根据设计制作3D打印模型的过程
            print("Printing model: " + current_design)
            completed_models.append(current_design)
def show_completed_models(completed_models):
     """显示打印好的所有模型"""
     print("\nThe following models have been printed:")
     for completed_model in completed_models:
         print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# 禁止函数修改列表：可向函数传递列表副本，这样函数所做修改不影响原始列表
def print_models(unprinted_designs, completed_models):
    """ 模拟打印每个设计，直到没有未打印的设计为止
        打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
# 传递任意数量的实参
def make_pizza(*toppings): # *topping中的星号让python创建一个名为topping的空元组
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
# 结合使用位置实参和任意数量实参，如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
# Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 使用任意数量的关键字实参,有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，
# 可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少
def build_profile(first, last, **user_info): # 双星号即表示创建以user_info命名的空字典
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    print(profile)
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)


# 8-1 编写一个名为display_message()，打印句子，指出你在本章学习什么
def display_message():
    print("I'm learning function .")
display_message()

# 8-2 编写一个名为favorite_book()的函数，传入形参，打印消息我最喜欢的书为。。。
def favorite_book(title):
    print('One of my favorite books is '+title.title())
favorite_book('alice in Wonderland')

# 8-3 编写一个名为make_shirt()的函数，需要一个尺码和字样，使用位置实参制作T恤，使用关键字实参调用
def make_shirt(size,logo):
    print('The shirt size is '+size+' and logo is '+logo+'.')
make_shirt('38','cat')
make_shirt(size='40',logo='fish')

# 8-4 修改函数make_shirt()，默认情况下制作印有'I love Python'的大号T恤，打印：默认字样大号T恤，默认字样中号T恤，其他T恤
def make_shirt(size,logo = 'I love Python'):
    print('The shirt size is ' + size + ' and logo is ' + logo + '.')
make_shirt('大号')
make_shirt(size='中号')
make_shirt('小号','Java')

# 8-5 编写函数describe_city(),接受城市名字和所属国家，给国家指定默认值，至少有一座城市不属于默认国家
def describe_city(city,country = 'China'):
    print(city.title()+' is in '+country)
describe_city('sichuan')
describe_city('anhui')
describe_city('luoshanji')

# 8-6 编写名为city_country()的函数，它接受城市及所属国家
def city_country(city,county):
    msg = city+','+county
    return msg.title()
while True:
    print('请输入城市和国家：')
    print('输入q即可退出')
    c_s = input('city:')
    if c_s == 'q':
        break
    g_j = input('country:')
    if g_j == 'q':
        break
    c_c = city_country(c_s,g_j)
    print(c_s)

# 8-7 编写名make_album()的函数，接受名字和专辑名，返回字典包含这两个信息,添加一个可选参数，专辑曲数
def make_album(name,album_name,num=''):
    if num:
        msg = {'name':name,'album_name':album_name,'num':num}
    else:
        msg = {'name':name,'album_name':album_name}
    print(msg)

# 8-8 在8-7中编写while循环让用户输入专辑的歌手和名称，调用函数打印字典
def make_album(name,album_name):
    msg = {'name':name,'album_name':album_name}
    return msg
while True:
    print('======请输入歌手和专辑名称======')
    print('======按q即可退出======')
    msg1 = input('name')
    if msg1 == 'q':
        break
    msg2 = input('album_name')
    if msg2 == 'q':
        break
    msg3 = make_album(msg1,msg2)
    print(msg3)

# 8-9 创建一个包含魔术师的列表，将其传递给一个名为show_magicians()的函数，打印列表中每个魔术师的名字
magic = ['magic1','magic2','magic3']
def show_magicians():
    for name in magic:
        print(name)
show_magicians()

# 8-10 在8-9基础上，编写一个名为make_great()的函数，对魔术师名字加入字样'the Great'，调用函数show_magicians()函数打印
magic = ['magic1','magic2','magic3']
mag = []
def make_great(magic,mag):
    while magic:
        a = magic.pop()
        a = 'the Great '+a
        mag.append(a)
def show_magicians(mag):
    for name in mag:
        print(name)
make_great(magic,mag)
show_magicians(mag)

# 8-11 在8-9中调用make_great()函数时，由于不想修改原始列表，只传递副本，分别调用show_magicians()函数查看结果
magic = ['magic1','magic2','magic3']
mag = []
def make_great(magic,mag):
    while magic:
        a = magic.pop()
        a = 'the Great '+a
        mag.append(a)
def show_magicians(mag):
    for name in mag:
        print(name)
make_great(magic[:],mag)
show_magicians(magic)
show_magicians(mag)

# 8-12 编写一个函数，他接受顾客在三明治添加的食材，只有一个形参，打印消息
def add_food(*foods):
    for food in foods:
        print(food)
add_food('apple')
add_food('orange','bananas')

# 8-13 复制前面程序user_profile.py，在其中调用bulid_profile()函数来创建关于你的简介
def build_profile(first, last, **user_info): # 双星号即表示创建以user_info命名的空字典
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('ji', 'juntao',location='杭州',sex='man')
print(user_profile)

# 8-14 编写一个函数，将一辆车信息存储在字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参
def msg_car(manufacturer,type,**informations):
    cars = {}
    cars['manufacturer'] = manufacturer
    cars['type'] = type
    for k,v in informations.items():
        cars[k] = v
    return cars
car = msg_car('subaru', 'outback', color='blue', tow_package=True)
print(car)