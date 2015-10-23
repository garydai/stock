# -*- coding: utf-8-*-

#抓取网易的股票信息，股票名字、代码、所属行业
import re,urllib2
import xlwt
from bs4 import BeautifulSoup



count1 = 1
class getstock:
    def __init__(self):
        pass
     
    def go(self, count, summ):
        #定义网址，获取上交所创业板只需对应修改stock_num为6开头或3开头即可
        stock_num = str(count).zfill(7)
        if count > 600000:
            stock_num = str(count).zfill(7)  
        else:
            stock_num = '1' + str(count).zfill(6)  
        print stock_num
        url = 'http://quotes.money.163.com/'+stock_num+'.html'
        print url
        #print("股票代码:" + stock_num)
        headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"}
        req = urllib2.Request( url, headers = headers)
        try:
            content = urllib2.urlopen(req).read()
        except Exception,e:
            print e
            return 0
        soup = BeautifulSoup(content)
      #  print content
        c = soup.findAll('div', {'class':'stock_info'})
       # print c
        name = soup.find('h1',{'class':'name'}).contents[1].contents[0].encode('utf-8')
       # print name

        c = soup.findAll('div', {'class':'relate_stock clearfix'})
       # print c[1]
        c1 = c[1].find('li')
        industry_name =  c1.contents[0].string.encode('utf-8').strip()
        #print name
        #industry = c[1].find('li')

        #industry_name = industry.contents[0].contents[0].encode('utf-8').strip()
        print industry_name
        print name
        if name != '':
            print summ
            #print name
            #ws.write(str(str(count).zfill(6))+'%'+str(name)+ '%'+str(industry_name) +'\n')
            ws.write(summ, 0, str(count).zfill(6))
            ws.write(summ, 1, name.decode('utf-8'))
            ws.write(summ, 2, industry_name.decode('utf-8'))
            return 1
     
        return 0
  

#if __name__ == '__main__':
    #定义excel表格内容
wb = xlwt.Workbook()
ws = wb.add_sheet(u'stock')
ws.write(1, 0, u'股票代码')
ws.write(1, 1, u'股票名称')
ws.write(1, 2, u'股票板块')
ws.write(0, 3, u'统计时间')
ws2 = wb.add_sheet(u'industry')
ws2.write(1, 0, u'股票板块')
ws2.write(0, 1, u'统计时间')


#ws = open('stock.txt', 'w')
#ws.write(0, 2, u'2013-12-31')
#ws.write(0, 3, u'2012-12-31')
#ws.write(0, 4, u'2011-12-31')
#ws.write(0, 5, u'2010-12-31')
#ws.write(0, 6, u'2009-12-31')
#ws.write(0, 7, u'2008-12-31')

gs = getstock()
#目前深证最大号为002725，获取上交所创业板请修改相应最大号码

summ = 2
count = 1
while count <=2735:
    try:
        ret = gs.go(count, summ)
        if ret == 1:
            
            summ += 1
            wb.save('stock.xls')
            print 'success'
        print count
        #wb.save('stockdebt.xls')
        count1 += 1
        count += 1

    except Exception,e:
        print e
        print 'fail'
        count1 += 1
        count += 1
        
    #break

count = 300000
while count <=300409:
    try:
        ret = gs.go(count, summ)
        if ret == 1:
            
            summ += 1
            wb.save('stock.xls')
            print 'success'
        print count
        #wb.save('stockdebt.xls')
        count1 += 1
        count += 1
    except Exception,e:
        print e
        print 'fail'
        count1 += 1
        count += 1
        

count = 600000
while count <=603998:
    try:

        ret = gs.go(count, summ)
        if ret == 1:

            summ += 1
            wb.save('stock.xls')
            print 'success'
        print count
        #wb.save('stockdebt.xls')
        count1 += 1
        count += 1
    except Exception,e:
        print e
        print 'fail'
        count1 += 1
        count += 1
        
wb.save('stock.xls')

