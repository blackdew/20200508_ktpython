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
    word_dict = {}
    if request.method == 'POST':
        # 문자열 전처리
        words = request.form.get('lyrics').strip().lower()
        words = words.replace('\n', ' ')
        specials = set(words) - set('abcdefghijklmnopqrstuvwxyz ')
        for s in specials:
            words = words.replace(s, '')

        # 단어 카운트
        words = words.split(' ')
        word_dict = {w: words.count(w) for w in set(words)}
        # word_dict = {}
        # for w in words:
        #     if w not in word_dict:
        #         word_dict[w] = 0
        #     word_dict[w] += 1

    return render_template('word_count.html', words=word_dict)

app.run()