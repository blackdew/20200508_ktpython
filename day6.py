from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='templates')
app.env = 'development'
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/<keyword>')
def download(keyword):
    url = 'https://search.naver.com/search.naver'
    query = dict(where='image', sm='tab_jum', query=keyword)

    res = requests.get(url, params=query)
    soup = BeautifulSoup(res.content, 'html.parser')
    soup = soup.select('img._img')

    return render_template('download.html', soup=soup)

app.run()