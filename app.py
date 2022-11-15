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
  box_receive = request.form['box_give']
  print(request)
  doc={'box' : box_receive,
       'a' :2
  }
  
  db.fmp.insert_one(doc)
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
  title_value = request.form["title"]
  content_value = request.form["content"]
  doc={
    # 유저 값 토큰에서 받아서 넣어야 함.
    'title' : title_value,
    'content' : content_value
  }
  
  db.board.insert_one(doc)
  return render_template('board.html')

@app.route("/board", methods=["POST"])
def board_post():
  title_value = request.form["title"]
  content_value = request.form["content"]
  doc={
    # 유저 값 토큰에서 받아서 넣어야 함.
    'title' : title_value,
    'content' : content_value
  }
  
  db.board.insert_one(doc)
  return render_template('board.html')

@app.route("/board/get", methods=["GET"])
def board_get():
  all_article = list(db.board.find({}))
  
  decoded_all_article = []
  for document in all_article :
    document['_id'] = str(document['_id'])
    decoded_all_article.append(document)
    
  all_comments = list(db.comments.find({}, {'_id':False}))
  
  return jsonify({'articles': decoded_all_article})

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
@app.route('/petcafe/seoul')
def petcafe_seoul():
  return render_template('petcafe_seoul.html')

@app.route("/petcafe/seoul", methods=["POST"])
def petcafe_seoul_post():
  
  doc={
  }
  
  db.mars.insert_one(doc)
  return jsonify({'msg': '완료!'})

@app.route("/petcafe/seoul", methods=["GET"])
def petcafe_seoul_get():
  all_article = list(db.article.find({},{'_id':False}))
  return jsonify({'orders': all_article})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True) 