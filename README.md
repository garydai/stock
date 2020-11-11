stock 
=====

###思路
Update Time:
2020/11/11 Description:test function

1 统计雪球讨论热门的股票

	1.1.在主页获取雪球活跃用户

	1.2.在活跃用户的发帖中统计股票被提及的次数

	1.3.画出与个股讨论度与价格走势图

2 对评论情感分析

	2.1.使用jieba分词

	[https://github.com/fxsjy/jieba.git](https://github.com/fxsjy/jieba.git)

	2.2.股票领域语料库的构建

	统计评论中的词语提及次数，把频率较高的当做股票领域词语

	2.3.提取特征值

	根据语料库，提取特征值

	2.4.使用nltk NaiveBayesClassifier简单分类评论的正面和负面情绪 

	[http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/](http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/)

	2.5.结论

	利用上边的语料库提取特征值，很难判断评论的正反情感，准确率只有一半。

	词典不够代表性

	2.6.第二种方法

	论坛里对股票的评论一般都是正面的

	把前几天的个股讨论度上升下降与第二天的股价上升下降进行机器学习，即统计概率

	输入前几天的个股讨论度，输出第二天最有可能的股价走势。

	目前是统计前两天的讨论度和两天的股价与第二天的股价走势的关系，
	0表示比昨天上升1表示下降2表示平，
	例如前两天的评论与股价走势'1010'与第二天股价上升、下降、平的概率 0.0444444444444 0.955555555556 0.0

	2.6.1.结论

	结果准确率只有一半

	2.7.第三种方法

	讨论度与第二天股价关系

todo：

统计被提及股票的版块热度图，判断版块热度加速度是否是热点转换的依据

个股与行业讨论度与股价走势的关系，利用机器学习预测走势

分析用户（或者大神）对个股的情绪与股价走势的关系

分词 不开心 会分成 不 开心 对情绪分析有点影响

分析哪几个大V的观点与大盘的走势相符（合力对市场的影响）

###运行说明

python stockCode.py 

用于抓取网易的股票信息，并保存在stock.xls中

python xueqiuPawer.py 3 2

抓取雪球从3天前开始2天内的数据

###需要安装的python模块
beautifulsoup

xlwt

xlrd

selenium

xlutils

nltk

####其他
chromedriver

###特殊说明

linux环境必须桌面版才能运行，因为需要打开浏览器

  


