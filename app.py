from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import datetime as dt

import jwt
import hashlib
import certifi
SECRET_KEY = 'SPARTA_mini'


ca=certifi.where()

app = Flask(__name__)

client = MongoClient("mongodb+srv://fmp:1234@fmp.fm5gjur.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.fmp



# 호영
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        return render_template('index.html', nickname=user_info["nick"])
    except jwt.ExpiredSignatureError:
        # return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
        return render_template('index.html')
    except jwt.exceptions.DecodeError:
        # return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))
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
  all_article = list(db.article.find({},{'_ id':False}))
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

@app.route("/board/<id>", methods=["POST"])
def board_post_comment(id):
  comment_id = id
  content_value = request.form["content"]
  now = dt.datetime.now()
  doc={
    # 유저 값 토큰에서 받아서 넣어야 함.
    'comment_id' : comment_id,
    'content' : content_value,
    'createdAt' : now.strftime("%x %X")
  }
  
  db.comments.insert_one(doc)
  return render_template('board.html')

@app.route("/board/get", methods=["GET"])
def board_get():
  all_article = list(db.board.find({}))
  
  decoded_all_article = []
  for document in all_article :
    document['_id'] = str(document['_id'])
    all_comments = list(db.comments.find({'comment_id' : document['_id']}, {'_id':False}))
    document['comments'] = all_comments
    decoded_all_article.append(document)
  
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



@app.route('/login')
def login():
      #로그인 중일 경우 로그인 페이지 접근 불가할 수 있도록 설정
      token_receive = request.cookies.get('mytoken')
      try:
          payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
          return redirect(url_for("home"))
      except jwt.ExpiredSignatureError:
          return render_template('login.html')
      except jwt.exceptions.DecodeError:
          return render_template('login.html')


@app.route('/register')
def register():
        #로그인 중일 경우 회원가입 페이지 접근 불가할 수 있도록 설정
        token_receive = request.cookies.get('mytoken')
        try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            return redirect(url_for("home"))
        except jwt.ExpiredSignatureError:
            return render_template('register.html')
        except jwt.exceptions.DecodeError:
            return render_template('register.html')

# 회원가입 세션
@app.route('/api/register', methods=['POST'])
def api_register():

    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    if db.user.find_one({'id': id_receive}) :
      return jsonify({'msg': '이미 등록된 아이디입니다.'})
    else :
      db.user.insert_one({'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive})
      return jsonify({'result': 'success'})
    
# [로그인 API]
# id, pw를 받아서 맞춰보고, 토큰을 만들어 발급합니다.
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
    result = db.user.find_one({'id': id_receive, 'pw': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': id_receive,
            'exp': dt.datetime.utcnow() + dt.timedelta(minutes=30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})
      
#로그아웃
@app.route('/api/logout', methods=['POST'])
def api_logout():
    token_receive = request.cookies.get('mytoken')
    
    userinfo = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    payload = {
        'id':  userinfo['id'],
        'exp': dt.datetime.fromtimestamp(0)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    # token을 줍니다.
    return jsonify({'result': 'success', 'token': token})

# [유저 정보 확인 API]
# 로그인된 유저만 call 할 수 있는 API입니다.

@app.route('/api/nick', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')

    # try / catch 문?
    # try 아래를 실행했다가, 에러가 있으면 except 구분으로 가란 얘기입니다.

    try:
        # token을 시크릿키로 디코딩합니다.
        # 보실 수 있도록 payload를 print 해두었습니다. 우리가 로그인 시 넣은 그 payload와 같은 것이 나옵니다.
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)

        # payload 안에 id가 들어있습니다. 이 id로 유저정보를 찾습니다.
        # 여기에선 그 예로 닉네임을 보내주겠습니다.
        userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})
        return jsonify({'result': 'success', 'nickname': userinfo['nick']})
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})
      
      
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True) 
    