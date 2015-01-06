stock
=====

统计雪球讨论热门的股票

1.在主页获取雪球活跃用户

2.在活跃用户的发帖中统计股票被提及的次数

3.画出与个股讨论度与价格走势图

对评论情感分析

1.使用jieba分词

[https://github.com/fxsjy/jieba.git](https://github.com/fxsjy/jieba.git)

2.情绪分析词典的构建

统计评论中的词语提及次数，把频率最高的当做情感词语

3.提取特征值

根据情感词典，提取特征值

4.使用nltk NaiveBayesClassifier简单分类评论的正面和负面情绪 

[http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/](http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/)

todo：

统计被提及股票的版块热度图，判断版块热度加速度是否是热点转换的依据

行业讨论度与股价走势的关系

分析用户（或者大神）对个股的情绪与股价走势的关系

分词 不开心 会分成 不 开心 对情绪分析有点影响




