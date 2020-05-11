from flask import Flask
app = Flask(__name__, static_folder='static')
app.env = 'development'
app.debug = True

@app.route('/')
def index():
    f = open('./web/index.html', 'r', encoding='utf8')
    content = f.read()
    f.close()
    return content

@app.route('/html')
def html():
    f = open('./web/1.html', 'r', encoding='utf8')
    content = f.read()
    f.close()
    return content

@app.route('/css')
def css():
    f = open('./web/2.html', 'r', encoding='utf8')
    content = f.read()
    f.close()
    return content

app.run()