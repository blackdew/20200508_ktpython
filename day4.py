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
    words = ''
    if request.method == 'POST':
        words = request.form.get('lyrics').strip().lower()
        specials = set(words) - set('abcdefghijklmnopqrstuvwxyz ')

        for s in specials:
            words = words.replace(s, '')

    return render_template('word_count.html', words=words)

app.run()