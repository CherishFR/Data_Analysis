from sklearn.preprocessing import MinMaxScaler, StandardScaler


def stand():
    """
    标准化缩放
    :return:None
    """
    std = StandardScaler()
    # 对二维数组的每一列做归一化处理
    data = std.fit_transform([[50, 2, 10, 40], [70, 8, 5, 9], [100, 50, 25, 10]])
    print(data)
    return None


if __name__ == '__main__':
    stand()