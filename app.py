from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://fmp:1234@fmp.fm5gjur.mongodb.net/?retryWrites=true&w=majority")
db = client.fmp

# 호영
@app.route('/')
def home():
  return render_template('index.html')

@app.route("/", methods=["POST"])
def home_post():
  
  doc={
  }
  
  db.mars.insert_one(doc)
  return jsonify({'msg': '완료!'})

@app.route("/", methods=["GET"])
def home_get():
  all_article = list(db.article.find({},{'_id':False}))
  return jsonify({'orders': all_article})


  
@app.route('/board')
def board():
  return render_template('board.html')

@app.route("/board", methods=["POST"])
def board_post():
  
  doc={
  }
  
  db.mars.insert_one(doc)
  return jsonify({'msg': '완료!'})

@app.route("/board", methods=["GET"])
def board_get():
  all_article = list(db.article.find({},{'_id':False}))
  return jsonify({'orders': all_article})
 
@app.route('/petcafe')
def petcafe():
  return render_template('petcafe.html')

@app.route("/petcafe", methods=["POST"])
def petcafe_post():
  
  doc={
  }
  
  db.mars.insert_one(doc)
  return jsonify({'msg': '완료!'})

@app.route("/petcafe", methods=["GET"])
def petcafe_get():
  all_article = list(db.article.find({},{'_id':False}))
  return jsonify({'orders': all_article})
  

  # 지현 
@app.route('/petcafe/suwon')
def petcafe_suwon():
  return render_template('petcafe.html')

@app.route("/petcafe/suwon", methods=["POST"])
def petcafe_suwon_post():
  
  doc={
  }
  
  db.mars.insert_one(doc)
  return jsonify({'msg': '완료!'})

@app.route("/petcafe/suwon", methods=["GET"])
def petcafe_suwon_get():
  all_article = list(db.article.find({},{'_id':False}))
  return jsonify({'orders': all_article})


# 진솔
@app.route('/pethospital')
def pethospital_seoul():
  return render_template('pethospital.html')

@app.route("/pethospital", methods=["POST"])
def pethospital_seoul_post():
  
  doc={
  }
  
  db.mars.insert_one(doc)
  return jsonify({'msg': '완료!'})

@app.route("/pethospital", methods=["GET"])
def pethospital_seoul_get():
  all_article = list(db.article.find({},{'_id':False}))
  return jsonify({'orders': all_article})
  
  
# 제이
@app.route('/petcafe/incheon')
def petcafe_incheon():
  return render_template('petcafe.html')

@app.route("/petcafe/incheon", methods=["POST"])
def petcafe_incheon_post():
  
  doc={
  }
  
  db.mars.insert_one(doc)
  return jsonify({'msg': '완료!'})

@app.route("/petcafe/incheon", methods=["GET"])
def petcafe_incheon_get():
  all_article = list(db.article.find({},{'_id':False}))
  return jsonify({'orders': all_article})
  
if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)