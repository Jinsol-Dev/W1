from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

client = MongoClient("mongodb+srv://fmp:1234@fmp.fm5gjur.mongodb.net/?retryWrites=true&w=majority")
db = client.fmp

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://map.kakao.com/")
#
# driver.find_element(By.ID, "search.keyword.query").send_keys('경기도 애견 카페')
# driver.find_element(By.ID, 'search.keyword.submit').send_keys(Keys.ENTER)
#
# time.sleep(2)
#
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# cafe_lists = soup.select('#info\.search\.place\.list > li')
# for cafe in cafe_lists:
#     name = cafe.select_one('div.head_item.clickArea > strong > a.link_name').text
#     time = cafe.select_one('div.info_item > div.openhour > p > a').text
#     phone = cafe.select_one('div.info_item > div.contact.clickArea > span.phone').text
#     category = name.replace(name, '카페')
#
#     doc = {'name': name,
#            'time': time,
#            'phone': phone,
#            'category': category
#            }
#
#     db.petcafe.insert_one(doc)
#
# time.sleep(2)
#
# driver.quit()

# 호영
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def home_post():
    doc = {
    }

    db.mars.insert_one(doc)
    return jsonify({'msg': '완료!'})


@app.route("/", methods=["GET"])
def home_get():
    all_article = list(db.article.find({}, {'_id': False}))
    return jsonify({'orders': all_article})


@app.route('/board')
def board():
    return render_template('board.html')


@app.route("/board", methods=["POST"])
def board_post():
    doc = {
    }

    db.mars.insert_one(doc)
    return jsonify({'msg': '완료!'})


@app.route("/board", methods=["GET"])
def board_get():
    all_article = list(db.article.find({}, {'_id': False}))
    return jsonify({'orders': all_article})


# 지현
@app.route('/petcafe')
def petcafe():
    return render_template('petcafe.html')


@app.route("/petcafe", methods=["POST"])
def petcafe_Gyeonggi_post():
    return jsonify({'msg': '완료!'})


@app.route("/petcafe_get", methods=["GET"])
def petcafe_Gyeonggi_get():
    petcafe_list = list(db.petcafe.find({}, {'_id': False}))
    return jsonify({'petcafe': petcafe_list})


# 진솔
@app.route('/petcafe/seoul')
def petcafe_seoul():
    return render_template('petcafe.html')


@app.route("/petcafe/seoul", methods=["POST"])
def petcafe_seoul_post():
    doc = {
    }

    db.mars.insert_one(doc)
    return jsonify({'msg': '완료!'})


@app.route("/petcafe/seoul", methods=["GET"])
def petcafe_seoul_get():
    all_article = list(db.article.find({}, {'_id': False}))
    return jsonify({'orders': all_article})


# 제이
@app.route('/petcafe/incheon')
def petcafe_incheon():
    return render_template('petcafe.html')


@app.route("/petcafe/incheon", methods=["POST"])
def petcafe_incheon_post():
    doc = {
    }

    db.mars.insert_one(doc)
    return jsonify({'msg': '완료!'})


@app.route("/petcafe/incheon", methods=["GET"])
def petcafe_incheon_get():
    all_article = list(db.article.find({}, {'_id': False}))
    return jsonify({'orders': all_article})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
