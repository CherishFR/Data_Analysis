from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import jieba


def cutword():
    # 分词，结果为生成器
    con1 = jieba.cut("22号俄罗斯彼尔姆边疆区一在建钾盐矿井因建筑材料起火引发火灾，事故造成9人死亡。目前井下大火已基本扑灭。")
    con2 = jieba.cut("据塔斯社23号援引现场救援指挥部的消息报道，事发矿井深约500米，起火位置距地表300多米。")
    con3 = jieba.cut("事发时井下共有17人作业，其中8人成功升井，9人被困。")

    # 转化成列表
    content1 = " ".join(list(con1))
    content2 = " ".join(list(con2))
    content3 = " ".join(list(con3))

    return content1, content2, content3


def hanzivec():
    """
    对汉字进行特征值化
    :return:None
    """
    c1, c2, c3 = cutword()
    tf = TfidfVectorizer()
    data = tf.fit_transform([c1, c2, c3])

    print(tf.get_feature_names())

    print(data.toarray())


if __name__ == '__main__':
    hanzivec()