from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')
app.env = 'development'
app.debug = True

@app.route('/')
def index():
    # return "Welcome, class day 4"
    return render_template('index.html', message="my message")

@app.route('/wordcount', methods=['get', 'post'])
def wordcount():
    words = []
    if request.method == 'POST':
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

    return render_template('word_count.html', words=words)

app.run()