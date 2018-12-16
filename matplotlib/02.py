import numpy as np
import pandas as pd
import random
from matplotlib import pyplot as plt
from numpy.random import randn
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  # 让matplotlib支持中文字体

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
fig = plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y, label="图例", color="r", linestyle="--")

_x = list(x)[::10]
_x_label = ["H{}".format(i) for i in _x]  # matplotlib默认不支持中文
# 设置字符串刻度，第二个参数长度必须和第一个参数一致
plt.xticks(_x, _x_label, rotation=45, fontproperties=font)  # rotation表示旋转多少度
plt.yticks(range(min(y), max(y)))

# 设置表述信息
plt.xlabel("X轴", fontproperties=font)
plt.ylabel("Y轴", fontproperties=font)
plt.title("折线图", fontproperties=font)

# 设置网格
plt.grid()

# 设置图例，需要在plot方法添加label参数
plt.legend(prop=font, loc="upper left")  # 与其他地方不同，图例设置字体需要添加prop

plt.savefig("./t2.png")
plt.show()
