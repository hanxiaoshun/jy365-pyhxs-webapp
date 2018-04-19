#创建一个list

L = [x*x for x in range(10)]
# print(L)

g = (x*x for x in range(10))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# for i in g:
#     print(i)

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print(b)
        a,b = b,a + b
        n = n+1
    return 'done'

for i in fib(5):
    print(i)
# print(fib(10))


def fibg(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

for i in fibg(5):
    print(i)

ret = [1,2,3,4,5,10]
ret = [ ret[i] + ret[i+1] for i in range(len(ret)-1)]
print(ret)