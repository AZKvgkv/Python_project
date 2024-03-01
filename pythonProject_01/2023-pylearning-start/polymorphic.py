# 多态
class Animal:
    def shout(self):
        print("动物叫了一声")

class Dog(Animal):
    def shout(self):
        print("小狗，汪汪汪")

class Cat(Animal):
    def shout(self):
        print("小猫，喵喵喵")

def animalShout(a):
    a.shout()           # 会产生多态，传入的对象不同，则调用的方法也不一样

animalShout(Dog())
animalShout(Cat())