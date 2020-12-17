'''def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


print('factorial of 3 is', factorial(3))

s = lambda n: n * n
print('the square of 4 is', s(4))
print('the square of 16 is', s(16))

# code a lambda function to find tha total of two numbers

t = lambda x, y: x + y
print('the total is', t(10, 20))

# Example: - write a lambda function to find the greatest of two numbers.

g = lambda x, y: x if x > y else y
print('the greater number is:', g(10, 100))


'''

# without lambda function

'''def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


l = [0, 5, 10, 15, 20, 25, 30]
l1 = list(filter(isEven, l))
print(l1)

l = [0, 5, 10, 15, 20, 25, 30]
l1 = list(filter(lambda x: x % 2 == 0, l))
print(l1)


def isOdd(x):
    if x % 2 != 0:
        return True
    else:
        return False
'''

'''l = [0, 5, 10, 15, 20, 25, 30]
l1 = list(filter(isOdd, l))
print(l1)

l = [0, 5, 10, 15, 20, 25, 30]
l1 = list(filter(lambda x: x % 2 != 0, l))

print(l1)


def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


v = ['k', 'a', 'p', 'i', 'l']
for i in v:
    res = fun(i)
    if res == True:
        print('{} is a vowel'.format(i))'''

'''letters = ['a', 'e', 'i', 'o', 'u']
v = ['k', 'a', 'p', 'i', 'l', 'e', 'a']

l1 = set(filter(lambda i: i in ['a', 'e', 'i', 'o', 'u'], v))
print(l1)

# g = lambda x, y: x if x > y else y
'''

l = [1, 2, 3, 4, 5]


def double_it(li):
    return 2 * li


list1 = list(map(double_it, l))
print(list1)

l = [1, 2, 3, 4, 5]
list1 = list(map(lambda x: x * 2, l))
print(list1)

l = [1, 2, 3, 4, 5]


def square_it(li):
    return li * li


list1 = list(map(square_it, l))
print(list1)

l = [1, 2, 3, 4, 5]
list1 = list(map(lambda x: x * x, l))
print(list1)

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
list1 = list(map(lambda x, y: x * y, l1, l2))
print(list1)

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10, 100]
list1 = list(map(lambda x, y: x * y, l1, l2))
print(list1)

from functools import *

l = [10, 20, 30, 40, 50]
res = reduce(lambda x, y: x + y, l)
print(res)

from functools import *

l = [10, 20, 30, 40, 50]
res = reduce(lambda x, y: x * y, l)
print(res)


def f1():
    print('hello')


f1()
print(id(f1))


def wish(name):
    print('Good morning!!', name)


greeting = wish  # greeting is the alias name for the wish function
print(id(wish))
print(id(greeting))

greeting('prasad')
wish('durga')


def wish(name):
    print('Good morning!!', name)


greeting = wish  # greeting is the alias name for the wish function
print(id(wish))
print(id(greeting))

greeting('prasad')
wish('durga')

del wish
greeting('kapil')


def outer():
    print('outer function has started')

    def inner():
        print('inner function execution')

    print('outer function calling inner function')
    inner()


outer()
print('**********************************************************')


def outer():
    print('outer function has started')

    def inner():
        print('inner function execution')

    print('outer function calling inner function')
    return inner()


f1 = outer
f1()

