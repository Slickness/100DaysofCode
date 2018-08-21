#!/usr/bin/env python3

'''practice using requests and xpath to get the information needed'''

from lxml import html
import requests

# basic url will see if its dynamic or not
# stockhouse dynamic -- no good
# barchart https://www.barchart.com/stocks/quotes/HUGE.CN

# this will be a loop or function on its own but lets get it working first
# lets get the request, then pass it to functions to get what is wanted
def get_data(stock):
    url = "https://www.barchart.com/stocks/quotes/{}".format(stock)
    page = requests.get(url) # get the page info
    tree = html.fromstring(page.content) # get the tree format
    data = tree.xpath('//tr[@class="odd"]/td/text()')
    return data

def get_price(data):
    ''' Get the price in its own function because sometimes it is there twice'''
    for i in range(len(data)):
        if data[i] == "Last Price":
            return data[i+1]

def get_52_high(data):
    ''' Get the 52 week high'''
    for i in range(len(data)):
        if data[i] == "52-Week High":
            return data[i+1] # hmm does the forloop end if i use return

stocks = ["HUGE.CN",
          "HIP.VN",
          "HEXO.TO"]

for stock in stocks:
    data = get_data(stock)
    price = get_price(data)
    high = get_52_high(data)
    print("{} current price is {} and 52 week high is {}".format(stock,price,high))
