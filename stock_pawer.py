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
 

def start(url):
   # try:
    browser = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')
    url = url
    browser.get(url)

    t = browser.page_source

    pn = re.compile(ur'(.*)"statuses":(.*?)}]', re.S)
    match = pn.match(t)

    result =  match.group(2)
    result = result + '}]'
    decode = json.loads(result)
    
    f = open('stock.txt', 'r')
    today = datetime.now()
    
    stoday = today.strftime("%Y-%m-%d 00:00:00")
    print stoday
  #  timeArray = time.strptime(stoday, "%Y-%m-%d 00:00:00")

   # timeStamp = int(time.mktime(timeArray))
  #  print timeStamp

    while 1:
		line = f.readline()

		if not line:
			break
		print line
		array = line[:-1].split('%')
		print array[0], array[1]
		

    print decode[0]['description'].encode('utf-8')

    browser.close()
    browser.quit()

def pawner():

	f = open('id.txt', 'r')
	while 1:
		user = f.readline()

		if not user:
			break

		url = "http://xueqiu.com/" + user
		start(url)
    #id = 'backwasabi'
    #url = "http://xueqiu.com/" + id
    #start(url)


#	timer = threading.Timer(7200, pawner)
#	timer.start()

if __name__ == "__main__":



##	timer = threading.Timer(7200, pawner)
#	timer.start()


	pawner()
