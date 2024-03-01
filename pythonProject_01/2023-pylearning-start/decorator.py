# 装饰器
class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        # print(name,salary)
    @property
    def salary(self):
        print("我的薪水是：",self.__salary)
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if 0 < salary < 1000000:
            self.__salary = salary
        else:
            print("薪资录入错误！！，请在0-1000000之间！")
emp1 = Employee('AZ', 300000)
emp1.salary
emp1.salary = 900000
emp1.salary


