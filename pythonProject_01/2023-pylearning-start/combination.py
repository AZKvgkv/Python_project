# 组合
class CPU:
    def calculate(self):
        print('正在计算ing')

class Screen:
    def show(self):
        print("正在显示一个好看的画面！！！")

class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen

c = CPU()
s = Screen()
m = MobilePhone(c, s)
m.cpu.calculate()