from flask import Flask, render_template, request, session, redirect
import os 
import requests
from bs4 import BeautifulSoup
import pymysql

app = Flask(__name__, template_folder='templates')
app.env = 'development'
app.debug = True
app.secret_key = 'sookbun'

db = pymysql.connect(
    user='root',
    passwd='',
    db='web',
    host='localhost',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

def get_menu():
    cursor = db.cursor()
    cursor.execute("select id, title from topic order by title desc")
    return cursor.fetchall()

@app.route('/')
def index():
    return render_template('index2.html', 
                            menu=get_menu(),
                            user=session.get('user'))

@app.route('/<cid>')
def content(cid):
    cursor = db.cursor()
    cursor.execute(f"""
        select id, title, description, created, author_id from topic
        where id = '{ cid }'
    """)
    content = cursor.fetchone()
    return render_template('template.html', 
                            menu=get_menu(),
                            content=content)

@app.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    cursor = db.cursor()
    cursor.execute(f"""
        select id, name, profile from author
        where name = '{ request.form['userid'] }' and
              password = SHA2('{ request.form['password'] }', 256)
    """)
    user = cursor.fetchone()
    if user:
        session['user'] = user
        return redirect('/')
    else:
        return render_template('login.html', msg="로그인 정보를 확인하세요")

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@app.route('/download/<keyword>', methods=['get', 'post'])
def download(keyword):
    if request.method == 'GET':
        return render_template('download.html', keyword=keyword)

    url = 'https://search.naver.com/search.naver'
    query = dict(where='image', sm='tab_jum', query=keyword)

    res = requests.get(url, params=query)
    soup = BeautifulSoup(res.content, 'html.parser')
    img_links = [tag.get('data-source') 
                 for tag in soup.select('img._img')]

    # 디렉토리 생성
    os.makedirs(f'static/download/{keyword}', exist_ok=True)

    # 다운로드
    for i, link in enumerate(img_links):
        res = requests.get(link)
        with open(f'static/download/{keyword}/{i}.jpg', 'wb') as f:
            f.write(res.content)

    return render_template('download.html', 
        keyword=keyword, img_links=img_links)

app.run()