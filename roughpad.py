'''x = 10, 20, 30, 40
print(x)
print(type(x))

t = ()
print(type(t))

t = (10,)
print(t)
print(type(t))

t = (10)
print(t)
print(type(t))

i = 10,
print(i)
print(type(i))

t = ('kapil',)
print(t)
print(type(t))

t = ()
print(t)
print(type(t))
print(id(t))
t1 = 10, 20, 30, 40
print(id(t1))
t = t1
print(t)
print(id(t))
print(id(t1))'''

'''t1 = 10, 20, 30, 40
t2 = 100, 200, 300, 400
t3 = ()
t3 = t1
print(id(t1))
print(id(t3))
print(t1)
print(t3)
print('*****************************')
t3 = t2
print(id(t2))
print(id(t3))
print(t2)
print(t3)
print('*****************************')
t3 = t1 + t2
print(t3)
print(id(t3))
print('*****************************')
'''
# t3[0] = 1000

'''t = (10, 20, 30, 40)
print(t)
print(type(t))
print(t[0])
print(t[-1])'''
# print(t[100])

'''t = (10, 20, 30, 40, 50, 60)
print(t[2:5])
print(t[2:100])
print(t[::2])
print(t[::-1])

t1 = 100, 200, 300
t = (10, 20, 30, 40, 50, 60)
t = t + t1
print(t)

t1 = 100, 200, 300
t = ('cat', 'dog', 'cow')
t = t + t1
print(t)

t = (10, 20, 30, 40, 50, 60)
t1 = t * 3
print(t1)
'''
'''t = (10, 20, 30, 10, 40, 50, 60)
print(len(t))
print(t.count(10))
print(t.index(10))
t1 = sorted(t)  # after sorting it will return list datatype.
print(t1)
t1 = tuple(sorted(t))  # after sorting it will return tuple datatype.
print(t1)
print(min(t))
print(max(t))
'''
'''s = {10, 20, 30, 40}
print(s)
print(type(s))

s = {}
print(s)
print(type(s))

s = set()
print(s)
print(type(s))

s = {10, 20, 30, 40}
print(s)
s.add(50)
print(s)
print(type(s))
'''
'''s = {10, 20, 30, 40}
l = [60, 70, 80]
print(s)
s.update(l, range(5), range(20, 30, 3))
print(s)
l1 = [100, 200, 300, 400]
s.update(l1)
print(s)
print(type(s))
'''
'''s = {10, 20, 30, 40}
print(s)
s1 = s.copy()
print(s1)
print(type(s1))
print(id(s))
print(id(s1))
'''
'''s = {10, 20, 30, 40}
s1 = s
print(s1)
print(s)
print(id(s1))
print(id(s))
'''
'''s = {10, 20, 30, 40}
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)'''

'''s = {10, 20, 30, 40}
print(s)
s.remove(30)
print(s)'''

'''s = {10, 20, 30, 40}
print(s)
s.discard(30)
print(s)
s.discard(100)'''

'''s = {10, 20, 30, 40}
print(s)
s.clear()
print(s)
'''

'''s1 = {10, 20, 30, 40}
s2 = {100,200,40,500}
print(s1.union(s2))
print(s1 | s2)
'''

'''s1 = {10, 20, 30, 40}
s2 = {100, 200, 40, 500}
print(s1.intersection(s2))
print(s1 & s2)
'''

'''s1 = {10, 20, 30, 40}
s2 = {100, 200, 40, 500}
print(s1.difference(s2))
print(s1 - s2)
'''
'''s1 = {10, 20, 30, 40}
s2 = {100, 200, 40, 500}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
'''

s1 = {10, 20, 30, 40}
print(10 in s1)
print(100 not in s1)
print(100 in s1)
print(10 not in s1)
print(10 is s1)
print(10 is not s1)

s = set()
s = s1
print(s is s1)
print(s is not s1)
