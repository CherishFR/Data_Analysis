from sklearn.feature_extraction import DictVectorizer


def dictvec():
    """
    字典数据收起
    :return:none
    """
    # 实例化
    dict = DictVectorizer(sparse=False)
    # 调用fit_transform
    data = dict.fit_transform([
            {'name': 'liu', 'sex': 'man'},
            {'name': 'feng', 'sex': 'woman'},
            {'name': 'zhao', 'sex': 'woman'},
        ])
    # 展示特征类别
    print(dict.get_feature_names())

    # 将One-hot编码转化成字典形式
    print(dict.inverse_transform(data))

    # 将字典数据转化成One-hot编码，数字数据不需要转化
    print(data)


if __name__ == '__main__':
    dictvec()