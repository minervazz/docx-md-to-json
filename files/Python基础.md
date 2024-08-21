# 1-8 深拷贝和浅拷贝
### 浅拷贝：
-为目标对象创建副本，将副本对象的成员指向目标对象成员
-只是为了对象开辟内存，没有为对象成员开辟内存
```python
d = {"i":[],"j":123}
c = d.copy()
print(c)
print(d)
c["i"].append(1)	#{"i":[3],"j":123}
print(c)	#{"i":[3],"j":123}
print(d)	#{"i":[3],"j":123}
#浅拷贝只是为了对象开辟内存，没有为对象成员开辟内存
#浅拷贝会受原内容影响而改变
```
### 深拷贝：
-为目标对象创建副本，将副本对象的成员指向目标对象成员
-为对象开辟内存，并为对象成员开辟内存
```python
d = {"i":[],"j":123}
c = d.deepcopy()
print(c)
print(d)
c["i"].append(1)	#{"i":[3],"j":123}
print(c)	#{"i":[3],"j":123}
print(d)	#{"i":[],"j":123}
#深拷贝为对象开辟内存，并为对象成员开辟内存
#深拷贝后的变量不会受原内容影响
```
区别：
浅拷贝：对内存压了较小，受原数据影响
深拷贝：对内存压力较大，不受原数据影响，可以做到数据隔离
待补充

# 1-9 函数的创建与调用
关键字、函数名、函数体
def add():
print(3)

# 1-10 参数详解
形参和实参
形参：形式参数 add(num1,num2)
实参：
-按照变量位置进行传参，add(3,4)
-关键字传参，add(a = 3, b = 4)
默认参数
-函数自带默认值，add(a,b = 7);不传参则使用默认值，传参则使用传入的值

**不定长参数**
不确定的参数名都放到不定长参数里
不定长参数：
-*args	位置传参，会成为元组
-**kwargs		关键字传参，会成为字典
```python
def register(username,password,*args,**kwargs):
    print(args)		#("sd","213","end")
    print(kwargs)	#("adress":"beijing")


lis = [2,3,4,4]
dic = {"1":"1","2":"2"}
register("zhangsan",232322,"sd","213","end","adress" = "beijing")
register("zhangsan",232322,*lis,**dic,"adress" = "beijing")


def register2(username,*,password):
    print(args)		
register2("lisi",password = "21323") #*号后的参数必须使用关键字传参
```
-*号后的参数必须使用关键字传参

# 1-11 函数的递归、闭包和嵌套
-递归函数：
-类似while，自己调用自己
-最大只能调用996次，超出会报错
-函数嵌套
-函数内部使用其他函数 def add（）：abb（）
-在调用函数时传入另一个函数的retrun	add(abb())
-闭包函数
```python
def add():
    def xbb():
        print("内函数")
    return abb

a = add() #	a = xbb()
a()		#xbb()
```
闭包函数的优缺点：
优点：
-嵌套函数（特别匿名函数），可以直接访问外层函数的局部变量，免去传参
-创建外部无法修改的值
缺点：
-闭包操作导致整个函数的内部环境，被长久保存，占用大量的内存


作用域
LEGB
-L 函数内部，本地作用域/局部作用域
-E 闭包作用域
-G 全局作用域
-B 内置作用域

# 1-12 匿名函数和装饰器
匿名函数
特点：不能换行，只能写一下简单的函数
result = lambda a,b:a+b
两种调用方法：
-print（(lambda a,b:a+b)(1,2)）
-result(1,2)

装饰器，基于闭包函数
-方便对指定接口函数做判断或前置条件
```python
user = {
    "username":"root",
    "password":1234,
}

def login(fun):
    def inner():
        if user["username"] == "root" and user["password"] == 1234:
            fun()
        else:
            print("未登录，无法访问")
    return inner


@login
def index():
    print("欢迎来到首页")
@login
def shop():
    print("欢迎来到商品页")
@login
def pay():
    print("欢迎来到支付页面")



index()
```
# 1-13 生成器和迭代器
-生成器
-yield lis	#返回所有lis值
-yield from lis  #调用一次返回一次lis里的一个值
-生成器表达式
-y = (i for i in range(10))
print(dir(y))  # 	包含'__iter__'、'__next__'为生成器
print(y)  #<generator（生成器） object <genexpr> at 0x00000296088C8430>
```python
#生成器
def func():
    lis = [1,2,3,None]
    yield lis
    print("sdsd")

f = func()
print(next(f))
print(next(f))
```
-迭代器 
-
```python
#迭代器
str = "sadfasd"
ss = iter(str) #将可迭代对象放入迭代器内，进行迭代

print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
print(next(ss))
```

# 1-14 常用内置方法
-ads(-3)    获取绝对值
-bin(10)	将十进制转为二进制
-dir(str)	获取某模块有哪些方法
-eval("1+2")  将str转为python语句并执行，只能执行简单的
-exec("""[i for i in  range(3)]""")	将str转为python语句并执行，可以执行稍复杂一些的
-id（2）获取内存地址id值
-isinstance(3,int)	判断数据类型
-len()	获取长度
-map(lambda x : x + 1 , a)  将生成器或迭代器里的值都执行输出出来
-max(2,3,4)	获取最大值,可传list
-min(3,4,1)	获取最小值,可传list
-round(3.332)	获取四舍五入值，**注：如果小数点是5，指挥返回最近的偶数**
-sum(2,3,4) 	求和,可传list
-zip(a,b)	将多个列表合并成一个列表，获取的值是一个可迭代数据
```python
a = [3,4,5]
b = [0,9,8]
print(list(zip(a, b))) # [(3, 0), (4, 9), (5, 8)]
```


# 1-15 常用内置属性
```python
# 内置属性

def fun():
    """
    ashdjkhfakh
    :return:
    """
    print(2323)  # 撒地方


a = fun
print(a.__name__)  # 获取方法名字
print(a.__doc__)  # 获取注释内容
print(a.__code__)
print(a.__str__)
print(a.__dict__)  # 将方法转为字典

print(__doc__)  # 获取当前注释
print(__package__)  # 获取当前文件所在包

print(__file__)  # 获取当前文件的绝对路径★
print(__name__)  # 获取当前文件的主入口★

```

# 1-16 异常处理
```python
# 异常处理
import traceback

# 异常捕获
try:
    print(1 / 0)
except Exception as e:  # 捕获异常并输出简单的异常信息，用Exception捕获异常作为e（别名）
    print("yichangle ", e)
    print(traceback.print_exc())  # 捕获异常并打印详细的异常信息
else:
    print("meiyou ")
finally:
    print("sdajhfjkahskdjh")

print(2222)

# 常见的异常类型
"""
-NameError:名称错误
-ZeroDivisionError:除数为0异常
-KeyError:字典中key错误异常
-TypeError:数据类型异常
-IndentationError：缩进异常
-SyntaxError：语法异常
-ValueError：值异常
-IndexError：索引异常，一般是超出字符串等长度
"""

# 抛出异常
user_password = -1
if user_password < 0:
    raise Exception("用户输出密码错误！！")

```
# 1-17 文本处理
```python
# 文本处理
import requests as requests

# 读取txt文件
f = open('origin_data/a.txt', encoding='gbk')  # 使用open直接打开文件，会把文件保存在内存中每次使用后都需close
print(f.read())
f.close()

# 使用with方法打开，管理上下文，是将文件内存复制as给f，这样就不用再去close文件了
with open('origin_data/a.txt', encoding='gbk') as f:
    print(f.read())  # 读取文件内容
    print(f.name)  # 获取文件名字
    print(f.mode)  # 获取文件打开方式，r，w，a。。。
    print(f.newlines)  # 获取文件当前换行符
    print(f.encoding)  # 获取使用什么格式打开文件
    print(f.closed)  # 获取当前文件是否已经被关闭，这里还是没有关闭
print(f.closed)  # 获取当前文件是否已经被关闭，这里已经关闭

# 读取文件
with open('origin_data/a.txt', encoding='gbk') as f:
    print(f.read())  # 读取文件内容
    print(f.readline())  # 每次只读一行，根据指针所在位置进行读取
    print(f.tell())  # 获取当前指针
    f.seek(0)  # 修改指针位置，注：gbk编码下中文是2字节，utf-8编码下中文是3字节
    print(f.readlines())  # 读取所有行放入到列表中，根据指针所在位置进行读取

# 写入文件
with open('origin_data/a.txt', 'w', encoding='gbk') as f:
    f.write("sd")  # 覆盖写入
    f.writable()  # 判断当前文件是否支持写入，返回True/False
    f.writelines("sadfasd\nasdfhkajshd\n")  # 写入多行

# 追加写入
with open('origin_data/a.txt', 'a', encoding='gbk') as f:
    f.write("append_txt")

# 多模式打开文件
with open('origin_data/a.txt', 'r+', encoding='gbk') as f:
    print(f.writable())
    print(f.readable())
    print(f.read())
    print(f.write("\nappend_txt"))  # 追加写入模式

# b,以二进制写入模式
img_url = 'https://pics5.baidu.com/feed/1b4c510fd9f9d72a2c5ec…png@f_auto?token=48ef874831c600a1cc831bf493f3b612'
video_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F201808%2F01%2F20180801103755_qkpsm.thumb.1000_0.png&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1680706028&t=f8e50db558355fed5f995e86c5d928b4'
img_data = requests.get(img_url)
video_url = requests.get(video_url)
with open('origin_data/test.mp4', 'wb') as f:
    f.write(video_url.content)

with open('origin_data/test.jpg', 'wb') as f:
    f.write(img_data.content)

```

# 6-1 类的创建、调用、类方法、实例方法、静态方法
```python
# 类的创建与调用

class Ren:
    # 类属性，每一个实例都可以用到
    tui = 2
    gebo = 2
    # 实例属性
    def __init__(self,name,sex,age): #self == 张三；self == 李四
        self.name = name
        self.sex = sex
        self.age = age

    # 类方法,只能调用类属性，不能调用实例属性
    @classmethod
    def lf(cls):
        print(f"调用类属性tui = {Ren.tui}")

    # 实列方法，既可以调用实例属性也可调用类属性
    def demo(self):
        print(f"{self.name}zheshi shilifangfa")
    # 静态方法
    @staticmethod
    def static():
        print(f"静态方法：调用类属tui = {Ren.tui}")


#类的实例化
zhangsan = Ren("张飒飒","男",33)
zhangsan.demo()  #调用实例

lisi = Ren("里斯","女",13)
lisi.demo()

#调用类方法，
Ren.lf()
#调用静态方法,即可以用类调用也可以使用实例对象调用
Ren.static()
wangwu = Ren("王五","女",10)
wangwu.static()
```
# 6-2 私有属性、内置属性、魔法方法
```python
# 类的创建与调用

class Ren:
    # 类属性，每一个实例都可以用到
    tui = 2
    gebo = 2

    # 实例属性
    def __init__(self, name, sex, age):  # self == 张三；self == 李四
        self.name = name
        self.sex = sex
        self.age = age

    # 类方法,只能调用类属性，不能调用实例属性
    @classmethod
    def lf(cls):
        print(f"调用类属性tui = {Ren.tui}")

    # 实列方法，既可以调用实例属性也可调用类属性
    def demo(self):
        print(f"{self.name}zheshi shilifangfa")

    # 静态方法
    @staticmethod
    def static():
        print(f"静态方法：调用类属tui = {Ren.tui}")


# 类的实例化
zhangsan = Ren("张飒飒", "男", 33)
zhangsan.demo()  # 调用实例

lisi = Ren("里斯", "女", 13)
lisi.demo()

# 调用类方法，
Ren.lf()
# 调用静态方法,即可以用类调用也可以使用实例对象调用
Ren.static()
wangwu = Ren("王五", "女", 10)
wangwu.static()


# 私有属性（方法），在变量（方法）前加两个下划线__,在外部调不到
class Two:
    """
    sdsdfsfd
    """
    __bizi = 1  # 私有属性
    zuiba = 1

    def __init__(self, name, sex, pizhong):
        self.name = name
        self.sex = sex
        self.__pizhong = pizhong

    # 实列方法，既可以调用实例属性也可调用类属性
    def __demo(self):
        print(f"{self.name}zheshi shilifangfa")

    # 让外部可以调到私有属性
    def getPizhong(self):
        return self.__pizhong

    # 让外部可以修改私有属性
    def setPizhong(self, value):
        self.__pizhong = value

    # 使用装饰器  让外部可以调到私有属性,调用方法不同★
    @property
    def pizhong(self):
        return self.__pizhong

    # 使用装饰器  让外部可以修改私有属性，调用方法不同★
    @pizhong.setter
    def pizhong(self, value):
        self.__pizhong = value


dubin = Two("小黄", "公", "杜宾")
dubin.setPizhong("哈士奇")
print(dubin.getPizhong())

dubin.pizhong = "中华田园犬"
print(dubin.pizhong)

#内置属性
print(Two.__doc__) #获取类中的注释
print(Two.__dict__) # 显示类中可以调用到的属性
print(Two.__name__)#查看类名
print(callable(Two))#判断类或方法是否可以被调用

#魔法方法（内置方法）
class Three:
    def __init__(self):
        pass
    #print(Three()) 打印return
    def __str__(self):
        return "这是str的魔法方法"

    # print(Three()) 打印return
    def __repr__(self):
        return "这是repr的魔法方法"
    #将方法标为迭代器
    def __next__(self):
        pass
    def __iter__(self):
        pass


print(Three())

```
6-3 反射
```python
# 反射

class Ren:
    # 类属性，每一个实例都可以用到
    tui = 2
    gebo = 2

    # 实例属性
    def __init__(self, name, sex, age):  # self == 张三；self == 李四
        self.name = name
        self.sex = sex
        self.age = age

    # 类方法,只能调用类属性，不能调用实例属性
    @classmethod
    def lf(cls):
        print(f"调用类属性tui = {Ren.tui}")

    # 实列方法，既可以调用实例属性也可调用类属性
    def demo(self):
        print(f"{self.name}zheshi shilifangfa")

    # 静态方法
    @staticmethod
    def static():
        print(f"静态方法：调用类属tui = {Ren.tui}")


# 类的实例化
zhangsan = Ren("张飒飒", "男", 33)
zhangsan.demo()  # 调用实例

# 反射 -用str来获取属性值和调用方法
print(getattr(zhangsan, "name"))  # 获取实例zhangsan  name值
getattr(zhangsan, "demo")()  # 调用实例zhangsan  demo方法

print(hasattr(zhangsan, "sex1"))  # 判断实例shangsan中是否有 sex1属性

delattr(zhangsan, "sex")  # 删除类中的属性
print(hasattr(zhangsan, "sex"))  # 判断实例shangsan中是否有 sex属性

setattr(zhangsan, "name", "王五")  # 设置属性
print(getattr(zhangsan, 'name'))


def f():
    print("设置一个外部函数")


setattr(zhangsan, "name", f)  # 将属性值设为外部函数
zhangsan.name()  # 调用name时就会将外部函数执行

```
# 6-4 创建迭代器
```python
# 创建迭代器
class Ren:
    # 实例属性
    def __init__(self, x, count):  # self == 张三；self == 李四
        self.x = x
        self.count = count

    def __iter__(self):  # 这里一般返回自己即可
        return self

    def __next__(self):  # 这里需要定义具体的迭代器逻辑
        self.count += 1
        if self.count <= self.x:
            return self.count - 1
        else:
            raise StopIteration

a = Ren(10, 1)
for i in a:
    print(i)

print(a.__next__())

```
# 7-1 类的三大特性
## 1. 封装
-广义封装
```python
# 封装
class XiYiji:
    def __init__(self):
        self.chothes = 0
        self.cleanagent = 0

    def washing(self):
        if self.chothes == 0:
            raise Exception("请放入衣服！")
        elif self.cleanagent == 0:
            raise Exception("请放入洗衣液！！")
        else:
            print("开始清洗。。。。清洗结束")

    def drying(self):
        if self.chothes == 0:
            raise Exception("请放入衣服！")
        else:
            print("开始烘干。。。烘干结束！")


class WashPeople:
    def __init__(self, name):
        self.name = name

    # machine:XiYiJi  传入一个类作为参数，machine是参数，：XiYiJi是为了使用类machine时可以提示可调用的方法
    def input_chothes(self, num, machine: XiYiji):
        machine.chothes = num
        print(f"以放入衣服：{num}件")

    def input_cleanagent(self, num, machine: XiYiji):
        machine.cleanagent = num
        print(f"已放入洗衣液{num}ML")

    def wash(self, machine: XiYiji, chothes_num=0, cleanagent=0):
        print(f"{self.name}在操作洗衣机")
        self.input_chothes(chothes_num, machine)
        self.input_cleanagent(cleanagent, machine)
        machine.washing()
        machine.drying()
        print("dididi,清洗并烘干完成————")


zhangsan = WashPeople("张三")  # 对类WashPeople实例化
xyj = XiYiji()  # 对类XiYiJi实例化
zhangsan.wash(xyj, 3, 10)

```
-狭义封装

## 2.继承
作用：代码复用
1.子类可以使用父类的属性和方法
2.子类调用方法，先找自己，再去找父类，一直往上找，找不到报错
3.子类不能继承父类 私有属性和私有属性
4.子类可以重写父类的方法，覆盖或者扩展
```python
# 继承
# 父类或基类  子类

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__sex = "男"

    def pao(self):
        print(f'{self.name}今年{self.age}岁')


class B(A):  # 子类B继承父类B的参数和方法
    def pao(self):
        print("zileide fangfa ")


class C(B, A):  # 多继承,存在一样的方法或属性，使用排在前面的
    pass


b = B("张干", "223")  # 子类继承了父类，必须传入父类需要的参数值
b.pao()

c = C("李快", 21)
c.pao()
print(C.mro())  # 查看类已经继承的方法

"""
1.子类可以使用父类的属性和方法
2.子类调用方法，先找自己，再去找父类，一直往上找，找不到报错
3.子类不能继承父类 私有属性和私有属性
4.子类可以重写父类的方法，覆盖或者扩展
"""
```
## 3.多态

```python
# 多态
# way1：通过扩展和重新的方式|来实现多态
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pao(self):
        print(f'{self.name}今年{self.age}岁，A的跑******')


class B(A):
    def __init__(self, name, age, sex):
        self.sex = sex
        super().__init__(name, age)  # 使用单继承时可以这样写，来扩展属性
        # super(B, self).__init__(name,age)# 使用多继承时可以这样写，来扩展属性，找的时B后面类的属性和方法

    def pao(self):
        print("B的跑！！！ ")
        super().pao()  # 使用单继承时可以这样写，来重写方法
        super(B, self).pao()  # 使用单继承时可以这样写，来重写方法，找的时B后面类的属性和方法


class C(B, A):
    def __init__(self, name, age, sex):
        self.sex = sex
        super(B, self).__init__(name, age)  # 使用多继承时可以这样写，来扩展属性，找的时B后面类的属性和方法

    def pao(self):
        print("B的跑！！！ ")
        super(B, self).pao()  # 使用多继承时可以这样写，来重写方法，找的时B后面类的属性和方法


b = B("张干", "223", "女")  # 子类继承了父类，必须传入父类需要的参数值
b.pao()

c = C("jack", "223", "女")  # 子类继承了父类，必须传入父类需要的参数值
c.pao()

# way2：通过类的封装实现多态
"""
参考前面洗衣机类的例子
"""

```
# 7-2 接口抽象类和类装饰器
## 1.接口抽象类
```python
# 接口抽象类
# way1:弱约束类,只有在调用方法时会抛出异常，在实例化时并不会报错
class Pay:
    def pay(self, money):
        raise Exception("请在子类中重写同名的pay方法")


class ZFBPay(Pay):
    def __init__(self, name):
        self.name = name

    def pay(self, money):
        print(f"{self.name}通过支付宝支付{money}元成功√")


class WeChatPay(Pay):
    def __init__(self, name):
        self.name = name

    def pay(self, money):
        print(f"{self.name}通过微信支付{money}元成功√")


zfb = ZFBPay("张三")
zfb.pay(333)

wx = WeChatPay("张三")
wx.pay(444)
```
```python
# way2：强约束类，如果子类没有重写同名方法在实例化时就会报错
from abc import ABC, abstractmethod


class Pay(ABC):
    @abstractmethod
    def pay(self, money):
        raise Exception("请在子类中重写同名的pay方法")


class ZFBPay(Pay):
    def __init__(self, name):
        self.name = name

    def pay(self, money):
        print(f"{self.name}通过支付宝支付{money}元成功√")


class WeChatPay(Pay):
    def __init__(self, name):
        self.name = name

    def pay(self, money):
        print(f"{self.name}通过微信支付{money}元成功√")


zfb = ZFBPay("张三")
zfb.pay(333)

wx = WeChatPay("张三")
wx.pay(444)
```
## 2.类装饰器
```python
# 类的装饰器
class Demo:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):  # 在函数前加上类装饰器，或者调用实例化对象时会自动执行__call__方法
        print("call方法")
        self.func()
        print(f"执行{self.func.__name__}扩展功能成功")


@Demo  # 类的装饰器
def test():
    print("执行test函数")


test()

a = Demo("a")
a()

```
