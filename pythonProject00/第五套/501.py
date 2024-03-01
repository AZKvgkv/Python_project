# class Animal:
#     def __init__(self,name):
#         self.name = name
#         print('这是构造初始化方法')
#         pass
#     def __del__(self):
#         print('这是析构方法')
#     pass
#
#
# cat=Animal('小狸猫')


class Animal2:
    def eat(self):
        '''
        吃
        :return:
        '''
        print('吃饭饭')
    def drink(self):
        '''
        喝
        :return:
        '''
        print('喝水水')

class Dog(Animal2):#继承Animal父类
    def wwj(self):
        print('小狗汪汪叫')
    pass


class Cat(Animal2):
    def mmj(self):
        print('小猫喵喵叫')
    pass

d1=Dog()
d1.eat()
d1.wwj()
c1=Cat()
c1.drink()
c1.mmj()
