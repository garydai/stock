
#coding: utf-8


import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import jieba
import re
import os
import xlrd
import xlwt
from glob import glob

import re,urllib2
from bs4 import BeautifulSoup

def word_feats(text, feature):

	words_t = cut(text)
	words = []
	for w in words_t:
		#print w

		if feature.has_key(w.decode('utf-8')):
			#print 1
			words.append(w)

	return dict([(word, True) for word in words])
 
def deal_corpus():

	l = os.listdir('corpus')
	#print l
	posfeats = []
	negfeats = []
	for f in l:
		#print f
		corpus = open('corpus/' + f, 'r')
		text = corpus.read()
		p = re.compile(r'[\x80-\xff]+') 
		chlist =  p.findall(text)


		t =  " ".join(chlist) 
		corpus.close()
		corpus = open('corpus/' + f, 'w')
		corpus.write(t)
		#return

import chardet

def cut(text):
	seg_list = jieba.cut(text, cut_all=False)
	t = " ".join(seg_list).encode('utf-8')
	#print chardet.detect(t)
	#print t
	p = re.compile(r'[\x80-\xff]+') 
	chlist =  p.findall(t)

	#print " ".join(chlist) 
	return chlist

def prodict(freq):

	l = os.listdir('corpus')
	#print l
	posfeats = []
	negfeats = []
	for f in l:
		#print f
		corpus = open('corpus/' + f, 'r')
		text = corpus.read()
		seg_list = jieba.cut(text, cut_all=False)
		for d in seg_list:
			#print d.encode('utf-8')
			if freq.has_key(d):
				freq[d] += 1
			else:
				freq[d] = 1

#sentiment
def method1():
	
	freq = {}
	#deal_corpus()
	#prodict(freq)
	#print freq
	#f = open('dict.txt', 'w')

	#t = sorted(freq.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
	#for key in t:
		#print str(key[0]) + '%' + str(key[1]) + '\n'
	#	f.write(key[0].encode('utf-8') + ' ' + str(key[1]) + '\n')

	#f.close()

	feature = {}
	f = open('feature1.txt', 'r')
	while 1:
		line = f.readline()
		if not line:
			break
		#array = line.split(' ')
		#feature[array[0].decode('utf-8')] = None
		feature[line[:-1].decode('utf-8')] = None
	#print 1
	#print feature[u'坏']
	f.close()
	#print feature
	#exit()
	l = os.listdir('pos')
	#print l
	posfeats = []
	negfeats = []
	for f in l:
		pos = open('pos/' + f, 'r')
		text = pos.read()
		#print text.encode('utf-8')
		ret = word_feats(text, feature)
		if ret != {}:
			posfeats.append((word_feats(text, feature), 'pos'))

	for t in posfeats:
		for k in t[0]:
			print k
		print '1'
	print posfeats

	l = os.listdir('neg')
	#print l
	for f in l:
		neg = open('neg/' + f, 'r')
		text = neg.read()
		#print text.encode('utf-8')
		ret = word_feats(text, feature)
		if ret != {}:
			negfeats.append((word_feats(text, feature), 'neg'))

	for t in negfeats:
		for k in t[0]:
			print k
		print '1'
	print negfeats

	negcutoff = len(negfeats)*3/4
	poscutoff = len(posfeats)*3/4
	 
	trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
	testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
	print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
	classifier = NaiveBayesClassifier.train(trainfeats)
	test_f = open('test.txt', 'r')
	test = test_f.read()
	#tt = []
	tt = word_feats(test, feature)
	#tt.append((word_feats(test, feature)))
	for t in tt:
		#for k in t:
		print t
	
	print classifier.classify(word_feats(test, feature))
	print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
	#classifier.show_most_informative_features(5)


def get_price(code, date):

	url = 'http://quotes.money.163.com/trade/lsjysj_'+ str(code)+'.html'
	print url
	#print("股票代码:" + stock_num)
	headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"}
	req = urllib2.Request( url, headers = headers)
	content = ''
	try:
	    content = urllib2.urlopen(req).read()
	except Exception,e:
	    print e
	    #return 0
	soup = BeautifulSoup(content)

	table = soup.find('table',class_='table_bg001 border_box limit_sale')
	tr = table.findAll('tr')

	#print td
	web = {}
	for i in range(1, len(tr)):
		td = tr[i].findAll('td')

		web[td[0].contents[0]] = (td[4].contents[0])



	url = 'http://quotes.money.163.com/trade/lsjysj_'+ str(code)+'.html?year=2014&season=4'
	print url
	#print("股票代码:" + stock_num)
	headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"}
	req = urllib2.Request( url, headers = headers)
	content = ''
	try:
	    content = urllib2.urlopen(req).read()
	except Exception,e:
	    print e
	    #return 0
	soup = BeautifulSoup(content)

	table = soup.find('table',class_='table_bg001 border_box limit_sale')
	tr = table.findAll('tr')


	for i in range(1, len(tr)):
		td = tr[i].findAll('td')

		web[td[0].contents[0]] = (td[4].contents[0])


	price = []
	for key in date:
		if web.has_key(key):
			price.append(float(web[key]))
			#date[key] = float(td[4].contents[0])
	return price
	#print date

#count
#0上升1下降2打平
def method2():

	file_names = glob('score*')
#file_names = glob('industry*')
	file_names.sort()
#	f = open(file_names[len(file_names) - 6], 'r')

#	while 1:
#		line = f.readline()
		#print line
#		if not line:
#			break
#		array = line[:-1].split('%')
#		a = array[0].decode('utf-8')
#		stock[a] = [int(array[2])]

	
	wb = xlrd.open_workbook('stock.xls')
	sh = wb.sheet_by_name('stock')
	code = {}
	for rownum in range(sh.nrows):
		if rownum < 2:
			continue
		code[sh.cell(rownum, 1).value] = sh.cell(rownum, 0).value

		#s = stock(str(sh.cell(rownum, 0).value), sh.cell(rownum, 1).value.encode('utf-8'), sh.cell(rownum, 2).value.encode('utf-8'))
		#vstock.append(s)

	length = 4
	pro = {}
	for j in range(len(file_names) - length + 1):
		stock = {}
		i = j
		date = {}
		while i < j + length:
			fname = file_names[i]

			date[fname[5:-4]] = -1

			f = open(fname, 'r')
			print fname
			stock_t = {}
			summ = 0
			while 1:
				line = f.readline()
				#print line
				if not line:
					break
				array = line[:-1].split('%')
				a = array[0].decode('utf-8')


				stock_t[a] = int(array[2])
	
				#print line
				summ += int(array[2])

			for key in stock_t:
				if stock.has_key(key):
					stock[key].append(stock_t[key]/float(summ))
				else:
					stock[key] = [stock_t[key]/float(summ)]		



			i += 1
		print 2
		for key in stock:
			#if len(stock[key]) != len(file_names):
			if len(stock[key]) != length:
				continue
			
			#print code[key].encode('utf-8')
			##print stock[key]
			#web = {}
			price = get_price(code[key], date)
			if len(price) != length:
				continue

			print price
			pattern = ''
			for i in range(1, len(stock[key]) - 1):
				if stock[key][i] < stock[key][i-1]:
					pattern += '1'
				elif stock[key][i] == stock[key][i-1]:
					pattern += '2'
				elif stock[key][i] > stock[key][i-1]:

					pattern += '0'

			for i in range(1, len(stock[key]) - 1):
				if price[i] < price[i-1]:
					pattern += '1'
				elif price[i] == price[i-1]:
					pattern += '2'
				elif price[i] > price[i-1]:

					pattern += '0'

			print pattern	

			if price[length - 1] < price[length - 2]:
				p = 1
			elif  price[length - 1] == price[length - 2]:
				p = 2
			elif price[length - 1] > price[length - 2]:
				p = 0

			if pro.has_key(pattern):
				pro[pattern].append(p)
			else:
				pro[pattern] = [p]
	print pro
	for key in pro:
		up = 0
		down = 0
		draw = 0
		for t in pro[key]:
			if t == 0:
				up += 1
			elif t == 1:
				down += 1
			elif t == 2:
				draw += 1
		summ = up + down + draw

		print key, up*1.0 /(summ), down* 1.0/summ, draw*1.0/summ





def get_pattern(stock_name):



	wb = xlrd.open_workbook('stock.xls')
	sh = wb.sheet_by_name('stock')
	code = {}
	for rownum in range(sh.nrows):
		if rownum < 2:
			continue
		code[sh.cell(rownum, 1).value] = sh.cell(rownum, 0).value


	file_names = glob('score*')
#file_names = glob('industry*')
	file_names.sort()

	length = 3
	pro = {}
	stock = {}
	date = {}

	for i in range(len(file_names) - 2 - length , len(file_names) - 2):

		fname = file_names[i]

		date[fname[5:-4]] = -1

		f = open(fname, 'r')
		print fname
		stock_t = {}
		summ = 0
		while 1:
			line = f.readline()
			#print line
			if not line:
				break
			array = line[:-1].split('%')
			a = array[0].decode('utf-8')


			stock_t[a] = int(array[2])

			#print line
			summ += int(array[2])

		for key in stock_t:
			if stock.has_key(key):
				stock[key].append(stock_t[key]/float(summ))
			else:
				stock[key] = [stock_t[key]/float(summ)]		

	#print stock_name.encode('utf-8')
	#print stock
	if stock.has_key(stock_name):
		key = stock_name
	#for key in stock:
		#if len(stock[key]) != len(file_names):
		if len(stock[key]) != length:
			print 'data not enougth'
			return
		
		#print code[key].encode('utf-8')
		##print stock[key]
		#web = {}
		price = get_price(code[key], date)
		print price
		if len(price) != length:
			print 'price data not enougth'
			return

		print price
		pattern = ''
		for i in range(1, len(stock[key])):
			if stock[key][i] < stock[key][i-1]:
				pattern += '1'
			elif stock[key][i] == stock[key][i-1]:
				pattern += '2'
			elif stock[key][i] > stock[key][i-1]:

				pattern += '0'
		#print pattern
		for i in range(1, len(stock[key])):
			if price[i] < price[i-1]:
				pattern += '1'
			elif price[i] == price[i-1]:
				pattern += '2'
			elif price[i] > price[i-1]:

				pattern += '0'

		print pattern	


if __name__ == "__main__":

	#method2()
	get_pattern(u'中信证券')

 
	
	