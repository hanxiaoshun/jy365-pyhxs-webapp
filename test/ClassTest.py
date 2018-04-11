# 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

class Screen(object):
    pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # if not isinstance(value, int):
        #     raise ValueError('width must be an integer!')
        # if value < 0 or value > 2000:
        #     raise ValueError('width must between 0 ~ 1000!')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
    @property
    def resolution(self):
        return self.__width*self.__height
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')