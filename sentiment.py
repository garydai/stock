
#coding: utf-8


import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import jieba
import re
import os
def word_feats(text):

	words = cut(text)
	return dict([(word, True) for word in words])
 
def deal_corpus():

	l = os.listdir('corpus')
	#print l
	posfeats = []
	negfeats = []
	for f in l:
		print f
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
	print t
	p = re.compile(r'[\x80-\xff]+') 
	chlist =  p.findall(t)

	print " ".join(chlist) 
	return chlist

if __name__ == "__main__":


	deal_corpus()
	exit()
	l = os.listdir('pos')
	print l
	posfeats = []
	negfeats = []
	for f in l:
		pos = open('pos/' + f, 'r')
		text = pos.read()
		#print text.encode('utf-8')

		posfeats.append((word_feats(text), 'pos'))
	print posfeats

	l = os.listdir('neg')
	print l
	for f in l:
		neg = open('neg/' + f, 'r')
		text = neg.read()
		#print text.encode('utf-8')
		
		negfeats.append((word_feats(text), 'neg'))
	print negfeats
	negcutoff = len(negfeats)*3/4
	poscutoff = len(posfeats)*3/4
	 
	trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
	testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
	print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
	classifier = NaiveBayesClassifier.train(trainfeats)
	test_f = open('test.txt', 'r')
	test = test_f.read()

	print classifier.classify(word_feats(test))
	print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
	#classifier.show_most_informative_features(5)
 
	
	