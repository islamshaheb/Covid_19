from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.
#1
toi_r = requests.get("https://www.prothomalo.com/topic/%E0%A6%95%E0%A6%B0%E0%A7%8B%E0%A6%A8%E0%A6%BE%E0%A6%AD%E0%A6%BE%E0%A6%87%E0%A6%B0%E0%A6%BE%E0%A6%B8")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')
toi_headings = toi_soup.find_all('h2')
toi_news = []

for t in toi_headings:
    toi_news.append(t.text)
#/1

#2
ht_r = requests.get("https://www.bangla.24livenewspaper.com/coronavirus-update")
ht_soup = BeautifulSoup(ht_r.content, 'html.parser')
#ht_headings = ht_soup.findAll("div", {"class":"sf-item-header-wrapper"})
ht_paragraph = ht_soup.find_all('h3')
#ht_headings = ht_headings[2:]
ht_news = []

#for hth in ht_paragraph:
#    ht_news.append(hth.text)
for ht in ht_paragraph:
    ht_news.append(ht.text)
#/2

#3
third = requests.get("https://www.ittefaq.com.bd/covid19-update")
third_soup = BeautifulSoup(third.content, 'html.parser')
third_headline = third_soup.find_all('h5')
third_news = []

for t in third_headline:
    third_news.append(t.text)
#/3

#4
fourth = requests.get("https://www.bd-pratidin.com/coronavirus/9840")
fourth_soup = BeautifulSoup(fourth.content, 'html.parser')
fourth_headline = fourth_soup.find_all('span')
fourth_news = []

for t in fourth_headline:
    fourth_news.append(t.text)
#/4

def home(request):
    return render(request,'more.html',{'toi_news':toi_news,'ht_news':ht_news, 'third_news': third_news, 'fourth_news': fourth_news})
