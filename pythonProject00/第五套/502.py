#多继承
# class shenxian:
#     def fly(self):
#         print('神仙都会飞')
#         pass
#
# class Monkey:
#     def chitaozi(self):
#         print('猴子喜欢吃桃子')
#         pass
#
#
# class sunwuks(shenxian,Monkey):
#     print('Sun的特点：')
#     pass


# das=sunwuks()
# das.fly()
# das.chitaozi()



#问题是，当多个父类存在相同方法的时候会调用哪一个,,,,{【（先子后父），A-B-C-D】}

# class D(object):
#     def eat(self):
#         print('D.eat')
#         pass
#     pass
#
#
# class C(D):
#     def eat(self):
#         print('C.eat')
#         pass
#
#
#
# class B(D):
#     pass
#
#
# class A(B,C):
#     pass
#
# a=A()
# a.eat()
#
# print(A.__mro__)#自带的魔术方法，可以显示类的一次继承关系



#基类（父类）传递
# class GrandFather:
#     def eat(self):
#         print("吃的方法")
#
#
#
# class Father(GrandFather):
#     def eat(self):
#         print("父亲经常吃海鲜")
#     pass
#
# class Son(Father):
#     def eat(self):
#         print("儿子通常吃火锅")
#     pass
#
# son=Son()
# son.eat()
# print(Son.__mro__)



class Dog:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def bark(self):
        print("汪汪叫。。。。")
        pass
    pass
class kejiquan(Dog):
    def __init__(self,name,color):#属于重写父类的方法
        #针对这种需求  需要调用父类的函数
        # Dog.__init__(self,name,color)#手动调用,调用父类的方法执行完毕就可具备name和color这两个实例属性



        super().__init__(name,color)#super，自动找到父类，进而调用方法。如果是多个父类，会按照顺序找到并调用



        # 拓展其他的属性
        self.height = 90
        self.weight =30
        pass
    def __str__(self):
        return '{}的颜色是{} 它的身高是{}cm 它的体重是{}kg'.format(self.name,self.color,self.height,self.weight)
    def bark(self):
        super().bark()#调用父类的bark方法
        print("叫的很是不一般")
        print(self.name)
        print(self.color)
    pass


kj=kejiquan('柯基犬','黄色')
kj.bark()
print(kj)