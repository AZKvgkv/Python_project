import numpy as np
import matplotlib.pyplot as plt


# 定义函数
def f(x):
    return 1 - (np.cos(x) * np.cosh(x))


# 生成x值
x = np.linspace(2, 6, 100)  # 在区间[2, 6]内生成100个均匀分布的点

# 生成y值
y = f(x)

# 绘制函数的图像
plt.plot(x, y, label='f(x) = 1 - (cos(x) * cosh(x))')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # 绘制水平参考线
plt.axvline(root, color='r', linewidth=0.5, linestyle='--', label='Root')  # 标记根的位置
plt.scatter(root, 0, color='r')  # 在根的位置添加一个点
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of the Function')
plt.legend()
plt.grid(True)
plt.show()
