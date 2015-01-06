
#coding: utf-8


import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import jieba
import re
import os

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


if __name__ == "__main__":


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
	f = open('feature.txt', 'r')
	while 1:
		line = f.readline()
		if not line:
			break
		array = line.split(' ')
		feature[array[0].decode('utf-8')] = None
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

		posfeats.append((word_feats(text, feature), 'pos'))
	#for t in posfeats:
	#	for k in t[0]:
	#		print k
	print posfeats

	l = os.listdir('neg')
	#print l
	for f in l:
		neg = open('neg/' + f, 'r')
		text = neg.read()
		#print text.encode('utf-8')
		
		negfeats.append((word_feats(text, feature), 'neg'))

#	for t in negfeats:
#		for k in t[0]:
#			print k

	print negfeats
	#for key in negfeats:
	#	print key
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
 
	
	