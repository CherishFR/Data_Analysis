from sklearn.datasets import load_iris

li = load_iris()

print(li.data)  # 获取特征值
print(li.target)  # 获取目标值