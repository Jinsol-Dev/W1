from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(executable_path='C:\\Users\Jinsol Kim\Desktop/chromedriver.exe')

driver.get("https://map.kakao.com/")

driver.find_element(By.ID, "search.keyword.query").send_keys('경기도 동물병원') # 검색 창
driver.find_element(By.ID, 'search.keyword.submit').send_keys(Keys.ENTER) # Enter로 검색

time.sleep(2)

 # 우선 더보기 클릭해서 2페이지
driver.find_element_by_xpath('//*[@id="info.search.place.more"]').send_keys(Keys.ENTER)
time.sleep(1)
        

from bs4 import BeautifulSoup
import requests 
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient("mongodb+srv://fmp:1234@fmp.fm5gjur.mongodb.net/?retryWrites=true&w=majority")
db = client.fmp

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
hospital_lists = soup.select('#info\.search\.place\.list > li')

for hospital in hospital_lists:
   name = hospital.select_one('div.head_item.clickArea > strong > a.link_name').text
   time = hospital.select_one('div.info_item > div.openhour > p > a').text
   phone = hospital.select_one('div.info_item > div.contact.clickArea > span.phone').text
   address = hospital.select_one('div.info_item > div.addr > p:nth-child(1)').text
   category = name.replace(name, '병원')
         
   doc = {
      'name' : name, 
      'time' : time,
      'phone':  phone,
      'address' : address              
   }
   db.hospitals.insert_one(doc)

   # print(name, time, phone, address)

   


   # 카카오맵 copyselector 결과
   #info\.search\.place\.list > li:nth-child(1) > div.head_item.clickArea > strong > a.link_name
   #info\.search\.place\.list > li:nth-child(1) > div.info_item > div.openhour > p > a
   #info\.search\.place\.list > li:nth-child(1) > div.info_item > div.contact.clickArea > span.phone
   #info\.search\.place\.list > li:nth-child(1) > div.info_item > div.addr > p:nth-child(1)