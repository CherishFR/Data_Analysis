from sklearn.decomposition import PCA


def pca():
    """
    主成分分析进行特征降维
    :return:
    """
    pca = PCA(n_components=0.9)
    data = pca.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(data)


if __name__ == '__main__':
    pca()