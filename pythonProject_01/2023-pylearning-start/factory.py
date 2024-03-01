# 工厂模式

class Benz:pass
class BMW:pass
class BYD:pass

class CarFactory:
    def creatCar(self,brand):
        if brand == "奔驰":
            return Benz()
        elif brand == '宝马':
            return BMW()
        elif brand == '比亚迪':
            return BYD()
        else:
            return "品牌未知，无法创建"

factory = CarFactory()
c1 = factory.creatCar("奔驰")
c2 = factory.creatCar("宝马")
print(c1)
print(c2)