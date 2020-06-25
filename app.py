from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbnetflixTV 

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
    return render_template('index.html')

#  API역할을 하는 부분

# @app.route('/member/netfilx', methods=['GET']) - 삭제

# 검색어를 주고
@app.route('/search', methods=['GET'])
def search_list():
    tvpros = list(db.tvprogram.find({},{'_id':False}))

    return jsonify({'result': 'success','search_list':tvprosss})



# 검색어와 일치하는 콘텐츠를 찾아 돌려준다
@app.route('/search', methods=['POST'])
def search_post():

    title_receive = request.form['title_give']
    tvpro = db.tvprogram.find_one({'title':title_receive})
    

    return jsonify({'result': 'success','msg':'검색어찾기 연결'})






if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)