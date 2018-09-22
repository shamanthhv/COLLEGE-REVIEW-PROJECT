import final2 as s
import time
import urllib
import urllib.request
from urllib.request import urlopen
import re
from http.cookiejar import CookieJar
import http.cookiejar
import datetime
import pprint


cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


def fun(page):
    try:
        sourcecode = opener.open(page).read()

        try:
            reviews_1 = re.findall(b'<div class="comment-body".*?>(.*)</div>', sourcecode)
            for review_1 in reviews_1:
                print("************************************************")
                new=review_1.decode("utf-8")
                print(s.sentiment(new))

        except Exception as e:
                print (e)

    except Exception as e:
        print(e)


def main():
    var=input("Enter 1.RV 2.BIT")
    if var=='1':
        page = 'http://www.stupidsid.com/engineering-college-reviews?id=1155'
        fun(page)
    elif var=='2':
        page = 'http://www.stupidsid.com/me-mtech-college-reviews?id=1225'
        fun(page)
    elif var=='3':
        page='http://www.stupidsid.com/engineering-college-reviews?id=1188'
        fun(page)

main()
