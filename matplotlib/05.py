import numpy as np
import pandas as pd
import random
from matplotlib import pyplot as plt
from numpy.random import randn
from matplotlib.font_manager import FontProperties

my_font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  # 让matplotlib支持中文字体

a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

bar_width = 0.2

x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]

plt.figure(figsize=(20, 8), dpi=80)

plt.bar(range(len(a)), b_14, width=bar_width, label="9月14日")
plt.bar(x_15, b_15, width=bar_width, label="9月15日")
plt.bar(x_16, b_16, width=bar_width, label="9月16日")

# 设置图例
plt.legend(prop=my_font)

# 设置x轴的刻度
plt.xticks(x_15, a, fontproperties=my_font)

plt.show()