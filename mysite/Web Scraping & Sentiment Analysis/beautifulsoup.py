import bs4 as bs
import urllib.request
import final2 as s

#url 1 : https://www.unigo.com/colleges/new-jersey-institute-of-technology/2
#url 2 : https://www.unigo.com/colleges/rochester-institute-of-technology
#url 3 : https://www.unigo.com/colleges/ohio-state-university-main-campus
#url 4 : https://www.unigo.com/colleges/florida-memorial-university

def printing():
    even = 1
    for paragraph in body.find_all('p'):
        if(even):
            print(paragraph.text)
            print(s.sentiment(paragraph.text))

            print('__________________________________________________')
            even-=1
            continue
        even+=1
    
sauce = urllib.request.urlopen('https://www.unigo.com/colleges/florida-memorial-university')

soup = bs.BeautifulSoup(sauce,'lxml')

body = soup.body




printing()
    


