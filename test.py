n = [1, 2, 3, 4, 5, 1, 2]
print(n)
n.pop()
print(n)
n.pop(1)
print(n)
x = n.pop(0)
print(x)
del n
del x

n = [1, 2, 3, 4, 5]
print(n)
n.reverse()
print(n)

n = [20, 5, 15, 10, 20]
print(n)
n.sort()
print(n)

s = ['dog', 'banana', 'cat', 'apple']
s.sort()
print(s)

s = ['dog', 'banana', 'cat', 'apple']
s.sort(reverse=True)
print(s)
s.sort(reverse=False)
print(s)

s = ['a', 'b', 'c', 'd', True, False]
s.sort(reverse=True)

s = [10, 30, -22, 100, 22.35, 10.20, -18.36, 1000]
s.sort(reverse=True)
s.sort()
print(s)
s.sort(reverse=False)
print(s)
