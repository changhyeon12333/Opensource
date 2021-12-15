import requests
import soupsieve
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np

#https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-element.do?stn=108&yy=(연도)&obs=(요소)
# for year in list(range(1960:2020):
#
data = []
EleAdd = ['07','08','21']


for year in range(1960,2021):
    for element in EleAdd:
        html="https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-element.do?stn=108&yy=%d&obs=%s" % (year,element)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #ChromeDriverManager().install()로 자동으로 하려고 했지만 코드를 짜던중에 사용자이름을 바꿔 오류가 떠서 절대경로로 해주었다.
        driver.implicitly_wait(3)
        driver.get(html)## 셀레니움 사용으로 웹 크롤링
        ##weather_table > tbody > tr:nth-child(1) > td:nth-child(1) > span
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        for i in range(2,14):
            row = soup.select("#weather_table > tbody > tr:nth-child(32) > td:nth-child(%d) > span" % i)
            data.append(row)

value = []
csv_data = []
for i in data:
    for j in i:
        value.append(j.get_text())## 원하는 값만 추출한다.
for i in value:
    csv_data.append([i])

df = pd.DataFrame(np.array(csv_data))
df.to_csv("C:\\Users\\ChangHyeon\\PycharmProjects\\pythonProject1\\weather.csv",sep=',',encoding = 'utf-8-sig') #csv파일에 한그이 드러가므로 utf-8-sig를 해준다



#반복문을 이용하여 <td> 이런 부분을 제거해준다

# for i in range(1,32):
#     for j in range(1,14):
#         row = soup.select("#weather_table > tbody > tr:nth-child(%d) > td:nth-child(%d) > span" % (i, j))
#         data.append(row)

# print(data)
# temp_data = []
#
# for i in data:
#     day = data[0::13]
#

# for a,b,c,d,e,f,h,i,j,k,l,m in zip(day,month1,month2,month3,month4,month5,month6,month7,month8,month9,month10,month11,month12):
#     for n,o,p,q,r,s,t,u,v,w,x,y,z in zip(a,b,c,d,e,f,h,i,j,k,l,m):
#         print(n.get_text(),o.get_text(),p.get_text(),q.get_text(),r.get_text(),s.get_text(),t.get_text(),u.get_text(),v.get_text(),w.get_text(),x.get_text(),y.get_text(),z.get_text(),sep='\t')
#

        # print(j.get_text(), end = ' ')


# el = row.selct("span")
# for i in row:
#     print(i.get_text())
#print(row)

 ## 온도Temperatue