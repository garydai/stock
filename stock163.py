# -*- coding: utf-8-*-
# @Date    : 2014-05-20
# @Author  : Lifemaxer
# @Website : http://lifemaxer.com
# @Description1:  python-大批量自动采集获取网易财经所有A股上市公司股票资产负债率
# @Description2:  并导入excel表格中
# @Description3:  替换下方中文可修改成获取任意财务数据
# @Tools-Required: BeautifulSoup, xlwt
import re,urllib2
import xlwt
from bs4 import BeautifulSoup
count1 = 1
class getstock:
    def __init__(self):
        pass
     
    def go(self, count):
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
            return
        soup = BeautifulSoup(content)

        c = soup.findAll('div',class_='relate_stock clearfix')
        #print c
        name = soup.find('h1',class_='name').contents[1].contents[0].encode('utf-8')
        industry = c[1].find('li')

        industry_name = industry.contents[0].contents[0].encode('utf-8').strip()
        print industry_name
        print name
        if name != '':
            #print name
            ws.write(str(str(count).zfill(6))+'%'+str(name)+ '%'+str(industry_name) +'\n')

        #获取负债率
     #   a = soup.find_all(class_='table_bg001 border_box fund_analys')
     #   for i in a:
            #此处替换中文可修改成获取任意财务数据
      #      if i.find('td',text=re.compile(u'资产负债率')):
        #       b = i.find('td',text=re.compile(u'资产负债率')).parent.contents
               #网易财经默认一页最多显示2008-2013年年报共6年
        #       number = [3,4,5,6,7,8]
         #      for num in number:
         #          if num < len(b):
               #          data = b[num].contents[0].decode('unicode_escape')
               #          ws.write(count, num-1, data)
  
#if __name__ == '__main__':
    #定义excel表格内容
#wb = xlwt.Workbook()
#ws = wb.add_sheet(u'资产负债表')
#ws.write(0, 0, u'股票代码')
#ws.write(0, 1, u'股票名称')
ws = open('stock.txt', 'w')
#ws.write(0, 2, u'2013-12-31')
#ws.write(0, 3, u'2012-12-31')
#ws.write(0, 4, u'2011-12-31')
#ws.write(0, 5, u'2010-12-31')
#ws.write(0, 6, u'2009-12-31')
#ws.write(0, 7, u'2008-12-31')
gs = getstock()
#目前深证最大号为002725，获取上交所创业板请修改相应最大号码


count = 1
while count <=2735:
    try:
        gs.go(count)
        print count
        #wb.save('stockdebt.xls')
        count1 += 1
        count += 1
    except Exception,e:
        print e
        count1 += 1
        count += 1
        
    #break

count = 300000
while count <=300409:
    try:
        gs.go(count)
        print count
        #wb.save('stockdebt.xls')
        count1 += 1
        count += 1
    except Exception,e:
        print e
        count1 += 1
        count += 1
        

count = 600000
while count <=603998:
    try:

        gs.go(count)
        print count
        #wb.save('stockdebt.xls')
        count1 += 1
        count += 1
    except Exception,e:
        print e
        count1 += 1
        count += 1
        


