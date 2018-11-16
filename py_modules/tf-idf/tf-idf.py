from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
corpus = [
  "布克 准 绝杀 带队 取胜 北京 时间 11 月 5 日 菲尼克斯 太阳队 主场 迎战 孟菲斯 灰熊 此役 两队 激战 四节 最终 凭借着 德文 - 布克 最后 时刻 的 关键 投篮 帮助 球队 以 102 比 100 险胜 对手 艰难 赢下 胜利 距离 全场 比赛 结束 还 剩 6 秒 时 布克 持球 单打 左手 运球 到 三分 线 内急 停 跳投 抬高 弧线 皮球 划过 一道 彩虹 般 弧线 直接 坠入 网窝 此球 打进 之后 太阳队 得以 102 比 100 完成 反超 布克 的 关键 进球 帮助 主队 赢得 了 主动 随着 康利 最后 时刻 投篮不中 布克 成为 了 今天 太阳 的 救世主 作为 关键 先生 的 他 全场 出战 35 分钟 17 投 7 中 其中 三分球 8 投 2 中 得到 25 分 外加 7 次 助攻",
  "帮我 查下 今天 北京 天气 好不好",
  # "帮我 查询 去 北京 的 火车",
  # "帮我 查看 到 上海 的 火车",
  # "帮我 查看 特朗普 的 新闻",
  # "帮我 看看 有没有 北京 的 新闻",
  # "帮我 搜索 上海 有 什么 好玩的",
  # "帮我 找找 上海 东方明珠 在哪"
]
# step 1
vectoerizer = CountVectorizer(min_df=1, max_df=1.0, token_pattern='\\b\\w+\\b')
# step 2
vectoerizer.fit(corpus)
# step 3
bag_of_words = vectoerizer.get_feature_names()
print("Bag of words:")
print(bag_of_words)
print(len(bag_of_words))
# step 4
X = vectoerizer.transform(corpus)
print("Vectorized corpus:")
print(X.toarray())
# step 5
print("index of `的` is : {}".format(vectoerizer.vocabulary_.get('的')))

# step 1
tfidf_transformer = TfidfTransformer()
# step 2
tfidf_transformer.fit(X.toarray())
# step 3
for idx, word in enumerate(vectoerizer.get_feature_names()):
  print("{}\t{}".format(word, tfidf_transformer.idf_[idx]))
# step 4
tfidf = tfidf_transformer.transform(X)
print(tfidf.toarray())
print(type(tfidf.toarray()))