from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://test:sparta@cluster0.lwbd7w1.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.dbsparta

@app.route('/')
def home():
  return render_template('index.html')

@app.route("/mars", methods=["POST"])
def board_post():
  
  doc={
  }
  
  db.mars.insert_one(doc)
  return jsonify({'msg': '완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
  all_article = list(db.article.find({},{'_id':False}))
  return jsonify({'orders': all_article})

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)