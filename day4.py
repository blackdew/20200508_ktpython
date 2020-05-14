from flask import Flask, render_template, request
from konlpy.tag import Kkma
import requests
import re

app = Flask(__name__, template_folder='templates')
app.env = 'development'
app.debug = True
kkma = Kkma()

@app.route('/')
def index():
    # return "Welcome, class day 4"
    return render_template('index.html', message="my message")

@app.route('/wordcount/<lang>', methods=['get', 'post'])
def wordcount(lang):
    words = []
    if request.method == 'POST':
        if lang == 'en':
            # 문자열 전처리
            words = request.form.get('lyrics').strip().lower()
            words = words.replace('\n', ' ')
            specials = set(words) - set('abcdefghijklmnopqrstuvwxyz ')
            for s in specials:
                words = words.replace(s, '')

            # 단어 카운트
            words = words.split(' ')
            words = [(w, words.count(w)) for w in set(words)]
            words = sorted(words, key=lambda x: x[1], reverse=True)
        else:
            # 한글의 경우 단어카운트
            words = request.form.get('lyrics').strip()
            words = kkma.pos(words)
            words = [w for w in words if w[1] in ['NNG', 'NNP']]

            words = [(w, words.count(w)) for w in set(words)]
            words = sorted(words, key=lambda x: x[1], reverse=True)

    return render_template('word_count.html', 
                            words=words, lang=lang)

@app.route('/requests', methods=['get', 'post'])
def req():
    links = []
    if request.method == 'POST':
        url = request.form.get('url')
        res = requests.get(url)

        # url을 추출하세요. 
        regex = re.compile("""href=["'](http[^"']+)["']""")
        links = regex.findall(res.text)
        
    return render_template("requests.html", links=links)

app.run()