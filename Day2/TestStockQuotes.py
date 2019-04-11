__author__ = 'rdhek'
import urllib2
import json,ast
from pprint import  pprint as pp
from prettytable import PrettyTable

class GoogleFinanceAPI:
    def __init__(self):
        self.prefix = "http://finance.google.com/finance/info?client=ig&q="
        self.content=[]

    def get(self,listOfStocks,exchange):
        try:
            for stock in listOfStocks:
                url = self.prefix+"%s:%s"%(exchange,stock)
                u = urllib2.urlopen(url)
                jsonStr = u.read()
                obj = json.loads(jsonStr[3:])
                stockList=dict([(str(k), str(v)) for k, v in obj[0].items()])
                #print stockList
                self.content.append(stockList)
            return self.content
        except Exception, e:
            print  e

    def displayQuote(self,stockList):
            self.content.append(stockList)

    def myDashBoard(self, buygpricePerStock,livePricePerStock):
        net={}
        for (quote1, cp),(quote2,lp)in zip(buygpricePerStock.items(),livePricePerStock.items()):
            net[quote1]=format((float(lp)- cp[0])*cp[1],'.2f')
        return net


if __name__ == "__main__":
    c = GoogleFinanceAPI()
    #listOfStocks = raw_input("Enter the list of Stocks")
    #list = map(str,listOfStocks.split())
    listLowCap =['DEN','PIONEEREMB','HCC','EDELWEISS','WELCORP','BLISSGVS','DLINKINDIA','KPIT','CROMPGREAV','PINCON','SPICEJET','ASTRAMICRO']
    #list =['TCI']
    listMidCap = ['SBIN','ICICIBANK','AXISBANK','AUROPHARMA','GLENMARK','SUNPHARMA','CADILAHC','WIPRO','MINDTREE','ADANIPORTS','IBULHSGFIN','ITC','HSIL','TCI']
    listHighCap=['INFY','LT','EMAMILTD','HDFC','HDFCBANK']
    listBought = ['EDELWEISS','ICICIBANK','AUROPHARMA','TCI','ASTRAMICRO','PINCON']
    livePrice={}
    #stockListLowCap=c.get(listLowCap,"NSE")
    #stockListMidCap=c.get(listMidCap,"NSE")
    #stockListHighCap=c.get(listHighCap,"NSE")
    stockListBought=c.get(listBought,"NSE")
    buypricePerStock={'EDELWEISS':[93.15,100],'ICICIBANK':[255.65,19],'AUROPHARMA':[698.75,7],'TCI':[174.74,50],'ASTRAMICRO':[113.75,70],'PINCON':[60.05,100]}
    displayStocks = PrettyTable(["Exchange","Stock","Live Price","Time","Previous Close","Change" , "Change Percentage"])
    displayStocks.padding_width=1
    for stocks in stockListBought:
        displayStocks.add_row([stocks['e'],stocks['t'],stocks['l'],stocks['lt'],stocks['pcls_fix'],stocks['c_fix'],stocks['cp_fix']])
        livePrice[stocks['t']]=stocks['l']
    print displayStocks

    netPrice=c.myDashBoard(buypricePerStock,livePrice)
    myDashBoard = PrettyTable(["Exchange","Stock","Live Price", "Cost Price","Quantity","NetProfit"])
    myDashBoard.padding_width=1
    count = 0

    for price in netPrice:
        myDashBoard.add_row(["NSE",listBought[count],livePrice[listBought[count]],buypricePerStock[listBought[count]][0],buypricePerStock[listBought[count]][1],netPrice[listBought[count]]])
        count = count + 1
    print "\n\n"
    print "---" *8 , "My Dashboard" , "---"*8
    print myDashBoard
    total = PrettyTable(["TotalProfit/Loss"])
    totalProfitLoss = 0

    for item in netPrice:
        totalProfitLoss = totalProfitLoss + float(netPrice[item])
    total.add_row([format(totalProfitLoss,'.2f')])
    print "\n\n"
    print total

#list[count],stockList[list[count]]['t'],buygpricePerStock[list[count]][1]




