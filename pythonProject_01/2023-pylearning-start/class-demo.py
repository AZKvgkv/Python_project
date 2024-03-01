# 定义一个类
class Student:
    def __init__(self, name, score):
        self.name = name  # 新增 name 属性
        self.score = score  # 新增 score 属性

    def say_score(self):
        print("{0} 的分数是 {1}".format(self.name, self.score))


s1 = Student("AZ", 93)
print(s1.name, s1.score)
s1.say_score()


# 类对象、类属性


class Emp:
    company = "MW"  # 类属性
    count = 0

    def __init__(self, name, score):
        self.name = name  # 实例属性
        self.score = score
        Emp.count += 1

    def say_score(self):  # 实例方法
        print("我之前待的公司是：", Emp.company)
        print(self.name, "的分数是：", self.score)


e1 = Emp("AZ", 90)  # e1是实例对象
e2 = Emp("YX", 80)
e1.say_score()
print("一共创建了{0}个Emp对象".format(Emp.count))


# 类方法
# 以 @classmethod 为标志

# 静态方法
# 以 @staticmethod 为标志
