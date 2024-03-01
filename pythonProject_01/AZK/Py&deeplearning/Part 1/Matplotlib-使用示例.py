# 绘制简单图形,sin函数曲线
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0,6,0.1)# 以0.1为单位，生成 0 到 6 的数据
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
plt.plot(x,y1,label = 'sin')
plt.plot(x,y2,linestyle = "--",label = 'cos')   # 用虚线绘制
plt.xlabel("x") # 给 x 轴打标签
plt.ylabel("y") # 给 y 轴打标签
plt.title('sin & cos')  # 标题
plt.legend()    # 线条说明
plt.show()


# 显示图像
import matplotlib.pyplot as plt
from matplotlib.image import imread
img = imread('test.png')
plt.imshow(img)
plt.show()