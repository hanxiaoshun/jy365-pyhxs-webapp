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
print(yanghui(7))
print('-------------------------')
for i in range(2):
    print(i)
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

yg = yanghuiG(5)
# print(next(yg))
# print(next(yg))
# print(next(yg))
# print(next(yg))
# for i in yg:
#     print(i)


while True:
    try:
        x = next(yg)
        print('yg: ',x)
    except StopIteration as e:
        print('Generator return value :' , e.value)
        break





