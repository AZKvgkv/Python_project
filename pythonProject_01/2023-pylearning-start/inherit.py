# 继承
class Person:
    def __init__(self, name, age):
        print('创建Person')
        self.name = name
        self.__age = age

    def say_age(self):
        print("{0}的年龄是{1}".format(self.name, self.__age))


class Student(Person):
    def __init__(self, name ,age, score):
        # 调用父类的构造方法，可以使用如下两种方法：
        # Person.__init__(self, name, age)
        super(Student, self).__init__(name, age)
        print("创建Student")
        self.score = score

    def say_score(self):
        print('我的分数是：', self.score)

s1 = Student('az', 23,98)
s1.say_age()
s1.say_score()