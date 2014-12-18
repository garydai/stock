#coding: utf-8

from selenium import webdriver
#from selenium.webdriver.chrome.options import Options 
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
#from adspider import target
import time
import os
import re


import sys


import os
import logging
import time
from datetime import datetime
from datetime import timedelta
from datetime import date


import threading  
import time 
import json
 

def start(url, d):
   # try:
    browser = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')
    url = url
    browser.get(url)

    t = browser.page_source

    pn = re.compile(ur'(.*)"statuses":(.*?)}]', re.S)
    match = pn.match(t)
    if not match:
        browser.close()
        browser.quit()
    	return 0
    result =  match.group(2)
    result = result + '}]'
    decode = json.loads(result)
    
    f = open('stock.txt', 'r')


    today   = date.today()
    print today
    startDetect = time.time()
    ed = int(time.mktime(datetime.strptime(datetime.strftime(today, "%Y-%m-%d"), "%Y-%m-%d").timetuple()))
    st = int(time.mktime(datetime.strptime(datetime.strftime(today - timedelta(days = 1), "%Y-%m-%d"), "%Y-%m-%d").timetuple()))
    st = str(st) + '000'
    print st
    ed = str(ed) + '000'
    print ed

    #today = datetime.now()
    
    #stoday = today.strftime("%Y-%m-%d 00:00:00")
    #print stoday
  #  timeArray = time.strptime(stoday, "%Y-%m-%d 00:00:00")

   # timeStamp = int(time.mktime(timeArray))
  #  print timeStamp

    while 1:
		line = f.readline()

		if not line:
			break
		#print line
		array = line[:-1].split('%')
		for item in decode:
			#print item['created_at'], st, ed
			if str(item['created_at']) > st and str(item['created_at']) < ed:
				if item['description'].encode('utf-8').find(array[1]) != -1:
				#	print 2
					print array[1], item['description'].encode('utf-8')
					if d.has_key(array[1]):
						d[array[1]] = d[array[1]] + 1
					else:
						d[array[1]] = 1
			elif str(item['created_at']) < st:
				#print 1
				browser.close()
				browser.quit()
				return 0

		#print array[0], array[1]
		


   # print decode[0]['description'].encode('utf-8')

    browser.close()
    browser.quit()

def pawner():

	f = open('id.txt', 'r')
	ff = open('score.txt', 'r')
	d = {}
	while 1:
		score = ff.readline()
		if not score:
			break
		array = score[:-1].split(' ')
		d[array[0]] = int(array[1])
	ff.close()
	#i = 1000000000
	while 1:
		user = f.readline()
	#	user = str(i)
		#if not user:
		#	break
		page = 1
		while 1:

			url = "http://xueqiu.com/" + user + "?page=" + str(page)
			ret = start(url, d)
			if ret == 0:
				#print i
				break
			page = page + 1
		#i = i  + 1
		#if i >=9999999999:
		#	break
	f.close()
	ff = open('score.txt', 'w')
	t = sorted(d.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
	for key in t:
		#print str(key[0]) + ' ' + str(key[1]) + '\n'
		ff.write(str(key[0]) + ' ' + str(key[1]) + '\n')

    #id = 'backwasabi'
    #url = "http://xueqiu.com/" + id
    #start(url)


#	timer = threading.Timer(7200, pawner)
#	timer.start()

if __name__ == "__main__":



##	timer = threading.Timer(7200, pawner)
#	timer.start()


	pawner()
