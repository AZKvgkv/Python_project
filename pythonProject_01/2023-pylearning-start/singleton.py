# 单例模式
class MySingleton:
    __obj = None
    __init__flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self, name):
        if MySingleton.__init__flag:
            print('初始化第一个对象.....')
            self.name = name
            MySingleton.__init__flag = False

