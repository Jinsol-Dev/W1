from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient("mongodb+srv://fmp:1234@fmp.fm5gjur.mongodb.net/?retryWrites=true&w=majority")
db = client.fmp

url = "https://map.kakao.com/"

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)

previous = driver.execute_script("return document.body.scrollHeight")
interveal = 5

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interveal)
    current = driver.execute_script("return document.body.scrollHeight")

    if previous == current:
        break

    previous = current

soup = BeautifulSoup(driver.page_source, "html.parser")
items = soup.find_all("li", attrs={"class": "basicList_item__0T9JD"})

try :
    for i, item in enumerate(items):
        # print("*" * 100)
        # print(f"{i+1} 번째 상품")

        title = item.find("div", attrs={"class": "basicList_title__VfX3c"}).text
        print(title)

        price = item.find("span", attrs={"class": "price_num__S2p_v"}).text
        print(price)

        url = item.find("a")["href"]
        print(url)

        img = item.find("img")["src"]
        print(img)

        doc = {'title': title,
               'price': price,
               'url': url,
               'img': img}
        db.lodging.insert_one(doc)

except Exception:
    pass