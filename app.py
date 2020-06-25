from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbnetflix                 # 'dbsparta'라는 이름의 db를 만듭니다.

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
    return render_template('index.html')


#  API역할을 하는 부분
@app.route('/member/netfilx', methods=['GET'])


@app.route('/search', methods=['GET'])
def stars_list():
    # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!  -1:desc > 내림차순 1:asc > 오름차순

    stars = list(db.mystar.find({},{'_id':False}).sort('like',-1))
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success','msg':'list 연결되었습니다!','stars':stars})




@app.route('/search', methods=['POST'])
def search_post():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    search_receive = request.form['search_give']

    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    content = db.dbnetchaving.find_one({'search':search_receive})

    db.dbnetchaving.update({'name':name_receive},{'$set':{'like':new_like}})

    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success','msg':'like 연결되었습니다!'})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)