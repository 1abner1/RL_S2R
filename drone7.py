import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 随机生成1000个数据点
n = 1000
x = np.random.rand(n)
y = np.random.rand(n)
z = np.random.rand(n)

# 绘制Mesh图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none', rstride=2, cstride=2)
plt.savefig('drone1.pdf')
plt.show()
