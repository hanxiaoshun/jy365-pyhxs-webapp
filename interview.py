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
# classmethod 与类交互，不需要与实例交互的方法 也就是类中的方法参数的前一个不用传入self也可以调用实例
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
        print('args is',args)
    @classmethod
    def class_method2(cls):
        print('arg is',cls)

    @staticmethod
    def static_method(*args):
        print('arg is',args)
ct = ClassTest


