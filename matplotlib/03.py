import numpy as np
import pandas as pd
import random
from matplotlib import pyplot as plt
from numpy.random import randn
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  # 让matplotlib支持中文字体

y1 = [i for i in randn(30)]
y2 = [i for i in randn(30)]

x1 = range(1, 31)
x2 = range(51, 81)

plt.figure(figsize=(20, 8), dpi=80)

# 绘制散点图
plt.scatter(x1, y1, label="第一次")
plt.scatter(x2, y2, label="第二次")

# 调整刻度
_x = list(x1)+list(x2)
plt.xticks(_x)

plt.legend(prop=font)

plt.show()