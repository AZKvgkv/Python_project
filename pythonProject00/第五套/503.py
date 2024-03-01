#多态：多种状态、形态。就是同一种行为对于不同的子类（对象）有不同的行为
#实现多态需要两个前提，1、继承：多态必须发生在父类和子类之间
#                  2、重写：子类重写父类的方法

#案例演示

class Animal:
    '''
    父类【基类】
    '''
    def say_who(self):
        print("我是一个动物")
        pass
    pass

class Duck(Animal):
    '''
    鸭子类【子类】 or【派生类】
    '''
    def say_who(self):
        '''
        在这里重写父类方法
        :return:
        '''
        print("我是一只鸭子")
        pass
    pass

class Dog(Animal):
    '''
    狗子类【子类】 or【派生类】
    '''
    def say_who(self):
        '''
        在这里重写父类方法
        :return:
        '''
        print("我是一只狗子")
        pass
    pass

# duck1=Duck()
# duck1.say_who()
# dog1=Dog()
# dog1.say_who()
#
# def commonInvoke(obj):
#     '''
#     统一调用的方法
#     :param obj: 对象的实例
#     :return:
#     '''
#     obj.say_who()
#     pass

# listobj = [Duck(),Dog()]
# for item in listobj:
#     '''
#     循环去调用函数
#     '''
#     commonInvoke(item)
#     pass

#属性分为类属性和实例属性
#类属性：类对象所拥有的属性
class Student:
    name="陈晓庆"#属于类属性，即Stuent 类对象所有的
    def __init__(self,age):
        self.age=age#实例属性
        pass
    pass


cxq=Student(22)
print(cxq.name)
print(cxq.age)


Student.name="郑奎"
zk=Student(23)
print(zk.name)
print(zk.age)

#小结，
#类属性是可以被类对象和实例对象共同访问使用的
#实例对象只能由实例对象所访问


















