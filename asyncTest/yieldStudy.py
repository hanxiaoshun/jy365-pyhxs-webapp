def fibg(max):
    n , a, b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

# for i in fibg(5):
#     print(i)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))

# g = fibg(5)
# while True:
#     try:
#         x = next(g)
#         print('g;',x)
#     except StopIteration as e:
#         print('Generator return value:' ,e.value)
#         break


def yanghui(max):
    t = [1]
    n = 1
    while n<max:
        print(t)
        if n>0:
            L = t.copy()
            for i in range(1,len(t)):
                L[i] = t[i]+t[i-1]
            L.append(1)
            # print(L)
        t = L
        n= n+1
    return 'done'
# print(yanghui(7))
print('-------------------------')
# for i in range(2):
#     print(i)

def yanghuiG(max):
    t = [1]
    n = 1
    while n<max:
        yield t
        if n>0:
            L = t.copy()
            for i in range(1,len(t)):
                L[i] = t[i]+t[i-1]
            L.append(1)
            # print(L)
        t = L
        n = n + 1
    return 'done'
def yanghuiG2(max):
    t = [1]
    n = 1
    while n<max:
        yield t
        if n>0:
            L = t.copy()
            for i in range(1,len(t)):
                L[i] = t[i]+t[i-1]
            L.append(1)
        t = L
        n = n + 1
    return 'done'
def yanghuiG3(max):
    t = [1]
    n= 0
    while n<max:
        yield t
        # 当t = [1]时，for i in range(len(t) - 1)]实际上是for i in range(0), 这时i是一个空list，就不会返回i，会自动跳出第一次循环，直接执行下一行语句
        t = [t[i] + t[i+1] for i in range(len(t)-1)]
        t.insert(0, 1)
        t.append(1)
        n = n + 1
    return 'done'
yg = yanghuiG(5)
yg2 = yanghuiG2(5)
yg3 = yanghuiG3(5)
# print(next(yg))
# print(next(yg))
# print(next(yg))
# print(next(yg))
# for i in yg:
#     print(i)

while True:
    try:
        x = next(yg3)
        print('yg: ',x)
    except StopIteration as e:
        print('Generator return value :' , e.value)
        break


# def triangles():
#     ret = [1]
#     while len(ret)-1 < 10:
#         yield ret
#         ret = [ ret[i] + ret[i+1] for i in range(len(ret)-1)]
#         ret.insert(0,1)
#         ret.append(1)
#
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')




