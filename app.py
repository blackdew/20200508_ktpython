from flask import Flask, request
app = Flask(__name__, static_folder='static')
app.env = 'development'
app.debug = True

def get_template(filename):
    with open(f'./web/{filename}', 'r', encoding='utf8') as f:
        content = f.read()
    return content

@app.route('/')
def index():
    f = open('./web/index.html', 'r', encoding='utf8')
    content = f.read()
    f.close()
    return content

@app.route('/html')
def html():
    f = open('./web/template.html', 'r', encoding='utf8')
    content = f.read()
    f.close()
    return content.format('HTML', 'HTML is..')

@app.route('/css')
def css():
    f = open('./web/2.html', 'r', encoding='utf8')
    content = f.read()
    f.close()
    return content

@app.route('/stars/<num>')
def stars(num):
    if not num.isnumeric():
        return "not numeric"

    stars = []
    for i in range(int(num)):
        stars.append("*" * (i + 1))

    return '<br>'.join(stars)

@app.route('/word_count', methods=['get', 'post'])
def word_count():
    dict_word = {}
    if request.method == 'POST':
        text = request.form.get('text')
        print(text)
        words = text.split(' ')
        for w in words:
            if w not in dict_word:
                dict_word[w] = 0
            dict_word[w] += 1
    print(dict_word)

    template = get_template('word_count.html')
    return template.format(result=str(dict_word))

app.run()