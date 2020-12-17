'''class Engine:
    a = 10

    def __init__(self):
        self.b = 20
        # print('engine class constructor executed')

    def m1(self):
        print('Engine specific functionality')


class Car:
    def __init__(self):
        self.engine = Engine()
        # print('car class constructor executed')

    def m2(self):
        print('Car is using some engine functionality')
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()


c = Car()
c.m2()
print('**** calling the engine method and variables using the object reference variable ****')
c.engine.m1()
print(c.engine.a)
print(c.engine.b)
'''

'''class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print('The car name is {}, model is {} and color is {}'.format(self.name, self.model, self.color))


class Employee:
    def __init__(self, ename, empno, car):
        self.ename = ename
        self.empno = empno
        self.car = car

    def empinfo(self):
        print('Employee name:', self.ename)
        print('Employee number:', self.empno)
        print('Employee car info:')
        self.car.getinfo()


c = Car("bmw m5", "m-series", "blue")
e = Employee('kapil', '1001', c)
e.empinfo()
'''

'''class X:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        print('m1 method of X class')


class Y:
    c = 30

    def __init__(self):
        self.d = 40

    def m2(self):
        print('m2 method of Y class')

    def m3(self):
        x1 = X()
        print(x1.a)
        print(x1.b)
        x1.m1()
        print(Y.c)
        print(self.d)
        self.m2()
        print('m3 is a method of Y class')


y1 = Y()
y1.m3()
'''

'''class P:

    def m1(self):
        print('parent instance method')


class C(P):
    def m2(self):
        print('child class method')


c = C()
c.m1()
c.m2()
'''

'''class P:
    a = 100

    def __init__(self):
        self.b = 200

    def m1(self):
        self.x = 10
        print('parent instance method')

    @classmethod
    def m2(cls):
        print('parent class method')
        cls.y = 20

    @staticmethod
    def m3():
        print('parent static method')
        z = 30


class C(P):
    pass


c = C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
print(c.x)
print(c.y)
c.x = 1000
print(c.x)
c.y = 2000
print(c.y)
# print(c.z)'''

'''class P:
    c = 30

    def __init__(self):
        self.d = 40

    def m2(self):
        print(self.c)
        self.var1 = 1000

    @classmethod
    def c2(cls):
        cls.var2 = 2000
        print('this is a class method')


v1 = P()
v1.m2()
print(v1.var1)
v1.c2()
print(v1.var2)
v1.var2 = 4000
print(v1.var2)
P.c2()


class person:
    @staticmethod
    def greet(name, job):
        print("Hello!")
        name = name
        job = job
        print(name, job)


#person.greet()
p = person()
#p.greet()
p.greet('kapil', 'clerk')'''

class P:
    a = 10

    def __init__(self):
        self.b = 20


class C(P):
    c = 30

    def __init__(self):
        super().__init__()
        self.d = 40


c1 = C()
print(c1.a)
print(c1.b)
print(c1.c)
print(c1.d)


'''class Engine:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        print('Engine specific functionality')


class Car:
    def __init__(self):
        self.c = 30
        self.engine = Engine()

    def m2(self):
        print('Car is using engine functionality')
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()


c1 = Car()
c1.m2()
print(c1.engine.a)
print(c1.engine.b)
print(c1.c)'''