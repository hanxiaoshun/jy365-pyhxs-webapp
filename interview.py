# python的语言特性：
# 1、动态语言
# 2、
#
# 1、列表和元组的区别
# 2、set特性:
# 可以做字典中的键
# 支持in
# 和 not in 检查成员
# 无法执行切片（slice）和索引查询
# 没有key值获取对应元素
# 3、切片
# m[::2]  # 每个2个取出一个
# m[::-1] #每隔1个倒叙取出
m = [1, 2, 3, 4]
idflg = id(m) == id(m[:]) # id函数用于获取对象的内存地址
print(idflg)

# 4、编写一个trim(str)
# 的函数
def trim(str):
    while str[:1] == ' ':
        str = str[:1]
    while str[-1:] == ' ':
        str = str[:-2]
    return str
# 5、优化代码--生成器
result = []
for i in range(10):
    result.append(i ** 2)
print(result)
print([i**2 for i in range(10)])
# 6、如何实现可选参数、可变参数、可选关键字参数
def funArgsTest(a, b, c=10, *args, **kwarg):
    temp = a+ b+ c
    for i in args:
        temp += i
    for v in kwarg.values():
        temp += v
    return temp
t = [4,5]
dictt = {'d': 6, 'e': 7}
print(funArgsTest(3, 4, *t, **dictt))

# 7、classmethod 和staticmethod
# classmethod 与类交互，不需要与实例交互的方法
# 也就是类中的方法参数的前一个不用传入self也可以调用实例
# 类方法：调用此方法时，我们通过类而不是类的实例方法的第一个参数
# （如我们平常做的方法）。
# 这意味着您可以使用该方法中的类及其属性而不是特定实例
class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst = Kls.no_inst + 1
    @classmethod
    def get_no_of_instance(cls):
        return cls.no_inst
# kls1 = Kls()
# kls2 = Kls()
# print(kls1.get_no_of_instance())
# print(kls2.get_no_of_instance())
print(Kls.get_no_of_instance())

class ClassTest(object):
    def __init__(self,a):
        self.a = a
    def printk(self):
        print('a is',self.a)
    @classmethod
    def class_method(*args):
        print('args is', args)
    @classmethod   # 为了实现对类本身的操作 https://segmentfault.com/q/1010000004016898
    def class_method2(cls):
        print('arg is', cls)

    @staticmethod  # 不会更改实力本身的数据
    def static_method(*args):
        print('arg is',args)
ct = ClassTest(100)
print(ct.printk())
print(ct.class_method())
print(ct.class_method2())
print(ct.static_method())

# 8、浮点数比较一定要用>= 或者<=?
# 9、写一个包含迭代器和生成器的程序
for i in (x for x in range(20)):
    print(i)

# 10、比较用于格式化显示类信息__str__（面向用户）
# 和 __repr__（面向程序猿）

# 11、排序
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

class Student:
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name,self.grade,self.age))
student_objects = [
Student('john', 'A', 15),
Student('jane', 'B', 12),
Student('dave', 'B', 10),
]

print(sorted(student_tuples,key=lambda x:x[2]))
print(sorted(student_objects,key=lambda s:s.age))

# 12、使用匿名函数
list = map(lambda x:x ** 2, [1, 2, 3])
for i in list:
    print(i)

list = filter(lambda x:x>2,[1,2,3,4,5])
for i in list:
    print(i)
from functools import reduce # 函数会对参数序列中元素进行累积。
# list = reduce(lambda x, y: x + y,[1,2,3,4,5])
# for i in list:
#     print(i)
reduce(lambda x,y: x + y,[1,2,3])
# >>> from functools import reduce
# >>> reduce(lambda x,y: x + y,[1,2,3])
# 6

# 13、deque使用 双端队列，
# 它最大的好处就是实现了从队列 头部快速增加和取出对象:

# 14、深拷贝和浅拷贝，数据类型很复杂的时候尽量使用深拷贝
# copy() 和 deepcope()

# 15、正则表达式
import re
# re.match(): 从字符串首字母处匹配
# re.search():遍历整个字符串匹配

# 16、标准库调试Python程序
# import pdb
# pdb.set_trace()

# 17、装饰器--允许向一个现有的对象添加新的功能，
# 同时又不改变其结构，也就是包装原有的类，赋予其附属的功能
def log(level):
    def dec(func):
        def wrapper(*kargc,**kwargs):
            print("before func was called")
            func(*kargc,**kwargs)
            print("after func was called")
        return wrapper
    return dec

@log(2)
def funcLog():
    print("funcLog was called")
print(funcLog())

# 18、with 关键字
# with可以用来简化try finally代码，
# 看起来可以比try finally更清晰
# with open('test.sh') as f:
#     f.read()
# 19、参数传递和值传递


# 20、self是怎样的一个参数
# self在Python里不是关键字。self代表当前对象的地址。self能避免非限定调用造成的全局变量。
# self在定义时需要定义，但是在调用时会自动传入。
# self的名字并不是规定死的，但是最好还是按照约定是用self
# self总是指调用时的类的实例

# 21、python的内存管理机制
# 三个区域存储变量：事先分配的静态内存，事先分配的可重复利用内存
# 以及需要通过malloc 和free来控制自由内存
# 主要方式包括程序计数以及垃圾回收，可以使用del释放资源

# 22、合法的标识符不能以数字开头
# 23、值为0的任何数字对象的布尔值是False
a=0,0
print(bool(a)) #True

print((3,2)<('a','b')) #报错

# 24、Python不支持的数据类型有
#
# A、char      B、int           C、float       D、list
#
# 答案：A（python里无char型数据，有string字符串类型;但C语言中有char数据类型）

# 25、python因为字符串有长度限制，到了长度就标志字符串的结束
# 26、在编写程序的时候，如果想为一个在函数外的变量重新赋值，
# 并且这个变量会作用于许多函数中时，就需要告诉python这个变量的作用域是全局变量。此时用global语句就可以变成这个任务，
# 也就是说没有用global语句的情况下，是不能修改全局变量的。

# 27、动态创建类
# 1、return class
# 2、type()
# 3、元类metaclass
