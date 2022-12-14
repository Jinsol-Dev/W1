from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import datetime as dt
from bson.objectid import ObjectId

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
        return render_template('index.html', nickname=user_info["nick"], userid=user_info["id"])
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
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        return render_template('board.html', nickname=user_info["nick"], userid=user_info["id"])
    except jwt.ExpiredSignatureError:
        return render_template('login.html', msg="로그인 후 이용 가능합니다.", target="board")
    except jwt.exceptions.DecodeError:
        return render_template('login.html', msg="로그인 후 이용 가능합니다.", target="board")

@app.route("/post/board", methods=["POST"])
def board_post():
  createuser = request.form['createuser']
  title_value = request.form["title"]
  content_value = request.form["content"]
  now = dt.datetime.now()
  doc={
    # 유저 값 토큰에서 받아서 넣어야 함.
    'title' : title_value,
    'content' : content_value,
    'createuser' : createuser,
    'createdAt' : now.strftime("%x %X")
  }
  
  db.board.insert_one(doc)
  return redirect(url_for("board"))

@app.route("/post/board/<id>", methods=["POST"])
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
  return redirect(url_for("board"))

@app.route("/del/board/<id>", methods=["POST"])
def board_del_comment(id):
  comment_id = ObjectId(id)
  db.board.delete_one({'_id':comment_id})
  return redirect(url_for("board"))

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

  # 지현 
@app.route('/gyunggi')
def petcafe_Gyeonggi():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        return render_template('petcafe.html', nickname=user_info["nick"], userid=user_info["id"])
    except jwt.ExpiredSignatureError:
        return render_template('login.html', msg="로그인 후 이용 가능합니다.", target="gyunggi")
    except jwt.exceptions.DecodeError:
        return render_template('login.html', msg="로그인 후 이용 가능합니다.", target="gyunggi")

@app.route("/gyunggi", methods=["POST"])
def petcafe_Gyeonggi_post():
  return jsonify({'msg': '완료!'})

@app.route("/gyunggi_get", methods=["GET"])
def petcafe_Gyeonggi_get():
  petcafe_list = list(db.petcafe.find({}))
  
  decoded_all_article = [] 
  for document in petcafe_list :
    document['_id'] = str(document['_id'])
    all_comments = list(db.gyungicom.find({'comment_id' : document['_id']}, {'_id':False}))
    document['comments'] = all_comments
    decoded_all_article.append(document)
  
  return jsonify({'petcafes': decoded_all_article})


# 펫카페 댓글 파트


@app.route("/get/gyunggi/<id>", methods=["GET"])
def gyunggi_get_comment(id):
  print(id)
  cafename = id
  all_comments = list(db.gyungicom.find({'comment_id' :cafename}, {'_id':False}))
  return jsonify({'comments': all_comments})

@app.route("/post/gyunggi/<id>", methods=["POST"])
def gyunggi_post_comment(id):
  print(id)
  comment_id = id
  content_value = request.form["content"]
  now = dt.datetime.now()
  doc={
    # 유저 값 토큰에서 받아서 넣어야 함.
    'comment_id' : comment_id,
    'content' : content_value,
    'createdAt' : now.strftime("%x %X")
  }
  
  db.gyungicom.insert_one(doc)
  return redirect(url_for("petcafe_Gyeonggi"))

# 병원 댓글 파트
@app.route("/get/seoul/<id>", methods=["GET"])
def seoul_get_comment(id):
  print(id)
  cafename = id
  all_comments = list(db.seoulcom.find({'comment_id' :cafename}, {'_id':False}))
  return jsonify({'comments': all_comments})

@app.route("/post/seoul/<id>", methods=["POST"])
def seoul_post_comment(id):
  print(id)
  comment_id = id
  content_value = request.form["content"]
  now = dt.datetime.now()
  doc={
    # 유저 값 토큰에서 받아서 넣어야 함.
    'comment_id' : comment_id,
    'content' : content_value,
    'createdAt' : now.strftime("%x %X")
  }
  
  db.seoulcom.insert_one(doc)
  return redirect(url_for("pethospital_Seoul"))



# 진솔
@app.route('/seoul')
def pethospital_Seoul():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        return render_template('pethospital.html', nickname=user_info["nick"], userid=user_info["id"])
    except jwt.ExpiredSignatureError:
        return render_template('login.html', msg="로그인 후 이용 가능합니다.", target="seoul")
    except jwt.exceptions.DecodeError:
        return render_template('login.html', msg="로그인 후 이용 가능합니다.", target="seoul")

# @app.route("/seoul", methods=["POST"])
# def pethospital_Seoul_post(): 
#     return jsonify({'msg': '완료!'})

@app.route("/seoul_get", methods=["GET"])
def pethospital_Seoul_get():
  all_pethospital = list(db.pethospital.find({}))
  
  decoded_all_article = [] 
  for document in all_pethospital :
    document['_id'] = str(document['_id'])
    all_comments = list(db.pethospital.find({'comment_id' : document['_id']}, {'_id':False}))
    document['comments'] = all_comments
    decoded_all_article.append(document)
  
  return jsonify({'pethospital': decoded_all_article})

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
      # *** 수정 내용 : 닉네임 중복 체크 추가 ***
      if db.user.find_one({'nick': nickname_receive}) :
        return jsonify({'msg': '이미 등록된 닉네임입니다.'})
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
            # *** 수정 내용 : 30 > 10 (로그인 유지 시간) ***
            'exp': dt.datetime.utcnow() + dt.timedelta(minutes=10)
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
    