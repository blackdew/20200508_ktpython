from flask import Flask, render_template, request
import os 
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='templates')
app.env = 'development'
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

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