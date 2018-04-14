def is_odd(n):
    return n % 2 == 1
def build(x, y):
    return lambda: x * x + y * y

def is_odds(n):
    return lambda: n % 2 == 1


n=range(1,20)
b=lambda n:n%2==1
L=list(filter(b,n))
# print(L)

L = list(filter(is_odd, range(1, 20)))
# print(L)

# print(list(filter(lambda n: n%2==1, range(10))))

def product(x, y):
    return x * y
def productN(*numbers):
    sub = 1
    for i in numbers:
        sub = sub * i
    return sub
nums = [1,2,3,4,5]
print(productN(*nums))
# for i in range(1,len(nums)):
#     nums[i] = nums[i] * nums[i-1]
#     print(nums[i])