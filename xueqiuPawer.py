#coding: utf-8

from selenium import webdriver

import time
import os
import re

import urllib2
import sys
from bs4 import BeautifulSoup

import os
import logging
import time
from datetime import datetime
from datetime import timedelta
from datetime import date


import threading  
import time 
import json
import xlrd
import xlwt

from xlrd import open_workbook
from xlutils.copy import copy

#import nltk

import threading
import time

description_id = 1
#windows
#browser = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')
#mac
browser = webdriver.Chrome(executable_path='/Users/daitechang/Documents/stock/chromedriver')

def start(url, d, today, vstock):
   # try:
    global description_id
    global browser
    url = url

    try:
	    browser.get(url)
	    t = browser.page_source

	    pn = re.compile(ur'(.*)"statuses":(.*?)}]', re.S)
	    match = pn.match(t)
	    if not match:
	       # browser.close()
	       # browser.quit()
	    	return 0
	    result =  match.group(2)
	    result = result + '}]'
	    decode = json.loads(result)
	
	    startDetect = time.time()
	    st = int(time.mktime(datetime.strptime(datetime.strftime(today, "%Y-%m-%d"), "%Y-%m-%d").timetuple()))
	    ed = int(time.mktime(datetime.strptime(datetime.strftime(today + timedelta(days = 1), "%Y-%m-%d"), "%Y-%m-%d").timetuple()))
	    st = str(st) + '000'
	    print st
	    ed = str(ed) + '000'
	    print ed

	    s_today = datetime.strftime(today, "%Y-%m-%d")
	    for i in range(len(vstock)):

			for item in decode:
				if item['mark'] == 1:
					continue
				#print item['created_at'], st, ed
				#print item['description'].encode('utf-8'), vstock[i]._name
				if str(item['created_at']) > st and str(item['created_at']) < ed:
					if item['text'].encode('utf-8').find(vstock[i]._name) != -1:
						print 2
						ff = open('corpus/' + s_today + '_' + str(description_id) + '.txt', 'w')
						ff.write(item['text'].encode('utf-8'))
						ff.close()
						description_id += 1
						#print vstock[i]._name, item['description'].encode('utf-8')
						if d.has_key(i):
							d[i] = d[i] + 1
						else:
							d[i] = 1
				elif str(item['created_at']) < st and i == len(vstock) -1:
					#print 1
				#	browser.close()
				#	browser.quit()
					#if i == len(vstock) -1: 
					return 0

			#print array[0], array[1]
			


	   # print decode[0]['description'].encode('utf-8')
	   	
	   # browser.close()
	   # browser.quit()
	    return 1
    except Exception , e:
    	print e

       # browser.close()
       # browser.quit()	
        return 0

import json

#获取热门用户列表
def get_id():

	f = open('id.txt', 'w')
	for i in range(25):
		url = 'http://xueqiu.com/recommend/user/industry.json?detail=1&index=' + str(i)

		#browser.get(url)
		#t = browser.page_source
		print url
	#	print t.encode('utf-8')

		cookie = '''s=10ht15dh2y; xq_a_token=5e47e2777e3b08d99725fe0f9f78815eb1cb8374; xqat=5e47e2777e3b08d99725fe0f9f78815eb1cb8374; xq_r_token=c38fedb2680c6b923eb4c87f16ebf19f574c3eca; xq_is_login=1; u=6585534947; xq_token_expire=Sun%20Nov%2015%202015%2009%3A14%3A02%20GMT%2B0800%20(CST); bid=73fe343eeb79fd513ae47464f938acf9_ig040t46; snbim_minify=true; __utmt=1; __utma=1.2082135748.1445390046.1445497172.1445504051.8; __utmb=1.14.10.1445504051; __utmc=1; __utmz=1.1445390046.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1445390044; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1445506132'''

		headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6","Cookie":cookie }
		req = urllib2.Request( url, headers = headers)
		try:
			content = urllib2.urlopen(req).read()
		except Exception, e:
			print e
			#return
		js = json.loads(content)
		#print js

		industries = js['industries']

		#print industries
		if industries:
			for industry in industries:
				for user in industry['users']:
					print user['id'], user['screen_name'].encode('utf-8')
					f.write((str(user['id'])) + ' ' + (user['screen_name']).encode('utf-8') + '\n')

		#f.write(p[0].get('value').encode('utf-8') + ' ' + p[1].get('value').encode('utf-8') + '\n')


	print 1
class stock:
	_id = ''
	_name = ''
	_industry = ''

	def __init__(self, id, name, industry):
		self._id = id
		self._name = name
		self._industry = industry

#import chardet

def pawner(day, t2):


	today   = date.today()
	delta = -1

	os.mkdir('corpus')
	while 1:
		f = open('id.txt', 'r')
		delta += 1
		if delta >= t2:
			break
		yesterday1 = today - timedelta(days = day - delta)
		yesterday = datetime.strftime(yesterday1, "%Y-%m-%d")
		score_file = 'score' + yesterday + '.txt'
		industry_file = 'industry' + yesterday + '.txt'
		#ff = open('score' + yesterday + '.txt', 'r')
		d = {}
		print score_file
		vstock = []
		#ff = open('stock.txt', 'r')


		wb = xlrd.open_workbook('stock.xls')
		sh = wb.sheet_by_name('stock')

		for rownum in range(sh.nrows):
			if rownum < 2:
				continue
			s = stock(str(sh.cell(rownum, 0).value), sh.cell(rownum, 1).value.encode('utf-8'), sh.cell(rownum, 2).value.encode('utf-8'))
			vstock.append(s)
	

		print len(vstock)
		print repr(vstock[0]._name)
		
		while 1:
			try:
				line = f.readline()
			#	user = str(i)
				if not line:
					break
				array = line[:-1].split(' ')
				user = array[0]
				print array[0], array[1]
				#user = "1676206424"
				page = 1
				while 1:

					url = "http://xueqiu.com/" + user + "?page=" + str(page)
					ret = start(url, d, yesterday1, vstock)
					if ret == 0:
						#print i
						break
					page = page + 1
				time.sleep(2)
			except Exception , e:
				print e
				continue
			#break
			#i = i  + 1
			#if i >=9999999999:
			#	break
		

		f.close()
		ff = open(score_file, 'w')

		industry_p = open(industry_file, 'w')
		rb = open_workbook('stock.xls')
		rs = rb.sheet_by_name('stock')
		wb = copy(rb)
		ws = wb.get_sheet(0)
		ncol = rs.ncols	
		ws.write(1, ncol, yesterday)
		industry_d = {}
		t = sorted(d.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
		for key in t:
			print str(vstock[key[0]]._name) + '%' + str(vstock[key[0]]._industry) + '%'+ str(key[1]) + '\n'
			ff.write(str(vstock[key[0]]._name) + '%' + str(vstock[key[0]]._industry) + '%'+ str(key[1]) + '\n')

			if industry_d.has_key(vstock[key[0]]._industry):
				industry_d[vstock[key[0]]._industry] += 1
			else:
				industry_d[vstock[key[0]]._industry] = 1

			ws.write(key[0] + 2, ncol, key[1])

		t = sorted(industry_d.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
		for key in t:
			print str(key[0]) + '%' + str(key[1]) + '\n'
			industry_p.write(str(key[0]) + '%' + str(key[1]) + '\n')

		print industry_d

		wb.save('stock.xls')

	browser.close()
	browser.quit()	
#	timer = threading.Timer(7200, pawner)
#	timer.start()





if __name__ == "__main__":

	#nltk.download()
	#negids = movie_reviews.fileids('neg')
	#posids = movie_reviews.fileids('pos')
	#print 1
##	timer = threading.Timer(7200, pawner)
#	timer.start()
	t = int(sys.argv[1])
	t2 = int(sys.argv[2])
	#get_id()
	pawner(t, t2)
