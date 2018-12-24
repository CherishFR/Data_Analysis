from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer


def countvec():
    """
    对文本进行特征值化
    :return:None
    """
    cv = CountVectorizer()
    data = cv.fit_transform(["yes i love python", "life is short, i like python", "人生 苦短，我 用 python"])
    # 统计列表中出现的词
    print(cv.get_feature_names())

    # 统计每一段中各个词出现的次数，单个字母/汉字不统计（例如i,我）
    print(data.toarray())


if __name__ == '__main__':
    countvec()