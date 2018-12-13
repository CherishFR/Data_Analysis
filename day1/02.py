import numpy as np
import pandas as pd
import random
from matplotlib import pyplot as plt
from numpy.random import randn

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
fig = plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)

_x = list(x)[::10]
_x_label = ["H{}".format(i) for i in _x]  # matplotlib默认不支持中文
# 设置字符串刻度，第二个参数长度必须和第一个参数一致
plt.xticks(_x, _x_label, rotation=45)  # rotation表示旋转多少度
plt.yticks(range(min(y), max(y)))

# 设置表述信息
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.title("折线图")

plt.savefig("./t2.png")
plt.show()
