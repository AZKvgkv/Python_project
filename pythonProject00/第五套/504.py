# class People:
#     country = "China"
#     @classmethod#标识方法为类方法
#     def get_country(cls):
#         return cls.country  #访问类属性
#         pass
#     @classmethod
#     def change_country(cls,data):
#         cls.country=data    #在类方法中修改类属性的值
#
#     @staticmethod   #标识为静态方法
#     def getData():
#         return People.country



# print(People.get_country())#通过类对象去引用
#
# p=People()
# print(p.get_country()) #实例对象也能访问
#
#
# People.change_country('England')
# print(People.get_country())

#
# print(People.getData())
#
# p=People()
# print(p.getData())      #一般情况下，不会通过实例对象去访问静态方法

#   为什么要使用静态方法？
#   由于静态方法主要用于存放逻辑性代码，本身和类以及实例对象没有交互，
#   在静态方法中不会涉及到类中方法和属性的操作
#   数据资源能够得到有效的充分利用


#demo返回当前的系统时间
import time
class TimeTest:
    def __int__(self,hour,min,second):
        self.hour=hour
        self.min=min
        self.second=second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S",time.localtime())
    pass

print(TimeTest.showTime())

