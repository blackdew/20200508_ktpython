from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app.env = 'development'
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/<keyword>')
def download(keyword):
    url = 'https://search.naver.com/search.naver'
    query = dict(query=keyword)
    return render_template('download.html')

app.run()