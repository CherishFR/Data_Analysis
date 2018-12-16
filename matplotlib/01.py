import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.random import randn


x = range(2, 26, 2)
y = [15, 13, 15, 16, 17, 18, 22, 19, 17, 16, 16, 15]
fig = plt.figure(figsize=(20, 8), dpi=80)  # 设置图片大小和清晰程度
plt.plot(x, y)  # 设置X轴和Y轴
plt.xticks(x)  # 设置X轴刻度
plt.yticks(range(min(y), max(y)))  # 设置X轴刻度
plt.savefig("./t1.png")  # 保存图片
plt.show()
