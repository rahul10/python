#!/usr/bin/python
#importing modules
import bs4
from bs4 import BeautifulSoup
import requests

r=requests.get("http://www.espncricinfo.com/")		#requesting webpage
data =r.text						#retrieving html code
bdata=BeautifulSoup(data)				#converting code
ldata=bdata.find_all('span')[6]
print ldata.text
ldata=bdata.find_all('span')[8]
print ldata.text
ldata=bdata.find_all('span')[10]
print ldata.text


adata=bdata.find_all('a')
m1=adata[7].attrs['href']
m2=adata[8].attrs['href']
m3=adata[9].attrs['href']
#print("m1=", m1)
cs= m1.replace("'", "")

rm1=requests.get("http://www.espncricinfo.com"+cs)
print("http://www.espncricinfo.com"+m1)
m1data=rm1.text
m1bdata=BeautifulSoup(m1data)
#m1adata=m1bdata.find_all('div')
#for i in m1adata:
#	if (i.get('class'))=='cscore_score':
#		print 4
for div in m1bdata.find_all(name='div', attrs={"class":"cscore_score"}):
	print(div.get_text())
