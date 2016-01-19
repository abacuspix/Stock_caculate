
#!/usr/bin/env python
#-*-coding: utf-8-*-
import urllib2
import socket
counter = 600000
SZ_Number = 000000
from time import sleep, ctime
sh_url='http://hq.sinajs.cn/list=sh'
sz_url='http://hq.sinajs.cn/list=sz002562'

while counter < 602000:

    raw_data = urllib2.urlopen(sh_url+str(counter)).read()
    sleep(3)
    #print raw_data
    counter += 1
    t = raw_data.split(',')
    if len(t[0][21:30])< 6:
        #print "Not exist this number :" + str(counter)
        continue
    #print "StockName:" , t[0][21:30]
    #print len(t[0][21:30])
    #print "TodayOpen:" , t[1]
    #print "YestodayClose:" , t[2]
    #print "CurrentPrice:" , t[3]
    #print "TodayHighest:" , t[4]
    #print "TodayLowest:" , t[5]
    #print "Buy_1:" , t[6]
    #print "Sell_1:" , t[7]
    #print "VolHands:" , t[8]
    #print "VolValue:" , t[9]
    #print "Buy1Vol:" , t[10]
    #print "Buy1Value:" , t[11]
    #print "Buy2Vol:" , t[12]
    #print "Buy2Value:" , t[13]
    #print "Buy3Vol:" , t[14]
    #print "Buy3Value:" , t[15]
    #print "Buy4Vol:" , t[16]
    #print "Buy4Value:" , t[17]
    #print "Buy5Vol:" , t[18]
    #print "Buy5Value:" , t[19]
    #print "Sell1Vol:" , t[20]
    #print "Sell1Value:" , t[21]
    #print "Sell2Vol:" , t[22]
    #print "Sell2Value:" , t[23]
    #print "Sell3Vol:" , t[24]
    #print "Sell3Value:" , t[25]
    #print "Sell4Vol:" , t[26]
    #print "Sell4Value:" , t[27]
    #print "Sell5Vol:" , t[28]
    #print "Sell5Value:" , t[29]
    #print "Date:" , t[30]
    #print "Time:" , t[31]
    changeRate = float((float(t[3]) - float(t[2]))/float(t[2])*100)

    print "%s Change rate: %.2f" % (counter, changeRate) + '%'
    activeBuy = (int(t[10]) + int(t[12]) + int(t[14]))
    activeSell = (int(t[20]) + int(t[22]) + int(t[24]))
    print "Active Buy Vol: %d Active Sell Vol: %d" % (activeBuy, activeSell)

~                                                                                    
