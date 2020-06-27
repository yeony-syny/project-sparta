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


@app.route('/search', methods=['POST'])
def search_post():
    # 1. 클라이언트가 준 title 가져오기
    # 2. DB에서 정보 찾기
    # a = list(db.tvprogram.find({},{'_id':0})
    # 3. 성공 여부 확인
    # 4. 성공 메세지(=검색결과) 반환하기

    title_receive = request.form['title_give']
    # ssresult = list(db.tvprogram.find({'title':title_receive}))

    # print(ssresult)

    return jsonify({'result': 'success','correct_title':title_receive})



@app.route('/search', methods=['GET'])
def search_list():
    # 1. 모든 /search의 문서를 가져온 후 list로 변환하기
    # 2. 성공메세지와 함께 리스트 보내기

    sssresult = list(db.tvprogram.find({},{'_id':0}))
    
    return jsonify({'result': 'success','sssresult':sssresult})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

    
